from django.urls import path, include
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import GiocatoreViewSet, squadreViewSet, MyTokenObtainPairView, UserViewSet

# Crea un router per gestire automaticamente gli URL dei ViewSets.
# DefaultRouter include route di default per listare, creare,
# recuperare, aggiornare ed eliminare oggetti.

router = DefaultRouter()
router.register(r'giocatori', GiocatoreViewSet)
router.register(r'squadre', squadreViewSet)


# urlpatterns è la lista principale dei pattern URL del progetto/applicazione.
# Django cerca un pattern URL che corrisponda alla richiesta in arrivo
# e invia la richiesta alla vista associata al primo pattern corrispondente.

urlpatterns = [
    path('', include(router.urls)),
    # path('api/mie-squadre/', include(router.urls)),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]