# Generated by Django 4.1.1 on 2022-09-14 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('form_id', models.AutoField(primary_key=True, serialize=False)),
                ('form_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('field_id', models.AutoField(primary_key=True, serialize=False)),
                ('field_name', models.CharField(max_length=100)),
                ('field_type', models.CharField(max_length=100)),
                ('field_options', models.CharField(max_length=10000)),
                ('form_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_api.form')),
            ],
        ),
    ]
