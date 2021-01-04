from django.urls import path 
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('faq', views.faq_page, name='faq_page'),
        path('query',views.query_page, name='query_page'),
        path('query_table',views.query_table_page, name='query_table_page'),
        path('status',views.status_page, name='status_page'),
        path('error', views.error_page, name='error_page'),
        path('add_query', views.add_query, name='add_query'),
        path('get_query', views.get_query, name='get_query'),
        path('edit/<int:id>', views.edit, name='edit'),
        path('update/<int:id>', views.update, name='update'),
        path('delete/<int:id>', views.delete, name='delete'),
        path('rmd/<int:id>',views.rmd, name='rmd'),

]