from rest_framework.routers import DefaultRouter
from users.view.user import UserView

router = DefaultRouter()
router.register('users', UserView, basename='users')

urlpatterns = [

]

urlpatterns += router.urls