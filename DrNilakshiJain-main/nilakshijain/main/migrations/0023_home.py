# Generated by Django 4.2.1 on 2023-06-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_remove_book_contact_me'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('title1', models.CharField(max_length=255, null=True)),
                ('title1_1', models.CharField(max_length=255, null=True)),
                ('title1_2', models.CharField(max_length=255, null=True)),
                ('title1_3', models.CharField(max_length=255, null=True)),
                ('title1_4', models.CharField(max_length=255, null=True)),
                ('title1_5', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('more', models.CharField(max_length=255, null=True)),
                ('more_link', models.URLField(max_length=100, null=True)),
            ],
        ),
    ]