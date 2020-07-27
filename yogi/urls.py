from django.urls import path
from yogi import views

app_name="yogi"#is used to creatq a namespace
urlpatterns = [
    #path("secondary suffix",address of function, name of mapping)
    path('',views.index,name='index'),
    path('home',views.home,name="home"),
    path('fact/<n>',views.fact,name="fact"),
    path('child/',views.child,name="child"),
]