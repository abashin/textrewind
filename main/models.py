from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    title = models.CharField("Название", max_length=100)
    author = models.CharField("Автор", max_length=100)
    percent = models.IntegerField("Процент прочитаного", default=0)
    book_image = models.ImageField("Изображение1", upload_to="itemimage/",  default='')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

# Create your models here.
