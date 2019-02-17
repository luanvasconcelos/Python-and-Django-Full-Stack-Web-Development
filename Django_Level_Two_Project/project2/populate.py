import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project2.settings')

import django
django.setup()

import random
from app2.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for i in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        auser = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print('Pupulating...')
    populate()
    print('Fake populate complete!')
