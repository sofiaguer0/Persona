# Generated by Django 4.2.4 on 2023-10-24 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_persona_legajo'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=250)),
                ('mensaje', models.TextField(max_length=300)),
            ],
        ),
    ]
