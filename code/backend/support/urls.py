from django.urls import include, path

from . import views

urlpatterns = [
    path('start_flow/', views.start_flow),
    path('next_tlb/<int:pk>', views.next_tlb),
    path('set_success/<int:pk>', views.set_success),
    path('helppages/', views.helppages_index),
    path('test_stuff/', views.test_stuff),
]
