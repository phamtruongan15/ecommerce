from django.urls import path
from ecommerceapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name="index"),
    path('contact/', views.contact,name="contact"),
    path('About/', views.About,name="About"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
