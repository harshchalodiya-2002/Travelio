from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.second,name='contact')

]
urlpatterns = urlpatterns +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




