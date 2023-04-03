# Generated by Django 3.1.1 on 2023-02-18 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cetus', '0007_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Subject', models.CharField(max_length=500)),
                ('Message', models.CharField(max_length=500)),
            ],
        ),
    ]
