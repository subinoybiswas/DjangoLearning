# Generated by Django 4.1.5 on 2023-02-13 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titile', models.CharField(max_length=256)),
                ('text', models.TextField()),
                ('dete', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
