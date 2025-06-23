from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('documentation/', views.documentation, name='documentation_index'),

    path('components/buttons/', views.buttons, name='components_buttons'),

    path('components/gridsystem/', views.gridsystem, name='components_gridsystem'),

    path('components/panels/', views.panels, name='components_panels'),

    path('components/notifications/', views.notifications, name='components_notifications'),

    path('components/sweetalert/', views.sweetalert, name='components_sweetalert'),

    path('components/font_awesome_icons/', views.font_awesome_icons, name='components_font_awesome_icons'),

    path('components/simple_line_icons/', views.simple_line_icons, name='components_simple_line_icons'),

    path('components/typography/', views.typography, name='components_typography'),

    path('sidebar_style_2/', views.sidebar_style_2, name='sidebar_style_2'),

    path('icon_menu/', views.icon_menu, name='icon_menu'),

    path('forms/forms/', views.basic_form, name='forms_forms'),

    path('tables/basic/', views.tables, name='tables_tables'),

    path('tables/datatables/', views.datatables, name='tables_datatables'),

    path('maps/google/', views.googlemaps, name='maps_googlemaps'),

    path('maps/jsvectormap/', views.jsvectormap, name='maps_jsvectormap'),

    path('charts/charts/', views.charts, name='charts_charts'),

    path('charts/sparkline/', views.sparkline, name='charts_sparkline'),

    path('avatars', views.avatars, name='components_avatars'),

    path('widgets', views.widgets, name='widgets'),

    path('profile', views.profile, name='profile'),

     path('avatars', views.basic_form, name='base_form'),

    path('', views.index, name='demo1_index'),

    path('index/', views.index, name='index'),

]

