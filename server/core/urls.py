from django.urls import path
from . import views


app_name= 'core'

urlpatterns = [
    path('', views.home, name='home'),
	path('link_1/', views.link_1, name='link_1'),
	path('link_2/', views.link_2, name='link_2'),
	path('link_3/', views.link_3, name='link_3'),
	path('link_4/', views.link_4, name='link_4'),

	#Home_Page "Hmmm, I Need ..." option links
	path('i_need_option_01/', views.i_need_option_01, name='i_need_option_01'),
]