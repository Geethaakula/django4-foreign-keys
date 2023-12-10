# Generated by Django 3.2.13 on 2023-12-09 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_project', '0007_auto_20231209_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=32),
        ),
        migrations.CreateModel(
            name='Gifts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gift', models.CharField(max_length=32)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_project.user')),
            ],
        ),
    ]