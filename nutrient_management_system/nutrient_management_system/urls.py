from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/', include('about_us.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^contact/', include('drop_a_note.urls')),
    url(r'^info/', include('nutrients_info.urls')),
    url(r'^user/', include('users.urls')),
    url(r'^home/', include('home.urls'))
]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)
