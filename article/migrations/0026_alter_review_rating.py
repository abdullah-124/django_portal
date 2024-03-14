# Generated by Django 5.0.1 on 2024-03-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0025_alter_review_user_alter_review_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.DecimalField(choices=[('1.0', '★☆☆☆☆ (1/5)'), ('2.0', '★★☆☆☆ (2/5)'), ('3.0', '★★★☆☆ (3/5)'), ('4.0', '★★★★☆ (4/5)'), ('5.0', '★★★★★ (5/5)')], decimal_places=1, max_digits=2),
        ),
    ]
