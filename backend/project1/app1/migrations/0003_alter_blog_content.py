# Generated by Django 5.0 on 2023-12-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_blog_delete_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(max_length=900),
        ),
    ]
