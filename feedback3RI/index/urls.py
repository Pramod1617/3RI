from django.contrib import admin
from django.urls import path,include
from .views import index,about,contact,signup,signin,feedback,course,python,blockchain,datascience,selenium,signout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('about/',about,name="about"),
    path('contact/',contact,name="contact"),
    path('signup/',signup,name="signup"),
    path('signin/',signin,name="signin"),
    path('feedback/',feedback,name="feedback"),
    path('course/',course,name="course"),
    path('python/',python,name="python"),
    path('datascience/',datascience,name="datascience"),
    path('selenium/',selenium,name="selenium"),
    path('blockchain/',blockchain,name="blockchain"),
    path('signout/',signout,name="signout")

]