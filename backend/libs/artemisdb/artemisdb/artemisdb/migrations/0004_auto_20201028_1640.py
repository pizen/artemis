# Generated by Django 3.1 on 2020-10-28 16:40

import simplejson.encoder
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artemisdb", "0003_user_last_login"),
    ]

    operations = [
        migrations.AddField(model_name="scan", name="batch_priority", field=models.BooleanField(default=False)),
        migrations.AddField(
            model_name="scan",
            name="callback",
            field=models.JSONField(default=dict, encoder=simplejson.encoder.JSONEncoder),
        ),
        migrations.AddField(
            model_name="scan",
            name="categories",
            field=models.JSONField(default=list, encoder=simplejson.encoder.JSONEncoder),
        ),
        migrations.AddField(model_name="scan", name="depth", field=models.IntegerField(null=True)),
        migrations.AddField(model_name="scan", name="include_dev", field=models.BooleanField(default=False)),
        migrations.AddField(
            model_name="scan",
            name="plugins",
            field=models.JSONField(default=list, encoder=simplejson.encoder.JSONEncoder),
        ),
    ]
