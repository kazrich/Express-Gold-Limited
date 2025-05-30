from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.product, name='product'),  # ✅ Product page
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)