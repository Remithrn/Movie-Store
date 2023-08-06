from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path
app_name='movieapp'
urlpatterns = [
    path('',views.index,name='index'),
    path("movie/<int:movie_id>",views.detail,name='detail'),
    path('add/',views.add,name='add'),
    path('update/<int:id>',views.update,name='update'),
    path('remove/<int:id>',views.remove,name='remove')
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
