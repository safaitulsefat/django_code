# Generated by Django 5.0.2 on 2024-03-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('taskTitle', models.CharField(max_length=20)),
                ('taskDescription', models.CharField(max_length=20)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
