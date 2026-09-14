from django.shortcuts import render, redirect
from .models import ContactMessage, Service, Destination
from .utils import send_contact_email
from .map_utils import get_map_areas


def home(request):
    return render(request, "home.html", {
        "services": Service.objects.filter(is_active=True).order_by("order")[:3],
        "destinations": Destination.objects.filter(is_active=True).order_by("order")[:4],
        "map_areas": get_map_areas(),
    })


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html", {
        "services": Service.objects.filter(is_active=True).order_by("order"),
    })


def destinations(request):
    destination_qs = Destination.objects.filter(is_active=True).order_by("order")
    region = request.GET.get("region", "").strip()
    if region:
        destination_qs = destination_qs.filter(region__icontains=region)

    return render(request, "destinations.html", {
        "destinations": destination_qs,
        "active_region": region,
    })


def destination_detail(request, slug):
    destination = Destination.objects.filter(slug=slug, is_active=True).first()
    return render(request, "destination_detail.html", {
        "destination": destination,
    })


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        travel_dates = request.POST.get("travel_dates")
        message = request.POST.get("message")

        inquiry = ContactMessage.objects.create(
            name=name,
            email=email,
            travel_dates=travel_dates,
            message=message
        )

        send_contact_email(inquiry)

        return redirect("contact")

    return render(request, "contact.html")