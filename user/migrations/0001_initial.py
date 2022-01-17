# Generated by Django 4.0.1 on 2022-01-17 02:42

import datetime
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(default=datetime.date.today, null=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('born_date', models.DateField()),
                ('address', models.CharField(max_length=30)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('institution', models.CharField(max_length=100)),
                ('study_field', models.CharField(max_length=100)),
                ('certifications', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=15), blank=True, null=True, size=5)),
                ('languages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=15), blank=True, null=True, size=3)),
                ('references', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=2), blank=True, null=True, size=5)),
                ('card_id', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(max_length=100)),
                ('cellphone', models.CharField(max_length=13)),
                ('friends', models.ManyToManyField(blank=True, to='user.Intern')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile_of_%(class)s', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(default=datetime.date.today, null=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('card_id', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(max_length=100)),
                ('cellphone', models.CharField(max_length=13)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile_of_%(class)s', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='intern',
            index=models.Index(fields=['card_id'], name='card index intern'),
        ),
        migrations.AddIndex(
            model_name='agent',
            index=models.Index(fields=['card_id'], name='card index agent'),
        ),
    ]