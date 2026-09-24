from rest_framework.routers import DefaultRouter
from .views import TaskViewset

router = DefaultRouter()
router.register('tasks', TaskViewset)

urlpatterns = router.urls