
from django.urls import path
from . import views

app_name='vote'
urlpatterns = [
    path('', views.logins,name='logins'),
    path('<int:question_id>/votes/', views.votes,name='votes' ),
    path('dashbord/',views.election,name='index' ),
    path('<int:question_id>/',views.detail,name='detail' ),
    path('<int:question_id>/results/',views.display,name='display' ),
    path('register/student', views.register),
    path('profile', views.profile),
    path('pop', views.pop, name='pop'),
    path('logout', views.logout, name='logout'),
    # path('', views.index, name='index'),
    # path('test/', views.test,name='text' ),
    # path('image/', views.image_upload, name = "image-request")

   
   
]
#<int:question_id> will look through to see the id number of the question and add it to the url

