# Generated by Django 3.1.2 on 2020-10-21 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unit_operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit_operation_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Process_Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Process_Parameter_name', models.CharField(max_length=300)),
                ('unit_operation',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kasaapp.unit_operation')),
            ],
        ),
    ]
