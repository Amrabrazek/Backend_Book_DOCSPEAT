# Generated by Django 4.2.2 on 2023-07-01 19:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0006_alter_book_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='reader_books',
            unique_together={('id', 'reader', 'book')},
        ),
    ]
