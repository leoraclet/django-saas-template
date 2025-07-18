from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, reverse

from .models import Book
from .tasks import create_book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["__str__", "title", "author", "content", "pub_date"]
    change_list_template = "admin/core/change_list.html"
    readonly_fields = ["pub_date"]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "generate/",
                self.admin_site.admin_view(self.admin_create_book_view),
                name="create_book",
            ),
        ]
        return custom_urls + urls

    def admin_create_book_view(self, request):
        # https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#reversing-admin-urls
        redirect_url = reverse("admin:core_book_changelist")

        result = create_book.delay(redirect_url=redirect_url)  # type: ignore
        self.message_user(request, "Started creating a book ...")

        return redirect("admin:task_status", result.id)
