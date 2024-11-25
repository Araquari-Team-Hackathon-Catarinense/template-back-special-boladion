from core.parking.infra.parking_django_app.models import Parking


def generate_services():
    services = list()
    parkings = Parking.objects.all()

    for parking in parkings:
        for i in range(3):
            service = {
                "description": f"Service {i}",
                "payment_rules": {"rule": "value"},
                "parking": parking,
            }
            services.append(service)

    return services
