# Generated by Django 4.1.1 on 2022-09-29 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_api', '0004_field_field_data_form_data_template_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='field_options',
            field=models.CharField(default=1, max_length=10000),
            preserve_default=False,
        ),
    ]
