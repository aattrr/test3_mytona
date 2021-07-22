# Generated by Django 3.2.5 on 2021-07-15 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='first name')),
                ('second_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='second name')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='library.Author'),
        ),
    ]