# Generated by Django 4.1.1 on 2022-09-25 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_code', models.CharField(max_length=8, verbose_name='id_code')),
                ('name', models.CharField(max_length=80, null=True, verbose_name='name')),
            ],
        ),
    ]