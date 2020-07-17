from books.views import BooksList
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'books', BooksList)
urlpatterns = router.urls
