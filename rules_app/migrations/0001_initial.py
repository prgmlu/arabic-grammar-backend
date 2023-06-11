# Generated by Django 4.1.7 on 2023-06-11 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('rule', models.TextField()),
                ('highlightColor', models.CharField(max_length=7)),
                ('sound', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.TextField()),
                ('highlightedIndices', models.CharField(max_length=200)),
                ('rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules_app.rule')),
            ],
        ),
    ]