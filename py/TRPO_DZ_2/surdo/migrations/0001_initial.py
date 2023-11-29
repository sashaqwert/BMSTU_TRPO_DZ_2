# Generated by Django 4.2.7 on 2023-11-29 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=255, verbose_name='Имя пользователя')),
                ('first_name', models.CharField(default='', max_length=255, verbose_name='Имя')),
                ('middle_name', models.CharField(default='', max_length=255, verbose_name='Отчество')),
                ('last_name', models.CharField(default='', max_length=255, verbose_name='Фамилия')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id_task', models.AutoField(primary_key=True, serialize=False)),
                ('task_title', models.CharField(default='', max_length=255, verbose_name='Название задания')),
                ('task_text', models.CharField(default='', max_length=255, verbose_name='Текст задания')),
                ('task_author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='surdo.appuser', verbose_name='Автор задания')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id_answer', models.AutoField(primary_key=True, serialize=False)),
                ('answer_text', models.CharField(default='', max_length=255, verbose_name='Текст ответа')),
                ('answer_mark', models.IntegerField(default=0, verbose_name='Оценка')),
                ('answer_author', models.ForeignKey(default=1, max_length=255, on_delete=django.db.models.deletion.CASCADE, to='surdo.appuser', verbose_name='Автор ответа')),
                ('answer_task', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='surdo.task', verbose_name='Задание')),
            ],
        ),
    ]