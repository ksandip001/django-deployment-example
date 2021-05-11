import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','basic_pro.settings')

import django
django.setup()

import random
from basic_app.models import Bjp,Access
from faker import Faker

fakegen = Faker()

def populate(N=10):
    for entry in range(N):
        fake_name = fakegen.name()
        fake_email = fakegen.email()
        fake_text= fakegen.text()
        fake_date= fakegen.date()

        bjp = Bjp.objects.get_or_create(name = fake_name , email= fake_email , text = fake_text)[0]
        acc = Access.objects.get_or_create(name = bjp , date = fake_date)[0]

if __name__ == "__main__":
    print("Populating")
    populate(20)
    print("Population Completed")
    
