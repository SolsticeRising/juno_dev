import requests;
import json;

campaign_headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Api-Token": "264ac68f829ba7af6f8738b2410df0f29665eb2ff99229aea4f42cdb981283f1a5f721dd"
};

campaign_base_url = 'https://myersmdnutrition44171.api-us1.com/api/3';

def create_campaign_field(field_name, field_type):
    print('-----------------')
    print(field_name, field_type)
    print('-----------------')
    field_create_response = requests.post(campaign_base_url+'/fields', headers=campaign_headers, json={
        'field':{
            'type': field_type,
            'title': field_name,
        }
    });
    print(json.loads(field_create_response.text));
    return json.loads(field_create_response.text)['field']['id']

def get_campaign_field_id(field_name, field_type):
    campaign_field_list = requests.get(campaign_base_url+'/fields?limit=200', headers=campaign_headers);
    allFields = json.loads(campaign_field_list.text)['fields'];
    for field in allFields:
        if(field['title'] == field_name):
            return field['id'];
    new_field_id = create_campaign_field(field_name, field_type);
    return new_field_id;

def create_campaign_contact(data):
    pass

def get_campaign_contact_id():
    pass

def create_campaign_deal(data):
    pass
