# Generated by Django 4.1.5 on 2023-01-18 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vueBackend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotask',
            name='taskId',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]