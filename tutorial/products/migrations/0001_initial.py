# Generated by Django 4.0.9 on 2023-02-18 08:43

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
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cover', models.ImageField(blank=True, null=True, upload_to='product_covers/')),
                ('content_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
