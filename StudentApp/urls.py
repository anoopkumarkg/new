from rest_framework.routers import DefaultRouter
from .views import StudentView

router= DefaultRouter()

router.register("student_view",StudentView,basename= "student")
