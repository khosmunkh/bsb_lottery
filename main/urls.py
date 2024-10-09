from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('of/', views.office_wheel, name='of'),
    path('hf/', views.geriin_wheel, name='hf'),
    path('ons/', views.country_wheel, name='ons'),
    path('validate_code/', views.validate_code, name='validate_code'),
    path('validate_phone_no/', views.validate_phone_no, name='validate_phone_no'),
    path('validate_both/', views.validate_both, name='validate_both'),
    path('get_wheel_items/<int:id>', views.get_wheel_items, name='get_wheel_items'),
    path('save_result/', views.save_result, name='save_result'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
