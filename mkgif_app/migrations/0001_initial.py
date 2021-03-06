# Generated by Django 3.2.7 on 2021-09-14 13:37

from django.db import migrations, models
import django.db.models.deletion
import mkgif_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=mkgif_app.models.Image.image_path)),
                ('animation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mkgif_app.animation')),
            ],
        ),
    ]
