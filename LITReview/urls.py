"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeView, PasswordChangeDoneView)

import authentication.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.LoginPageView.as_view(), name='login'),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
        name='login'),
    path('home/', blog.views.home, name='home'),
    path('posts/', blog.views.posts, name='posts'),
    path('ticket/', blog.views.ticket_upload, name='ticket'),
    path('review/', blog.views.review_upload, name='review'),
    path('blog/ticket_review/<int:ticket_id>', blog.views.ticket_review_upload, name='ticket_review'),
    path('logout/', LogoutView.as_view(template_name='authentication/login.html'), name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('blog/ticket/<int:ticket_id>', blog.views.view_ticket, name='view_ticket'),
    path('blog/review/<int:review_id>', blog.views.view_review, name='view_review'),
    path('blog/ticket/<int:ticket_id>/edit', blog.views.edit_ticket, name='edit_ticket'),
    path('blog/review/<int:review_id>/edit', blog.views.edit_review, name='edit_review'),
    path('home/', blog.views.edit_ticket, name='delete_ticket'),
    path('home/', blog.views.edit_review, name='delete_review'),
    path('follow-users/', blog.views.follow_users, name='follow_users'),
    path('follow-users/<int:followed_user_id>', blog.views.delete_subscription, name='delete_subscription'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)
