from rest_framework.routers import DefaultRouter
from .views import AgendamentoViewSet

router = DefaultRouter()
router.register(r'agendamentos', AgendamentoViewSet)

urlpatterns = router.urls 