from django.db import models

# Create your models here.

BRANCH_CHOICES = [
    (0,'--------'),
    (1,'Гэрийн мебель'),
    (2,'Оффис мебель'),
    (3,'Орон нутаг'),
]

from datetime import datetime
class Wheel(models.Model):
    image = models.ImageField(upload_to='wheel/', verbose_name="Барааны зураг")
    wheel_slice_color =  models.CharField(max_length=20, default='#ffffff', verbose_name="Хүрдний хэрчмийн өнгө")
    wheel_text_color =  models.CharField(max_length=20, default='#000000', verbose_name="Хүрдний хэрчмийн текст өнгө")
    title = models.CharField(max_length=100, verbose_name="Барааны нэр")
    chance = models.FloatField(default=1.0, help_text="Зөвхөн тоон утга хийх | % тэмдэг бичиж болохгүй", verbose_name="Таарах магадлал")
    is_prize = models.BooleanField(default=True, verbose_name="Шагналтай хүрд эсэх")
    quantity = models.IntegerField(default=0, verbose_name="Үлдэгдэл")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    branch = models.IntegerField(choices=BRANCH_CHOICES, default=0)

    def __str__(self):
        return self.title + " " + str(self.quantity) + " ш ~ " + self.get_branch_display()

    class Meta:
        verbose_name = 'Хүрдний хэрчим'
        verbose_name_plural = 'Хүрдний хэрчим'


class Lottery(models.Model):
    code = models.CharField(max_length=20, verbose_name='Сугалааны код')
    description = models.CharField(max_length=200, null=True, blank=True, verbose_name='Тайлбар')
    is_active = models.BooleanField(default=True, verbose_name='Идэвхтэй эсэх')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Үүссэн огноо')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Шинэчилсэн/Зассан огноо')
    
    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name = 'Код'
        verbose_name_plural = 'Код'


class LotteryResult(models.Model):
    lottery = models.ForeignKey(Lottery, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Wheel, on_delete=models.DO_NOTHING)
    phone_no = models.CharField(max_length=100, verbose_name='Худалдан авагчийн утасны дугаар')
    created_at = models.DateTimeField(verbose_name='Үүссэн огноо')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Шинэчилсэн/Зассан огноо')

    def __str__(self):
        return self.phone_no

    class Meta:
        verbose_name = 'Сугалааны хариу'
        verbose_name_plural = 'Сугалааны хариу'