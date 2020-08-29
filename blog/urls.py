from django.urls import path
from blog import views
app_name="BLOG"
urlpatterns = [
    path('',views.blog , name="bloghome") ,
    path('<int:blog_id>/',views.spblog,name="spblog")
]