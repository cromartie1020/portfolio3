
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from todo import views as todo_view

admin.site.site_header="Cromartie's Admin"
admin.site.index_title="Features"



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('user/',include('user.urls')),
    path('contact/',include('contact.urls')),
    path('',todo_view.todo,name='todo'),
    path('newtodo/',todo_view.todo_form,name='newtodo'),
    path('deletetodo/<int:pk>/',todo_view.todo_delete,name='deletetodo'),
    path('updatetodo/<int:pk>/',todo_view.todo_update,name='updatetodo'),
    path('post/',include('post.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
