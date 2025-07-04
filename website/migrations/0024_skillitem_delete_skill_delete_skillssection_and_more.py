# Generated by Django 5.2.3 on 2025-06-20 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_alter_projectitem_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.PositiveIntegerField(help_text='Enter a value between 0 and 100')),
                ('order', models.PositiveIntegerField(default=0)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_items', to='website.section')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.DeleteModel(
            name='SkillsSection',
        ),
        migrations.AlterField(
            model_name='projectitem',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
