# Generated by Django 5.0.2 on 2024-02-21 19:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studying_now', '0002_alter_studyingnowmodel_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyingnowmodel',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]