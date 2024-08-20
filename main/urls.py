from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('test/', views.test, name='test'),
    path('validate_code/', views.validate_code, name='validate_code'),
    path('validate_phone_no/', views.validate_phone_no, name='validate_phone_no'),
    path('get_wheel_items/', views.get_wheel_items, name='get_wheel_items'),  # Added for dynamic wheel data
    path('save_result/', views.save_result, name='save_result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
