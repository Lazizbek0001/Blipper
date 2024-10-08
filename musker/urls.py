from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("profile_list/", views.profile_list, name='profile-list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('profile/followers/<int:pk>', views.followers, name='followers'),
    
    path('profile/follows/<int:pk>', views.follows, name='follows'),
    
    path("login/", views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('meep_like/<int:pk>', views.meep_like, name= 'meep_like'),
    path('meep_show/<int:pk>', views.meep_show, name= 'meep_show'),
    path('unfollow/<int:pk>', views.unfollow, name= 'unfollow'),
    path('follow/<int:pk>', views.follow, name= 'follow'),
    path('delete_meep/<int:pk>', views.delete_meep, name= 'delete_meep'),
    path('edit_meep/<int:pk>', views.edit_meep, name= 'edit_meep'),
    path('search/', views.search, name= 'search'),
    path('bookmarks/', views.bookmark, name='bookmark'),
    path('search_user/', views.search_user, name= 'search_user'),
    path('post_comment/<int:meep_id>/', views.post_comment, name='post_comment'),
    path('delete_comment/<int:pk>/', views.delete_comment, name='delete_comment'),
    path('comment_like/<int:pk>', views.comment_like, name= 'comment_like'),
    path('meep_mark/<int:pk>', views.meep_bookmark, name= 'meep_book'),
    path('notifications/', views.notification, name='notification'),
]