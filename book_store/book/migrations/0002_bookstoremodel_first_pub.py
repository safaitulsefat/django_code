# Generated by Django 5.0.2 on 2024-02-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookstoremodel',
            name='first_pub',
            field=models.DateField(auto_now=True),
        ),
    ]
