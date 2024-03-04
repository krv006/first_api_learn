# Generated by Django 5.0.1 on 2024-03-04 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_book_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.publisher'),
        ),
    ]
