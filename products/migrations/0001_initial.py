# Generated by Django 5.0.6 on 2024-06-27 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('inventory', models.IntegerField()),
            ],
        ),
    ]
