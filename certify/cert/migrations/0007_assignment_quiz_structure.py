# Generated by Django 2.2 on 2019-04-11 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cert', '0006_assignedquestion_quizstructure'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='quiz_structure',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='cert.QuizStructure'),
            preserve_default=False,
        ),
    ]
