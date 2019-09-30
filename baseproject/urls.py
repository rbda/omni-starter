from django.shortcuts import render
from django.urls import path, include
from django.conf import settings
from django.views.generic.base import View
import omni
from django.contrib import admin

admin.autodiscover()

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


urlpatterns = [
    # path("", hello.views.index, name="index"),
    # path("terms/", include(terminology.urls)),
    path('', IndexView.as_view(), name="index"),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path("admin/", admin.site.urls),
    path("omni/", include('omni.urls')),
    path('accounts/signup/',  omni.views.SignUp.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),

]

# django-debug-toolbar
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
        # path('', HelloWorld.as_view(), name="hello_world"),
    ]


# Hello World
# if settings.DEBUG:
#     from django.views.generic.base import View, View
#     from django.shortcuts import render
#
#     class HelloWorld(View):
#         def get(self, request, *args, **kwargs):
#             return render(request, "index.html")
#
#
#     urlpatterns += [
#         # path('__debug__/', include(debug_toolbar.urls)),
#         path('', HelloWorld.as_view(), name="hello_world"),
#     ]
