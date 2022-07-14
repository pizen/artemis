# Generated by Django 3.1 on 2020-10-02 14:34

import django.db.models.deletion
import simplejson.encoder
from django.db import migrations, models

import artemisdb.artemisdb.consts


class Migration(migrations.Migration):

    dependencies = [
        ("artemisdb", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("scope", models.JSONField(encoder=simplejson.encoder.JSONEncoder)),
            ],
        ),
        migrations.AlterField(
            model_name="scan",
            name="status",
            field=models.CharField(
                choices=[
                    (artemisdb.artemisdb.consts.ScanStatus["QUEUED"], "queued"),
                    (artemisdb.artemisdb.consts.ScanStatus["PROCESSING"], "processing"),
                    (artemisdb.artemisdb.consts.ScanStatus["COMPLETED"], "completed"),
                    (artemisdb.artemisdb.consts.ScanStatus["FAILED"], "failed"),
                    (artemisdb.artemisdb.consts.ScanStatus["ERROR"], "error"),
                    (artemisdb.artemisdb.consts.ScanStatus["TERMINATED"], "terminated"),
                ],
                max_length=64,
            ),
        ),
        migrations.CreateModel(
            name="APIKey",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("key_id", models.UUIDField(unique=True)),
                ("key_hash", models.CharField(max_length=256, unique=True)),
                ("name", models.CharField(max_length=256)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("last_used", models.DateTimeField(null=True)),
                ("expires", models.DateTimeField(null=True)),
                ("scope", models.JSONField(encoder=simplejson.encoder.JSONEncoder)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="artemisdb.user")),
            ],
        ),
        migrations.AddField(
            model_name="scan",
            name="owner",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="artemisdb.user"),
        ),
    ]
