# Generated by Django 3.2.4 on 2021-07-14 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0003_alter_event_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
