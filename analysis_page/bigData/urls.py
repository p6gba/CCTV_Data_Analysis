from django.urls import path
from . import views

urlpatterns = [
    path('base', views.base, name='base'),
    path('Category_1', views.Category_1, name='Category_1'),
    path('Category_2', views.Category_2, name='Category_2'),
    path('Category_3', views.Category_3, name='Category_3'),
    path('Category_4', views.Category_4, name='Category_4'),
    path('heatmap_menu1', views.heatmap_menu1, name='heatmap_menu1'),
    # 회원가입
    path('signUp', views.signUp.as_view(), name='signUp'),
    # 로그인
    path('', views.logIn.as_view(), name='logIn'),

    # D3 HeatMap JSON
    # From_to_date Get
    path('HeatMapJSON', views.HeatMapJSON, name='HeatMapJSON'),
    path('Get_menu1_Total', views.Get_menu1_Total, name='Get_menu1_Total'),
    path('RuleResult', views.RuleResult, name='RuleResult'),
    path('Get_menu2_Total', views.Get_menu2_Total, name='Get_menu2_Total'),
    path('Product', views.Product, name='Product'),
    path('Get_menu3_Total', views.Get_menu3_Total, name='Get_menu3_Total'),
    path('find_all', views.find_all, name='find_all'),
    path('default_GetTotal', views.default_GetTotal, name='default_GetTotal'),
    path('default_GetTotal2', views.default_GetTotal2, name='default_GetTotal2'),
    path('menu3_date', views.menu3_date, name='menu3_date'),
    path('menu3_gender', views.menu3_gender, name='menu3_gender'),
]
