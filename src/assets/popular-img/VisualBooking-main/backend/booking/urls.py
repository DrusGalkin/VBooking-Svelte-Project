from rest_framework.routers import DefaultRouter
from booking.view.objects import ObjectView

router = DefaultRouter()

router.register('objects', ObjectView, basename='objects')

urlpatterns = [

]

urlpatterns += router.urls
