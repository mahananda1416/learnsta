# Generated by Django 5.0.6 on 2024-07-05 17:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0005_remove_profile_id_user_profile_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AddField(
            model_name='profile',
            name='id_user',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='blank-profile-picture.png', upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]