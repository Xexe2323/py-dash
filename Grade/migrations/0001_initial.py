# Generated by Django 3.2.15 on 2023-01-20 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(default='', max_length=255)),
                ('score', models.CharField(default='1-100', max_length=10)),
                ('exam', models.CharField(max_length=50)),
                ('passed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50)),
                ('onclass', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4')], max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('paid', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=26)),
                ('presents', models.CharField(max_length=100)),
                ('absents', models.CharField(max_length=100)),
                ('term', models.CharField(max_length=100)),
                ('learning', models.CharField(choices=[('GER', 'German'), ('EN', 'English'), ('FR', 'French'), ('IR', 'Persian')], max_length=26)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
