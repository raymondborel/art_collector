# Generated by Django 4.2.2 on 2023-07-12 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.CharField(max_length=300)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='main_app.artist')),
            ],
        ),
    ]