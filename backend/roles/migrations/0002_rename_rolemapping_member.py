# Generated by Django 3.2.8 on 2022-01-12 23:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0028_auto_20220111_0655'),
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RoleMapping',
            new_name='Member',
        ),
    ]
