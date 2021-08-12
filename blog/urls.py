from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include

from posts.views import index, blog, post, search, post_update,post_delete , post_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name= 'post-list'),
    path('search/', search, name= 'search'),
    path('post/<id>/', post, name = 'post-detail'),
    path('post/<id>/update', post_update, name = 'post_update'),
    path('post/<id>/delete', post_delete, name = 'post_delete'),
    path('create/', post_create, name = 'post_create'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls'))
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
   # urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)