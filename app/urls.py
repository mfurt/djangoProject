from django.urls import path
from .views import Index, Detail, UserProfileView, order

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('detail/<int:pk>', Detail.as_view(), name='detail'),
    path('profile/', UserProfileView.as_view(), name="profile"),
    path('detail/<product_id>/order', order, name="order"),
]
