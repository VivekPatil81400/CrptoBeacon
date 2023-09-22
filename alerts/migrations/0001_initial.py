# Generated by Django 4.2.5 on 2023-09-21 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]