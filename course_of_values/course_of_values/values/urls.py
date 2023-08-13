from django.urls import path

from course_of_values.values.views import buying, selling, IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('buying/', buying, name='buying'),
    path('selling/', selling, name='selling'),
)
