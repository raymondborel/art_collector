# Generated by Django 4.2.2 on 2023-07-13 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_artwork'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('artworks', models.ManyToManyField(to='main_app.artwork')),
            ],
        ),
    ]
