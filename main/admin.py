from django.contrib import admin
from main.models import Lottery
from main.models import LotteryResult
from main.models import Wheel

# Register your models here.

admin.site.register(Lottery)
admin.site.register(Wheel)
