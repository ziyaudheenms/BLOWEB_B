from django.urls import path
from . import views
urlpatterns = [
    path('' ,views.Show ),
    path('view/<int:pk>/' ,views.singlePage ),
    path('view/suggestion/' ,views.MoreSuggestions ),
    path('view/myProject/' ,views.MyProjects ),
    path('category/' ,views.ShowCategory ),
    path('search/' ,views.SearchFilter ),
    path('profile/' ,views.UserProfile ),
    path('profile/all/' ,views.AllProfiles ),
    path('profile/<int:pk>/' ,views.RequestedProfile ),
    path('profile/build/' ,views.BuildProfile ),
    path('profile/buildProfile/' ,views.BuildProfileUser ),
    path('blog/create/' ,views.BuildBlog ),
    path('delete/<int:pk>/' ,views.DeleteBlog ),
    path('Like/<int:pk>/' ,views.BlogLikeUpdate ),
    path('Update/<int:pk>/' ,views.BlogPostUpdate ),
    path('Update/Profile/<int:pk>/' ,views.UserProfileUpdate ),
    path('view/user' ,views.UserDetail ),
    path('comments/<int:pk>/' ,views.PageComment ),
    path('comments/create/<int:pk>/' ,views.CreateComment ),
]
