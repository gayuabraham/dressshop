from django.urls import path , include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register("item" ,prd_view)


urlpatterns = [
    # path('api/items/' , item_api.as_view()),
    # path('api/items/<int:pk>/' , item_api.as_view()),
    # path('item/' , prd_fun),
    # path('item/<int:pk>' , prd_fun),/
    # path('item/' , prd_gen.as_view()),
    # path('item/<int:pk>' , prod_crt.as_view() ),
    path('', include(router.urls)),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/signup/' , signup ),
    path('dummy' , get_dummy_data)
]

