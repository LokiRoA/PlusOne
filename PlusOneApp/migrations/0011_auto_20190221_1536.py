# Generated by Django 2.1.3 on 2019-02-21 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlusOneApp', '0010_auto_20190221_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profilePic',
            field=models.ImageField(blank=True, default='images/default_profile_icon.jpg', upload_to=None),
        ),
    ]
