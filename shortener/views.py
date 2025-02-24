import secrets

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView

from .models import URL


class IndexView(TemplateView):
    template_name = "shortener/index.html"

    def post(self: "IndexView", request: HttpRequest) -> HttpResponse:
        original_url = request.POST.get("url")
        if original_url:
            short_code = self.generate_short_code()
            URL.objects.create(original_url=original_url, short_code=short_code)
            short_url = request.build_absolute_uri(reverse("redirect_url", args=[short_code]))
            return render(request, self.template_name, {"short_url": short_url})
        return render(request, self.template_name)

    @staticmethod
    def generate_short_code() -> str:
        while True:
            code = secrets.token_urlsafe(6)[:8]
            if not URL.objects.filter(short_code=code).exists():
                return code


def redirect_url(_request: HttpRequest, short_code: str) -> HttpResponse:
    url = URL.objects.get(short_code=short_code)
    url.click_count += 1
    url.save()
    return redirect(url.original_url)
