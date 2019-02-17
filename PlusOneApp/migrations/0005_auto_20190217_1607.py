# Generated by Django 2.1.3 on 2019-02-17 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlusOneApp', '0004_activity_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='currentCount',
        ),
        migrations.AddField(
            model_name='group',
            name='location',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='reccuring',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='group',
            name='timeCreated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='timeOccuring',
            field=models.DateTimeField(null=True),
        ),
    ]