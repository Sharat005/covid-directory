# Generated by Django 3.2.3 on 2021-06-02 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0002_alter_screen_screen_smoking_yn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='screen_smoking_yn',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], null=True, verbose_name='Are you a current or former smoker?'),
        ),
    ]