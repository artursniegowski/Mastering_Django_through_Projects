# Generated by Django 4.1.6 on 2023-06-05 13:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('booking_amount_money', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(50)])),
                ('reactivate_request_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['booking_date'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('intro', models.CharField(blank=True, max_length=200, null=True)),
                ('online_from', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=2000)),
                ('calculate', models.BooleanField(default=False)),
                ('textbox_inner_ticket_desc', models.TextField(blank=True, max_length=2000)),
                ('project_money_total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'ordering': ['online_from'],
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expiration_hours', models.PositiveSmallIntegerField(default=24)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='token', to='app_funding.booking')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following_since', models.DateTimeField(auto_now_add=True)),
                ('book_request_date', models.DateTimeField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='app_funding.project')),
            ],
            options={
                'ordering': ['following_since'],
            },
        ),
    ]
