# Generated by Django 4.0.4 on 2022-05-14 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('migrations', '0003_alter_fileupload_content_alter_fileupload_imgfile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='imgfile',
            field=models.ImageField(null=True, upload_to='media/%Y/%m/%d'),
        ),
    ]