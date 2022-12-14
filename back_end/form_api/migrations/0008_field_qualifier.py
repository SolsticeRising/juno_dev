# Generated by Django 4.1.1 on 2022-10-03 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form_api', '0007_alter_field_required'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field_qualifier',
            fields=[
                ('qualifier_id', models.AutoField(primary_key=True, serialize=False)),
                ('qualifier_type', models.CharField(max_length=100)),
                ('qualifier_operator', models.CharField(max_length=20)),
                ('qualifier_value', models.CharField(max_length=100)),
                ('field_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_api.field')),
            ],
        ),
    ]
