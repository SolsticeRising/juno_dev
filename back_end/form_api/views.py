from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
import json
from django.core import serializers
import requests

from form_api.serializers import FormSerializers, FieldSerializers
from form_api.models import Form, Field
from form_api.helpers import get_campaign_field_id
# Create your views here.

campaign_headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Api-Token": "264ac68f829ba7af6f8738b2410df0f29665eb2ff99229aea4f42cdb981283f1a5f721dd"
}

campaign_base_url = 'https://myersmdnutrition44171.api-us1.com/api/3';

@api_view(['GET'])
def testview(request):
    print('============= Request Came, Processing Started =============')
    if(request.method == 'GET'):
        return JsonResponse({
            'message': 'API running successfully',
        })

@api_view(['POST'])
def save_form(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        print('------------- Request Came -------------', data)
        form_data = {
            'form_name': data['formName'],
            'form_fields': data['formFields']
        }
        form_obj = FormSerializers(data=form_data)
        if form_obj.is_valid():
            print('---------- Valid Obj')
            form_obj.save()
            return JsonResponse({
                'message': 'Form saved successfully',
            })

@api_view(['GET'])
def form_list(request):
    if(request.method == 'GET'):
        form_list = Form.objects.all()
        print('------------ Form List ------------', serializers.serialize('json', form_list))
        return JsonResponse({
            'message': 'Form List fetched successfully',
            'form_list': serializers.serialize('json', form_list),
        })


@api_view(['POST'])
def save_filled_form(request):
    print(request)
    if(request.method == 'POST'):
        data = JSONParser().parse(request);
        print(data)
        campaignContact = {
            'email': data['Email']['value'],
            'fieldValues': []
        };
        for field_name in data:
            if(field_name != 'Email'):
                field_data = {
                    'email': data['Email']['value'],
                    'field_name': field_name,
                    'field_value': data[field_name]['value'],
                    'campaign_field_name': data[field_name]['campaignField']
                }

                if(field_data['campaign_field_name'] == 'firstName' or field_data['campaign_field_name'] == 'lastName' or field_data['campaign_field_name'] == 'phone'):
                    campaignContact[field_data['campaign_field_name']] = data[field_name]['value'];
                else:
                    campaign_field_id = get_campaign_field_id(field_data['campaign_field_name'], "text");
                    print('field', field_data['campaign_field_name'], ' id = ', campaign_field_id)
                    campaignContact['fieldValues'].append({
                        'field': campaign_field_id,
                        'value': data[field_name]['value'],
                    })

        # url = "https://myersmdnutrition44171.api-us1.com/api/3/contacts"
        # print(campaignContact);
        # response = requests.post(url, headers=campaign_headers, json={'contact': campaignContact})
        # print(response.text)
        return JsonResponse({
            'message': 'Form saved successfully',
        })

@api_view(['POST'])
def save_field(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request);
        data['field_qualifier_data'] = json.dumps(data['field_qualifier_data']);
        print(data)
        if(('required' in data) and data['required'] == 'true'):
            data['required'] = True;
        else:
            data['required'] = False;
        field_obj = FieldSerializers(data=data)
        if(field_obj.is_valid()):
            field_obj.save();
            return JsonResponse({
                'message': 'Field saved successfully',
            })
        return JsonResponse({
            'message': 'Could not save field'
        })

@api_view(['GET'])
def field_list(request):
    if(request.method == 'GET'):
        field_list = Field.objects.all();
        return JsonResponse({
            'message': 'Field List fetched successfully',
            'field_list': serializers.serialize('json', field_list),
        })
