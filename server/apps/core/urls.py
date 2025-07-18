from django.urls import path

from . import views

urlpatterns = [
    # === Core URLs (In Test Right Now ...) ===
    path(r"", views.index, name="index"),
    path(r"home/", views.home, name="home"),
    path(r"home/<path:path>", views.home, name="home_path"),
    # === Pricing Page ===
    path(r"pricing/", views.pricing_page, name="pricing_page"),
    # === Task Page ===
    path(r"create-book/", views.create_book_view, name="create_book_view"),
]
