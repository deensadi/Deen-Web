from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin Panel
    path('api/users/', include('users.urls')),  # Users API Routes
    path('api/courses/', include('courses.urls')),  # Courses API Routes
    path('api/blog/', include('blog.urls')),  # Blog API Routes
    path('api/school/', include('school.urls')),  # School API Routes
    path('api/payments/', include('payments.urls')),  # Payments API Routes
]
