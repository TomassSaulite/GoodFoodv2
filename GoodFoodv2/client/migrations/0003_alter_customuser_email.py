# Generated by Django 5.0.6 on 2024-06-26 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_customuser_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
