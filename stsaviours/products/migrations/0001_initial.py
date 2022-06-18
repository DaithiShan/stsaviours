# Generated by Django 4.0.5 on 2022-06-18 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('ordering', models.IntegerField(default=0)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('stock', models.IntegerField(default=15)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='products/thumbnails/')),
            ],
            options={
                'ordering': ('ordering', 'title'),
            },
        ),
    ]
