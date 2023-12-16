# Generated by Django 4.2.7 on 2023-12-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendationAiModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_file', models.FileField(default=None, max_length=1, upload_to='ai/recommendation')),
                ('model_name', models.CharField(default='knn', max_length=50)),
            ],
        ),
    ]
