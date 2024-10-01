from django.shortcuts import render
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

def phone_info(request):
    number_info = None
    if request.method == "POST":
        number = request.POST.get("phone_number")
        try:
            phone = phonenumbers.parse(number)
            time_zones = timezone.time_zones_for_number(phone)
            car = carrier.name_for_number(phone, "en")
            reg = geocoder.description_for_number(phone, "en")
            number_info = {
                "phone": phone,
                "time_zones": time_zones,
                "carrier": car,
                "region": reg
            }
        except Exception as e:
            number_info = {"error": str(e)}

    return render(request, 'phoneapp/phone_info.html', {'number_info': number_info})
