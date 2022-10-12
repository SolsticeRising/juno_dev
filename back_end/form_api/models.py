from django.db import models

# Create your models here.

# class FormField(models.Model):
#     field_id = models.AutoField(primary_key=True)
#     form_id = models.ForeignKey("Form", on_delete=models.CASCADE)
#     field_name = models.CharField(max_length=100)
#     field_type = models.CharField(max_length=100)
#     field_options = models.CharField(max_length=10000)
#
# class UserDetails(models.Model):
#     email=models.CharField(max_length=50)
#     field_name=models.CharField(max_length=100)
#     field_value=models.CharField(max_length=100)
#     campaign_field_name=models.CharField(max_length=100)

class Field(models.Model):
    field_id = models.AutoField(primary_key=True)
    field_name = models.CharField(max_length=1000)
    field_type = models.CharField(max_length=100)
    field_options = models.CharField(max_length=10000, null=True)
    required = models.BooleanField()
    condition_field_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    condition_field_success = models.CharField(max_length=1000, null=True)
    campaign_field_name = models.CharField(max_length=1000, null=True)
    field_qualifier_data = models.CharField(max_length=1000)

class Field_qualifier(models.Model):
    qualifier_id = models.AutoField(primary_key=True)
    field_id = models.ForeignKey('Field', on_delete=models.CASCADE)
    qualifier_type = models.CharField(max_length=100)
    qualifier_operator = models.CharField(max_length=20)
    qualifier_value = models.CharField(max_length=100)

class Form(models.Model):
    form_id = models.AutoField(primary_key=True)
    form_name = models.CharField(max_length=100)
    form_fields = models.CharField(max_length=10000)

class Template(models.Model):
    template_id = models.AutoField(primary_key=True)
    template_name = models.CharField(max_length=100)
    template_fields = models.CharField(max_length=1000)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)

class Form_data(models.Model):
    filling_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    form_id = models.ForeignKey('Form', on_delete=models.CASCADE)

class Field_data(models.Model):
    filling_id = models.ForeignKey('Form_data', on_delete=models.CASCADE)
    field_id = models.ForeignKey('Field', on_delete=models.CASCADE)
    field_value = models.CharField(max_length=1000)
