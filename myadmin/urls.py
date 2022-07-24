from django.urls import path, re_path
from . import views

urlpatterns = [
    # Common
    re_path(r'^$', views.index, name='myadmin_index'),
    re_path(r'^login$', views.login, name='myadmin_login'),
    # Danh muc 
    re_path(r'^danhmuc$', views.danhmuc, name='danhmuc_index'),
    re_path(r'^danhmuc_tao$', views.danhmuc_tao, name='danhmuc_tao'),
    re_path(r'^danhmuc_sua/(?P<danhmuc_id>[0-9]+)$', views.danhmuc_sua, name='danhmuc_sua'),
    re_path(r'^danhmuc_xoa/(?P<danhmuc_id>[0-9]+)$', views.danhmuc_xoa, name='danhmuc_xoa'),
    # Bai viet 
    re_path(r'^baiviet$', views.baiviet_index, name='baiviet_index'),
    re_path(r'^baiviet_tao$', views.baiviet_tao, name='baiviet_tao'),
    re_path(r'^baiviet_sua/(?P<baiviet_id>[0-9]+)$', views.baiviet_sua, name='baiviet_sua'),
    re_path(r'^baiviet_xoa/(?P<baiviet_id>[0-9]+)$', views.baiviet_xoa, name='baiviet_xoa'),

    # url(r'^export_order_wo_doc/$', fixbug.export_order_wo_doc, name='weekly_enterpriseorder_report'),
]