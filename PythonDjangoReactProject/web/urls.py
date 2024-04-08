"""
    - import django => import java.util.*
    - from django.urls import path => import java.util.Scanner
"""

from django.urls import path
from web import views, food_views, recipe_views
# localhost:8000
urlpatterns=[
    #root => ''
    path('', views.main_page),
    path('food/list/', food_views.food_list), # 주소가 food/list/ 일때 food_views.food_list를 호출
    path('food/find/', food_views.food_find),
    path('recipe/list/', recipe_views.recipe_list_view),
    path('recipe/list_vue/', recipe_views.recipe_list), # vue가 붙은 것은 JSON을 넘겨주는 역할
    path('recipe/find/', recipe_views.recipe_find_view), # 화면을 변경시켜주는 역할
    path('recipe/find_vue/', recipe_views.recipe_find),
    path('recipe/chef/', recipe_views.recipe_chef_view),
    path('recipe/chef/vue', recipe_views.recipe_chef),
    path('food/food_detail/', food_views.food_detail),
    path('recipe/detail/', recipe_views.recipeDetailView),
    path('recipe/detail_vue/', recipe_views.recipeDetail)
]
