
from django.urls import path, re_path
from apps.course import views
urlpatterns = [

    # The home page
    path('', views.index, name='course_home'),
]
