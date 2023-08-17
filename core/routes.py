from rest_framework.routers import DefaultRouter
from hammer_system.views import UserViewset
import sqlite3

router=DefaultRouter()

router.register('auth', UserViewset )