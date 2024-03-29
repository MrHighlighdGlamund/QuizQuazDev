# Generated by Django 5.0.1 on 2024-01-12 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateQuizApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizLibary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QuizID', models.IntegerField(default=0)),
                ('Quizmaster', models.CharField(max_length=12)),
                ('Question', models.CharField(max_length=200)),
                ('Answer1', models.CharField(max_length=50)),
                ('Answer2', models.CharField(max_length=50)),
                ('Answer3', models.CharField(max_length=50)),
                ('Answer4', models.CharField(max_length=50)),
                ('RightAnswerInt', models.IntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
    ]
