"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from mysite.view import here, add, math
from restaurants.views import waiting_time_evaluate
from evaluate_time.views import waiting

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('here/<slug:a>', here),
    path('<int:a>/plus/<int:b>', add),
    path('<int:a>/math/<int:b>', math),
    path('waiting/', waiting_time_evaluate),
    path('evaluate_time/', waiting)
]