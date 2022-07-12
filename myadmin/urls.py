from django.urls import path, re_path
from . import views

urlpatterns = [
    # General
    re_path(r'^$', views.index, name='myadmin_index'),
    re_path(r'^login$', views.login, name='myadmin_login'),

    # url(r'^export_order_wo_doc/$', fixbug.export_order_wo_doc, name='weekly_enterpriseorder_report'),
]