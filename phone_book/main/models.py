from django.db import models

class Users(models.Model):
    name = models.CharField('Имя пользователя', max_length=40)
    phone = models.CharField('Телефон', max_length=30)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
