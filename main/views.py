from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Wheel, Lottery, LotteryResult
from django.views.decorators.csrf import csrf_exempt

import datetime

@csrf_exempt
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def wheel(request):
    return render(request, 'wheel.html')


@csrf_exempt
def validate_both(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        phone_no = request.POST.get('phone_no')

        lottery = Lottery.objects.filter(code=code, is_active = True)
        if not lottery:
            return JsonResponse({
                'valid': False,
                'code': code,
                'phone_no': phone_no,
                'msg': 'Сугалааны код буруу эсвэл ашиглагдсан байна.',
            })

        if not phone_no or len(phone_no) != 8 or not phone_no.startswith(('6', '7', '8', '9')):
            return JsonResponse({
                'valid': False,
                'code': code,
                'phone_no': phone_no,
                'msg': 'Таны утасны дугаар буруу байна.',
            })

        return JsonResponse({
            'valid': True,
            'code': code,
            'phone_no': phone_no,
            'msg': 'Ok',
        })


@csrf_exempt
def validate_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            lottery = Lottery.objects.get(code=code, is_active=True)
            return JsonResponse({'valid': True})
        except Lottery.DoesNotExist:
            return JsonResponse({'valid': False})


@csrf_exempt
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


@csrf_exempt
def list(request):
    lottery_list = LotteryResult.objects.all()
    return render(request, 'list.html', {"lottery_list":lottery_list})


@csrf_exempt
def get_wheel_items(request):
    items = Wheel.objects.all().order_by('pk')
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


@csrf_exempt
def save_result(request):
    if request.method == 'POST':
        phone_no = request.POST.get('phone_no')
        item_id = request.POST.get('item_id')
        code = request.POST.get('code').upper()
        lottery = Lottery.objects.filter(code=code, is_active = True).first()
        wheel_item = get_object_or_404(Wheel, id=item_id)

        if not lottery:
            return JsonResponse({
                'success': False,
                'msg': 'Ашиглагдсан код байна',
            })

        test = LotteryResult.objects.create(
            lottery=lottery,
            item=wheel_item,
            phone_no=phone_no
        )
        test_codes = ['TST11000', 'TST12000', 'TST13000', 'TST14000', 'TST15000', 'TST16000', 'TST17000' ,'TST18000' ,'TST19000']

        if code not in test_codes:
            lottery.is_active = False
            lottery.save()
            wheel_item.quantity -= 1
            wheel_item.save()
        return JsonResponse({'success': True, 'title':wheel_item.title,'is_active':wheel_item.is_active, 'created_date': datetime.datetime.strftime( test.created_at, '%Y-%m-%d %H:%M:%S %p')})   
