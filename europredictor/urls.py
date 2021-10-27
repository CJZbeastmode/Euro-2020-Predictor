"""europredictor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from euro.views import predictor, home, login, register, logout, page_not_found, forbidden, unauthorized, method_not_allowed, save, pdf, community, my_homepage, prediction, delete, edit_user, devblog, help_us, about_us, terms_and_notices, newsroom, detail_news, newsletter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('predictor/', predictor, name='predictor'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('edit_user/', edit_user, name='edit_user'),
    ##### Save
    path('save/<str:gs_a1>/<str:gs_a2>/<str:gs_a3>/<str:gs_a4>/<str:gs_b1>/<str:gs_b2>/<str:gs_b3>/<str:gs_b4>/<str:gs_c1>/<str:gs_c2>/<str:gs_c3>/<str:gs_c4>/<str:gs_d1>/<str:gs_d2>/<str:gs_d3>/<str:gs_d4>/<str:gs_e1>/<str:gs_e2>/<str:gs_e3>/<str:gs_e4>/<str:gs_f1>/<str:gs_f2>/<str:gs_f3>/<str:gs_f4>/<str:btf_1>/<str:btf_2>/<str:btf_3>/<str:btf_4>/<str:btf_l1>/<str:btf_l2>/<str:ks16_aw>/<str:ks16_al>/<str:ks16_bw>/<str:ks16_bl>/<str:ks16_cw>/<str:ks16_cl>/<str:ks16_dw>/<str:ks16_dl>/<str:ks16_ew>/<str:ks16_el>/<str:ks16_fw>/<str:ks16_fl>/<str:ks16_gw>/<str:ks16_gl>/<str:ks16_hw>/<str:ks16_hl>/<str:ks8_aw>/<str:ks8_al>/<str:ks8_bw>/<str:ks8_bl>/<str:ks8_cw>/<str:ks8_cl>/<str:ks8_dw>/<str:ks8_dl>/<str:ks4_aw>/<str:ks4_al>/<str:ks4_bw>/<str:ks4_bl>/<str:final_l>/<str:winner>/', save, name='save'),
    path('pdf/<str:gs_a1>/<str:gs_a2>/<str:gs_a3>/<str:gs_a4>/<str:gs_b1>/<str:gs_b2>/<str:gs_b3>/<str:gs_b4>/<str:gs_c1>/<str:gs_c2>/<str:gs_c3>/<str:gs_c4>/<str:gs_d1>/<str:gs_d2>/<str:gs_d3>/<str:gs_d4>/<str:gs_e1>/<str:gs_e2>/<str:gs_e3>/<str:gs_e4>/<str:gs_f1>/<str:gs_f2>/<str:gs_f3>/<str:gs_f4>/<str:btf_1>/<str:btf_2>/<str:btf_3>/<str:btf_4>/<str:btf_l1>/<str:btf_l2>/<str:ks16_aw>/<str:ks16_al>/<str:ks16_bw>/<str:ks16_bl>/<str:ks16_cw>/<str:ks16_cl>/<str:ks16_dw>/<str:ks16_dl>/<str:ks16_ew>/<str:ks16_el>/<str:ks16_fw>/<str:ks16_fl>/<str:ks16_gw>/<str:ks16_gl>/<str:ks16_hw>/<str:ks16_hl>/<str:ks8_aw>/<str:ks8_al>/<str:ks8_bw>/<str:ks8_bl>/<str:ks8_cw>/<str:ks8_cl>/<str:ks8_dw>/<str:ks8_dl>/<str:ks4_aw>/<str:ks4_al>/<str:ks4_bw>/<str:ks4_bl>/<str:final_l>/<str:winner>/<str:name>/', pdf, name='pdf'),
    path('delete/<int:id>', delete, name='delete'),  
    ##### Extra
    path('devblog/', devblog, name='devblog'),
    path('help_us/', help_us, name='help_us'),
    path('about_us/', about_us, name='about_us'),
    path('terms_and_notices/', terms_and_notices, name='terms_and_notices'),
    path('newsroom/',newsroom, name='newsroom'),
    path('detail_news/<int:id>/', detail_news, name='detail_news'),
    path('newsletter/',newsletter, name='newsletter'),
    ##### Error
    path('404/', page_not_found, name='404'),
    path('403/', forbidden, name='403'),
    path('401/', unauthorized, name='401'),
    path('405/', method_not_allowed, name='405'),
    path('community/', community, name='community'),
    path('my_homepage/', my_homepage, name='my_homepage'),
    path('prediction/<int:id>/', prediction, name='prediction')
]