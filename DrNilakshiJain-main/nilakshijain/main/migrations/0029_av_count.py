# Generated by Django 4.2.1 on 2023-06-10 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_av_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='av',
            name='count',
            field=models.CharField(max_length=255, null=True),
        ),
    ]