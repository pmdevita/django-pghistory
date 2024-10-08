# Generated by Django 4.2.6 on 2024-09-24 17:46

import pgtrigger.compiler
import pgtrigger.migrations
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tests", "0013_concreteparent_concretechild_concretechildevent_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomAutoFieldModel",
            fields=[
                (
                    "id",
                    models.AutoField(db_column="pk_id", primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomBigAutoFieldModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(db_column="pk_id", primary_key=True, serialize=False),
                ),
            ],
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="ignoreautofieldssnapshotmodel",
            name="update_update",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="ignoreautofieldssnapshotmodel",
            name="delete_delete",
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="ignoreautofieldssnapshotmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="update_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition='WHEN (OLD."my_char_field" IS DISTINCT FROM (NEW."my_char_field") OR OLD."my_int_field" IS DISTINCT FROM (NEW."my_int_field"))',  # noqa: E501
                    func='INSERT INTO "tests_ignoreautofieldssnapshotmodelcreatedatupdatedatmychardc6b" ("created_at", "my_char_field", "my_int_field", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "updated_at") VALUES (OLD."created_at", OLD."my_char_field", OLD."my_int_field", _pgh_attach_context(), NOW(), \'update\', OLD."id", OLD."updated_at"); RETURN NULL;',  # noqa: E501
                    hash="e817c95f191e0d10b3e86643e2d8a050a864d45a",
                    operation="UPDATE",
                    pgid="pgtrigger_update_update_9dd1b",
                    table="tests_ignoreautofieldssnapshotmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="ignoreautofieldssnapshotmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="delete_delete",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "tests_ignoreautofieldssnapshotmodelcreatedatupdatedatmychardc6b" ("created_at", "my_char_field", "my_int_field", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "updated_at") VALUES (OLD."created_at", OLD."my_char_field", OLD."my_int_field", _pgh_attach_context(), NOW(), \'delete\', OLD."id", OLD."updated_at"); RETURN NULL;',  # noqa: E501
                    hash="c112d8f78e576e8fc9a895c72a92567c20b093a4",
                    operation="DELETE",
                    pgid="pgtrigger_delete_delete_42ea6",
                    table="tests_ignoreautofieldssnapshotmodel",
                    when="AFTER",
                ),
            ),
        ),
    ]
