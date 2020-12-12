# Generated by Django 3.1.2 on 2020-12-12 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_endofday_highlow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endofday',
            old_name='highLow',
            new_name='high',
        ),
        migrations.AddField(
            model_name='endofday',
            name='low',
            field=models.CharField(max_length=30, null=True),
        ),
    ]