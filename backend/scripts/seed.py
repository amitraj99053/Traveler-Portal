import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings")
django.setup()
from users.models import CustomUser, MechanicProfile

def run():
    if not CustomUser.objects.filter(username='alice').exists():
        u = CustomUser.objects.create_user(username='alice', password='alicepass', is_mechanic=False, email='alice@example.com')
    if not CustomUser.objects.filter(username='bob').exists():
        m = CustomUser.objects.create_user(username='bob', password='bobpass', is_mechanic=True, email='bob@example.com')
        prof = MechanicProfile.objects.get(user=m)
        prof.skills = "Engine repair, Tire change"
        prof.latitude = 28.6139
        prof.longitude = 77.2090
        prof.available = True
        prof.save()
    if not CustomUser.objects.filter(username='charlie').exists():
        m = CustomUser.objects.create_user(username='charlie', password='charliepass', is_mechanic=True, email='charlie@example.com')
        prof = MechanicProfile.objects.get(user=m)
        prof.skills = "Battery, Electrical"
        prof.latitude = 28.6200
        prof.longitude = 77.2100
        prof.available = True
        prof.save()
    print("Seed done")

if __name__ == "__main__":
    run()
