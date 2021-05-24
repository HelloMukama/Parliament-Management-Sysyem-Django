# Generated by Django 3.2 on 2021-05-19 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactioninstance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reaction',
            name='comment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='comment.comment'),
        ),
        migrations.AddField(
            model_name='follower',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='flaginstance',
            name='flag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flags', to='comment.flag'),
        ),
        migrations.AddField(
            model_name='flaginstance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flags', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flag',
            name='comment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='comment.comment'),
        ),
        migrations.AddField(
            model_name='flag',
            name='moderator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flags_moderated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='reactioninstance',
            unique_together={('user', 'reaction')},
        ),
        migrations.AlterUniqueTogether(
            name='flaginstance',
            unique_together={('flag', 'user')},
        ),
    ]
