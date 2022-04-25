from rest_framework import routers

from .viewsets import BookViewset

router = routers.SimpleRouter()
router.register('books', BookViewset)

urlpatterns = router.urls