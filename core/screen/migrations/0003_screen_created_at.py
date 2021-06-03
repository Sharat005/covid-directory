# Generated by Django 3.2.3 on 2021-06-02 03:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0002_remove_screen_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='screen',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created At'),
            preserve_default=False,
        ),
    ]