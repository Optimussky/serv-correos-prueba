from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import SpectacularAPIView,SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/', include('login.api.urls')),
    path('api/schema/swagger-ui/',SpectacularSwaggerView.as_view(url_name='schema'), name = 'swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'),name='redoc'),
    path('api/auth/login',include('login.api.urls'))
]
