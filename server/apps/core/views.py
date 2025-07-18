from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from djstripe.settings import djstripe_settings

from .tasks import create_book


def index(request):
    return render(request, "_base.html")


def home(request, path=""):
    return render(request, "core/home.html")


@login_required
def pricing_page(request):
    return render(
        request,
        "core/pricing_page.html",
        {
            "stripe_public_key": djstripe_settings.STRIPE_PUBLIC_KEY,
            "stripe_pricing_table_id": settings.STRIPE_PRICING_TABLE_ID,
        },
    )


def create_book_view(request):
    task = create_book.delay()  # type: ignore

    return JsonResponse(
        {
            "status": "The book is being created...",
            "task_id": task.id,
        }
    )
