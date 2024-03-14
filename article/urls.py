from django.urls import path 
from .views import add_article,show_article,article_by_category,detaile_article,delete_article,edit_article

urlpatterns = [
    path('',show_article, name='show_article'),
    path('detail/<int:id>/',detaile_article, name='detaile_article'),
    path('category/<slug:category_slug>/',article_by_category, name='article_by_category'),
    path('add_article/', add_article, name='add_article'),
    path('delete_article/<int:id>/', delete_article, name='delete_article'),
    path('edit_article/<int:id>', edit_article, name='edit_article'),
]