from rest_framework import serializers
from form_api.models import Form, Field, Template, User, Form_data, Field_data

class FormSerializers(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = (
            'form_name',
            'form_fields',
        )

class FieldSerializers(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = (
            'field_name',
            'field_type',
            'field_options',
            'required',
            'condition_field_id',
            'condition_field_success',
            'campaign_field_name',
            'field_qualifier_data',
        )

class FieldQualifierSerializers(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = (
            'field_id',
            'qualifier_type',
            'qualifier_operator',
            'qualifier_value',
        )

class TemplateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = (
            'template_name',
            'template_fields',
        )

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
        )
