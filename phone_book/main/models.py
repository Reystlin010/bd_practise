from django.db import models

class Users(models.Model):
    name = models.CharField('Имя пользователя', max_length=40)
    phone = models.CharField('Телефон', max_length=30)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return '/'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

# авторизация
# ограничения на ввод всякой фигни
# комментарии и тайпхинт в коде

