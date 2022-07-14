# Generated by Django 3.1.4 on 2021-03-05 09:46

import simplejson.encoder
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artemisdb", "0009_auto_20210304_0947"),
    ]

    operations = [
        migrations.AddField(
            model_name="scan",
            name="diff_summary",
            field=models.JSONField(default=dict, encoder=simplejson.encoder.JSONEncoder),
        ),
    ]
