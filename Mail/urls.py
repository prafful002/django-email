from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'Mail.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','invoice.views.main',name='main'),
    url(r'^pdf$','invoice.views.myview',name='myview'),
    url(r'^admin/', include(admin.site.urls)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
