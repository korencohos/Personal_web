# Generated by Django 5.2.3 on 2025-06-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_contactmessage_submitted_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='level',
            field=models.PositiveIntegerField(default=100, help_text='Enter a value between 0 and 100'),
            preserve_default=False,
        ),
    ]
