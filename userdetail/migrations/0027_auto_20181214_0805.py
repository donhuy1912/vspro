# Generated by Django 2.1.3 on 2018-12-14 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetail', '0026_auto_20181212_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='avatar',
            field=models.CharField(blank=True, db_column='Avatar', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='forum',
            name='avatar',
            field=models.CharField(blank=True, db_column='Avatar', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='projectshare',
            name='avatar',
            field=models.CharField(blank=True, db_column='Avatar', max_length=100, null=True),
        ),
    ]
