# Generated by Django 4.2.4 on 2023-08-23 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_merge_0003_comment_0003_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main_app.plant'),
        ),
    ]
