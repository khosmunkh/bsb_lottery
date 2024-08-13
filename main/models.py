from django.db import models

# Create your models here.


class Wheel(models.Model):
    image = models.ImageField(upload_to='wheel/')
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Хүрд'
        verbose_name_plural = 'Хүрд'


class Lottery(models.Model):
    code = models.CharField(max_length=20, verbose_name='Сугалааны код')
    description = models.CharField(max_length=200, null=True, blank=True, verbose_name='Тайлбар')
    is_active = models.BooleanField(default=True, verbose_name='Идэвхтэй эсэх')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Үүссэн огноо')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Шинэчилсэн/Зассан огноо')
    
    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name = 'Сугалаа'
        verbose_name_plural = 'Сугалаа'


class LotteryResult(models.Model):
    lottery = models.ForeignKey(Lottery, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Wheel, on_delete=models.DO_NOTHING)
    register_no = models.CharField(max_length=100, verbose_name='Худалдан авагчийн регистрийн дугаар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Үүссэн огноо')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Шинэчилсэн/Зассан огноо')

    def __str__(self):
        return self.register_no

    class Meta:
        verbose_name = 'Сугалааны хариу'
        verbose_name_plural = 'Сугалааны хариу'