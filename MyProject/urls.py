from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store.views import homepage  # استدعاء الصفحة الرئيسية من view

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ الصفحة الرئيسية تعرض home.html مباشرة
    path('', homepage, name='homepage'),

    # ✅ مسارات التطبيقات الفرعية
    path('store/', include('store.urls')),    # منتجات المتجر
    path('cart/', include('cart.urls')),      # السلة
    path('orders/', include('orders.urls')),  # الطلبات
]

# ✅ دعم تحميل صور المنتجات أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
