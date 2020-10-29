from django.urls import path,re_path
from .views import Home,search_results,profile,edit_profile,upload_image,comment,like,is_liked,follow_unfollow

urlpatterns = [
    path('', Home, name = 'index'),
    path('search/', search_results, name = 'search_results'),
    path('user/(<username>\w+)', profile, name='profile'),
    path('accounts/edit/', edit_profile, name='edit_profile'),
    path('upload/', upload_image, name='upload_image'),
    path('comment/(<image_id>\d+)', comment, name='comment'),
    path('like/(<image_id>\d+)', like, name='like'),
    path('is_liked/', is_liked, name = 'is_liked'),
    path('switch_follow/',follow_unfollow, name='follow-unfollow-view'),
]