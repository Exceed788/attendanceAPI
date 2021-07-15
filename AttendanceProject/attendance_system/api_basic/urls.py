
from django.urls import path

from .views import EventDetail, EventList, StudentDetail, StudentList


urlpatterns = [
    
    path('students/', StudentList.as_view()),
    path('students/<int:id>', StudentDetail.as_view()),
    path('events/', EventList.as_view()),
    path('events/<int:id>', EventDetail.as_view())
  
    
] 
