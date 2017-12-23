import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'protwo.settings')
django.setup()

## Populate DB with fake data
from faker import Faker
from apptwo.models import User

fake_gen = Faker()

def populate(N=5):
    for entry in range(N):
        f_name = fake_gen.first_name()
        l_name = fake_gen.last_name()
        email = fake_gen.email()

        # create webpage entry
        User.objects.get_or_create(first_name=f_name, last_name=l_name, email=email)

if __name__ == '__main__':
    print('Populating tables')
    populate(20)
    print('Populating complete')
