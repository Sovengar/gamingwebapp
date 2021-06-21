"""gamingwebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from users import views as user_views
from django.contrib.auth import views as auth_views
from appsite import views as appsite_views
from django.conf import settings 
from django.conf.urls.static import static 
from users.views import Keys_ListView

urlpatterns = [
    path('', include('appsite.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('search/', appsite_views.search_game_queryset, name='search_results'),
    path('partyroom/', appsite_views.partyroom_view, name='appsite-partyroom'),
    path('terms/', user_views.terms_view, name='terms'),
    path('faq/', user_views.faq_view, name='faq'),

    path('cart/', appsite_views.cart_view, name='cart'),
    path('cart/<int:id>/update/>', appsite_views.update_cart_view, name='update_cart'),
    path('cart/<int:id>/purchase/', appsite_views.purchase_cart_view, name='purchase_cart'),

    path('register/', user_views.register_view, name='register'),
    path('profile/', user_views.profile_view, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('register/seller/', user_views.register_seller_view, name='register_seller'),
    path('seller/', user_views.seller_view, name='sellkey'),
    path('user/keys/', Keys_ListView.as_view(), name='keys'),

    re_path(r'^daguerre/', include('daguerre.urls')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG: #Only on development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Manually serving static files urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)