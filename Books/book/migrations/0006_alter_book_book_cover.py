# Generated by Django 4.2.2 on 2023-07-01 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_book_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(default='book_images/defaultBC.jpg', upload_to='book_images/'),
        ),
    ]
