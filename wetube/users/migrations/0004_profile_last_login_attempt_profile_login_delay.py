# Generated by Django 4.2.7 on 2023-12-10 17:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_remove_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="last_login_attempt",
            field=models.DateTimeField(
                blank=True, default=django.utils.timezone.now, null=True
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="login_delay",
            field=models.IntegerField(
                default=0,
                help_text="Seconds that the user has been delayed for next login",
            ),
        ),
    ]