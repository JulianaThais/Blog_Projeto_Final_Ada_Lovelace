# Generated by Django 5.0.3 on 2024-04-10 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_blogpost_id_alter_comment_id_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]