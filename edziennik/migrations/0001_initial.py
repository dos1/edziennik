# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('value', models.BooleanField(default=False)),
                ('justified', models.NullBooleanField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('weight', models.FloatField()),
                ('value', models.DecimalField(max_digits=1, choices=[(2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5)], decimal_places=1)),
                ('comment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=16)),
                ('creation_year', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='studentclass',
            name='teachers',
            field=models.ManyToManyField(to='edziennik.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studentclass',
            name='tutor',
            field=models.ForeignKey(related_name='pupil', to='edziennik.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='class_member',
            field=models.OneToOneField(to='edziennik.StudentClass'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='student_class',
            field=models.ForeignKey(to='edziennik.StudentClass'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='subject',
            field=models.ForeignKey(to='edziennik.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(to='edziennik.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grade',
            name='lesson',
            field=models.ForeignKey(to='edziennik.Lesson'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(to='edziennik.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendance',
            name='lesson',
            field=models.ForeignKey(to='edziennik.Lesson'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(to='edziennik.Student'),
            preserve_default=True,
        ),
    ]
