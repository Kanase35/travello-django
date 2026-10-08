
#from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings 
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     #path('', include("calc.urls")),
#     path('', include('travello.urls')),
#     path('accounts/', include('accounts.urls')),
    
# ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include, re_path  # ✅ Added re_path here
from django.conf import settings
from django.views.static import serve           # ✅ Added serve import here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('travello.urls')),
    path('accounts/', include('accounts.urls')),
    
    # ✅ FIX: This forces Render to serve your uploaded media images even when DEBUG is False
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]


