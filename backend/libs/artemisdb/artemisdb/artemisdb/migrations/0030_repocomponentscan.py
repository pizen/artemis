# Generated by Django 3.2.10 on 2022-01-06 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artemisdb", "0029_scanschedule_time_of_day"),
    ]

    operations = [
        migrations.CreateModel(
            name="RepoComponentScan",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "component",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="artemisdb.component"),
                ),
                ("repo", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="artemisdb.repo")),
                ("scan", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="artemisdb.scan")),
            ],
            options={
                "unique_together": {("repo", "component")},
            },
        ),
        migrations.RunSQL(
            sql="""
INSERT INTO artemisdb_repocomponentscan(component_id, scan_id, repo_id)
SELECT DISTINCT ON (s.repo_id, d.component_id) d.component_id, d.scan_id, s.repo_id FROM artemisdb_dependency AS d
JOIN artemisdb_scan AS s ON d.scan_id = s.id ORDER BY s.repo_id, d.component_id, d.scan_id DESC;
""",
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
