# Generated by Django 2.2 on 2019-05-01 18:10

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fullname', models.CharField(max_length=50)),
                ('followings', models.ManyToManyField(related_name='followers', to='instagmar_app.MyUser')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('content', models.ImageField(upload_to='instagmar_app')),
                ('caption', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagmar_app.MyUser')),
            ],
        ),
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagmar_app.Chat')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagmar_app.MyUser')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('related_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagmar_app.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagmar_app.MyUser')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('related_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagmar_app.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagmar_app.MyUser')),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagmar_app.MyUser'),
        ),
    ]
