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
        #TODO: Register no hud urttai baival shalgah
        return JsonResponse({'valid': True})

def get_wheel_items(request):
    wheel_items = Wheel.objects.filter(is_active=True)
    data = [
        {'label': item.title, 'value': item.pk, 'image': item.image.url}
        for item in wheel_items
    ]
    return JsonResponse(data, safe=False)

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
        return JsonResponse({'success': True, 'title':wheel_item.title})
