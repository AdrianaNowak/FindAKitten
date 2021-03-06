"""FindAKitten URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from website.views import welcome, date, jakistrzeciprzyklad
from kotki.views import animals_list, new_animal, new_person ,new_image_view , detail , theanswerPies, display_animal_images, theanswerKot


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name="welcome"),
    path('date', date),
    path('temp', jakistrzeciprzyklad),
    path('person/<int:id>', detail, name="detail"),
    path('animals', animals_list, name="animals"),
    path('person/new_person', new_person, name="new_person"),
    path('person/new_animal', new_animal, name="new_animal"),
    path('image_upload', new_image_view, name='image_upload'),
    path('theanswerPies/<animal>/', theanswerPies, name='theanswerPies'),
    path('theanswerKot/<animal>/', theanswerKot, name='theanswerKot'),
    path('display_animal_images', display_animal_images, name='display_animal_images')

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
