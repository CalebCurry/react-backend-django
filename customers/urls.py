from django.contrib import admin
from django.urls import path
from customers import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/customers/', views.customers, name='customers'),
    path('api/customers/<int:id>/', views.customer, name='customer'),
    path('api/register/', views.register, name='register'),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True)))
]
