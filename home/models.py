from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe


class HomeTitle(models.Model):
    title = models.TextField(max_length=300)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Home Title'
        verbose_name_plural = 'Home Title'


class Customers(models.Model):
    title = models.TextField(max_length=300)
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Hamkorlar'
        verbose_name_plural = 'Hamkorlar'


class Faq(models.Model):
    title = models.TextField('Savol', max_length=1000)
    description = models.TextField('Javob', max_length=2000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Faq bo`limi'
        verbose_name_plural = 'Faq bo`limi'


class Projects(models.Model):
    title = models.TextField(max_length=500)
    sub_title = models.TextField(max_length=500)
    slug = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    content = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Bizning Loyihalar'
        verbose_name_plural = 'Bizning Loyihalar'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))


class Contact(models.Model):
    first_name = models.CharField('Ism', max_length=300)
    last_name = models.CharField('Familiya', max_length=300)
    phone = models.CharField('Telefon', max_length=300)
    telegram = models.CharField('Telegram', max_length=600)
    message = models.TextField('Xabar', max_length=3000)
    ip = models.CharField('IP ADDRESS', max_length=100)
    create_time = models.TimeField('Xabar kelgan vaqt', auto_now=True)
    create_date = models.DateField('Xabar kelgan sana', auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Mijozlar bilan aloqa'
        verbose_name_plural = 'Mijozlar bilan aloqa'
