from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
     path('', views.PointList.as_view(), name='point'),
     path('news/', views.NewsList.as_view(), name='news'),
     path('ask/', views.AskList.as_view(), name='ask'),
     path('show/', views.ShowList.as_view(), name='show'),

     path('comments/', views.CommentsList.as_view(), name='comments'),
     path('<str:username>/comments/', views.UserCommentsList.as_view(), name='usercomments'),

     path('create/', views.PostCreate.as_view(), name='create'),
     path('<int:post_id>/', views.PostDetail.as_view(), name='detail'),
     path('<int:post_id>/comments/', views.PostCommentsList.as_view(), name='postcomments'),

     path('<int:post_id>/comments/create/',
          views.CommentCreate.as_view(), name='comment_create'),
     path('<int:post_id>/comments/<int:comment_id>/',
          views.CommentUpdate.as_view(), name='comment_update'),


     path('comments/<int:comment_id>/replies/create/',
          views.ReplyCreateAPIView.as_view(), name='reply-create'),
     path('comments/<int:comment_id>/replies/<int:reply_id>/', 
          views.ReplyUpdateAPIView.as_view(), name='reply_update'),

     path('comments/<int:comment_id>/replies/',
          views.ReplyListAPIView.as_view(), name='reply-list'),
]
