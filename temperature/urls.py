from django.urls import path

from .views import (
    ReportListView,
    ReportDetail
)

urlpatterns = [
    path('',  ReportListView.as_view(), name="ReportListView"),
    path("<int:pk>/", ReportDetail.as_view(), name="ReportDetailView")
]