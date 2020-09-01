# Generated by Django 3.0.9 on 2020-08-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_image', models.ImageField(upload_to='event_media/')),
                ('event_text', models.CharField(max_length=300)),
            ],
        ),
    ]
