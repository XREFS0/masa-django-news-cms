"""
Developed by MASA
All Rights Reserved.
"""

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("newsApp", "0002_alter_category_status_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                default="", on_delete=django.db.models.deletion.CASCADE, to="newsApp.category"
            ),
        ),
    ]
