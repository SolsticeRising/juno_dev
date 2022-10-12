# Generated by Django 4.1.1 on 2022-09-29 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form_api', '0003_userdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('field_id', models.AutoField(primary_key=True, serialize=False)),
                ('field_name', models.CharField(max_length=1000)),
                ('field_type', models.CharField(max_length=100)),
                ('required', models.BooleanField(default=False)),
                ('condition_field_success', models.CharField(max_length=1000)),
                ('campaign_field_name', models.CharField(max_length=1000)),
                ('condition_field_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_api.field')),
            ],
        ),
        migrations.CreateModel(
            name='Field_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_value', models.CharField(max_length=1000)),
                ('field_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_api.field')),
            ],
        ),
        migrations.CreateModel(
            name='Form_data',
            fields=[
                ('filling_id', models.AutoField(primary_key=True, serialize=False)),
                ('form_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_api.form')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('template_id', models.AutoField(primary_key=True, serialize=False)),
                ('template_name', models.CharField(max_length=100)),
                ('template_fields', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='formfield',
            name='form_id',
        ),
        migrations.DeleteModel(
            name='UserDetails',
        ),
        migrations.DeleteModel(
            name='FormField',
        ),
        migrations.AddField(
            model_name='form_data',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_api.user'),
        ),
        migrations.AddField(
            model_name='field_data',
            name='filling_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_api.form_data'),
        ),
    ]