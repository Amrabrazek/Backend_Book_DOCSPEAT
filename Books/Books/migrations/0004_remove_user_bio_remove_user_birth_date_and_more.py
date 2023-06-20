# Generated by Django 4.2.2 on 2023-06-20 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_user_book_summary_alter_book_publication_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='user',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='title',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
        migrations.AddField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, null=True, upload_to='book_images/'),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Books.user')),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
                ('bio', models.TextField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
            ],
            bases=('Books.user',),
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Books.user')),
                ('reading_list', models.ManyToManyField(blank=True, related_name='readers', to='Books.book')),
            ],
            bases=('Books.user',),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='Books.author'),
        ),
    ]
