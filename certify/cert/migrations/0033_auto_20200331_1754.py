# Generated by Django 2.2 on 2020-03-31 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cert', '0032_email_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='html',
            field=models.TextField(default='\n    <html>\n    <body><p>\n    Здравствуйте, {{assignment.person.first_name}}!<br>\n    {{assignment.quiz_structure.name}}<br>\n    {{assignment.quiz_structure.minutes}}<br>\n<br>\n    {{assignment.quiz_structure.quantity()}}<br>\n    Логин: {{assignment.person.user.username}}<br>\n    Пароль: {{assignment.person.password}}<br>\n    </p>\n    </body>\n    </hmtl>\n        ', max_length=10000),
        ),
        migrations.AlterField(
            model_name='email',
            name='text',
            field=models.TextField(default='\nЗдравствуйте, {{assignment.person.first_name}}! /n\n{{assignment.quiz_structure.name}}/n\n{{assignment.quiz_structure.minutes}}/n\n/n\n{{assignment.quiz_structure.quantity()}}/n\nЛогин: {{assignment.person.user.username}}/n\nПароль: {{assignment.person.password}}/n\n    ', max_length=10000),
        ),
    ]
