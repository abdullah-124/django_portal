# Generated by Django 5.0.1 on 2024-03-14 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0023_alter_review_comment_alter_review_rating'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set(),
        ),
    ]
