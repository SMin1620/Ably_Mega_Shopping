from django.urls import path

from review.views import (
    ReviewListCreateViewSet
)


review_create = ReviewListCreateViewSet.as_view({
    'post': 'create'
})


urlpatterns = [
    path('', review_create),
]