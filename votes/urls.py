from django.urls import path 
from . import views 

urlpatterns = [
    path('token',views.index, name='index'),
    path('vote', views.vote, name='vote'),
    path('checktoken', views.check_token, name='checktoken'),
    path('submitvote', views.submit_vote, name='submitvote'),
    path('generatetoken', views.generate_token, name='generatetoken'),
    path('token_generate', views.generate_token_page, name='generatetokenpage')
]