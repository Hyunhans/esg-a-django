from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index),   #(1 , 2)  1번 주소가 오면 2번 처리를 하겠다. 
    path('<int:pk>/', views.single_post_page), # 숫자의 의미로 <int>를 써줌 :pk pk라는 이름으로 넘기겠다.  
]

#모든  path 의 blog 를 지워주고 프로젝트 url 에 가서 path 에 blog/를 투자해줌 