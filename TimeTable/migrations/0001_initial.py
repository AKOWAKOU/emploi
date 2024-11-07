# Generated by Django 4.2.16 on 2024-11-07 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('capacity', models.IntegerField(null=True)),
                ('status', models.BooleanField(default=True)),
                ('description', models.TextField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255, null=True)),
                ('total_time', models.IntegerField()),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.level')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('week', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TimeTable.classroom')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.level')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TimeTable.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
