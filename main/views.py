from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Wheel, Lottery, LotteryResult
import datetime

def index(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'test.html')


def validate_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            lottery = Lottery.objects.get(code=code, is_active=True)
            return JsonResponse({'valid': True})
        except Lottery.DoesNotExist:
            return JsonResponse({'valid': False})

def validate_phone_no(request):
    if request.method == 'POST':
        phone_no = request.POST.get('phone_no')
        if len(phone_no) == 8:
            if phone_no.startswith(('6', '7', '8', '9')):
                return JsonResponse({'valid': True})
            else:
                return JsonResponse({'valid': False})
        else:
            return JsonResponse({'valid': False})


def list(request):
    lottery_list = LotteryResult.objects.all()
    return render(request, 'list.html', {"lottery_list":lottery_list})


def get_wheel_items(request):
    items = Wheel.objects.filter(is_active=True)
    data = []
    for item in items:
        if item.quantity > 0:
            calculated_chance = item.chance
        else:
            calculated_chance = 0.0
        data.append({
            'id': item.id,
            'title': item.title.upper(),
            'color': item.wheel_slice_color,
            'text_color': item.wheel_text_color,
            'chance': calculated_chance,
            'image_url': item.image.url
        })
    
    return JsonResponse({'wheel_items': data})

def save_result(request):
    if request.method == 'POST':
        register_no = request.POST.get('register_no')
        item_id = request.POST.get('item_id')
        code = request.POST.get('code')
        lottery = get_object_or_404(Lottery, code=code)
        wheel_item = get_object_or_404(Wheel, id=item_id)
        test = LotteryResult.objects.create(
            lottery=lottery,
            item=wheel_item,
            register_no=register_no
        )
        if code != 'test0000':
            lottery.is_active = False
            lottery.save()
            wheel_item.quantity -= 1
            wheel_item.save()
        return JsonResponse({'success': True, 'title':wheel_item.title, 'created_date': datetime.datetime.strftime( test.created_at, '%Y-%m-%d %H:%M:%S %p')})  
