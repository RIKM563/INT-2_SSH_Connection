from django.db import models


class Information(models.Model):
    os = models.CharField('Название ОС', max_length=100)
    info = models.TextField('Информация')

    def __str__(self):
        return self.os


class Input(models.Model):
    hostname = models.CharField('ip', max_length=50)
    username = models.CharField('имя', max_length=50)
    password = models.CharField('пароль', max_length=50)
    port = models.CharField('порт', max_length=50)

    def __str__(self):
        return self.hostname
