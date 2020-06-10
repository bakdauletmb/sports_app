# Generated by Django 3.0.7 on 2020-06-08 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('definition', models.CharField(max_length=400)),
                ('image', models.FileField(upload_to='')),
                ('author', models.CharField(choices=[('Robert Pitt', 'Robert Pitt'), ('Sam Venom', 'Sam Venom'), ('Daniel John', 'Daniel John')], max_length=20)),
                ('realized', models.TextField()),
            ],
        ),
    ]