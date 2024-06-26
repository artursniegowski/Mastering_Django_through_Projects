# Generated by Django 4.2.5 on 2023-10-18 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_catalog', '0005_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': [('can_mark_returned', 'Can Set book as returned'), ('can_renew', 'Can extend the book return date'), ('can_view_staff', 'Can see the staff view')]},
        ),
    ]
