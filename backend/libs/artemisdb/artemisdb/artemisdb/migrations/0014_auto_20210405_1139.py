# Generated by Django 3.1.7 on 2021-04-05 11:39

from django.db import migrations, models

import artemisdb.artemisdb.consts


class Migration(migrations.Migration):

    dependencies = [
        ("artemisdb", "0013_remove_scan_error_msg"),
    ]

    operations = [
        migrations.AlterField(
            model_name="allowlistitem",
            name="item_type",
            field=models.CharField(
                choices=[
                    (artemisdb.artemisdb.consts.AllowListType["SECRET"], "secret"),
                    (artemisdb.artemisdb.consts.AllowListType["SECRET_RAW"], "secret_raw"),
                    (artemisdb.artemisdb.consts.AllowListType["VULN"], "vulnerability"),
                    (artemisdb.artemisdb.consts.AllowListType["VULN_RAW"], "vulnerability_raw"),
                    (artemisdb.artemisdb.consts.AllowListType["STATIC_ANALYSIS"], "static_analysis"),
                ],
                max_length=64,
            ),
        ),
    ]
