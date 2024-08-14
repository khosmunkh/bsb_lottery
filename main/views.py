from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Wheel, Lottery, LotteryResult

def index(request):
    return render(request, 'index.html')

def validate_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            lottery = Lottery.objects.get(code=code, is_active=True)
            return JsonResponse({'valid': True})
        except Lottery.DoesNotExist:
            return JsonResponse({'valid': False})

def validate_register_no(request):
    if request.method == 'POST':
        register_no = request.POST.get('register_no')
        if len(register_no) != 10:
            return JsonResponse({'valid': False})
        return JsonResponse({'valid': True})


def list(request):
    lottery_list = LotteryResult.objects.all()
    return render(request, 'list.html', {"lottery_list":lottery_list})


def get_wheel_items(request):
    wheel_items = Wheel.objects.filter(is_active=True, quantity__gt=0)
    data = [
        {'label': item.title, 'value': item.pk, 'image': item.image.url, 'chance': item.chance}
        for item in wheel_items
    ]
    response = {
        'has_items': bool(wheel_items),
        'items': data
    }
    return JsonResponse(response, safe=False)

def save_result(request):
    if request.method == 'POST':
        register_no = request.POST.get('register_no')
        item_id = request.POST.get('item_id')
        code = request.POST.get('code')
        lottery = get_object_or_404(Lottery, code=code)
        wheel_item = get_object_or_404(Wheel, id=item_id)
        
        LotteryResult.objects.create(
            lottery=lottery,
            item=wheel_item,
            register_no=register_no
        )
        if code != 'test0000':
            lottery.is_active = False
            lottery.save()
            wheel_item.quantity -= 1
            wheel_item.save()
        return JsonResponse({'success': True, 'title':wheel_item.title})
