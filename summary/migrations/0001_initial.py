# Generated by Django 5.0.7 on 2024-07-30 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('summary_id', models.AutoField(primary_key=True, serialize=False)),
                ('origin_text_path', models.URLField()),
                ('summary_text_path', models.URLField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]