# Generated by Django 5.0.2 on 2024-02-26 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_delete_studentinfomodel_delete_teacherinfomodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('roll', models.IntegerField()),
                ('payment', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeacherInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
