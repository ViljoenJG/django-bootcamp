import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()

## Populate DB with fake data
import random
from faker import Faker
from first_app.models import AccessRecord,Webpage,Topic

fake_gen = Faker()

topics = [
    'Search',
    'Social',
    'Marketplace',
    'News',
    'Games'
]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic
        top = add_topic()

        # create fake data for the entry
        f_url = fake_gen.url()
        f_date = fake_gen.date()
        f_name = fake_gen.company()

        # create webpage entry
        web_pg = Webpage.objects.get_or_create(topic=top, url=f_url, name=f_name)[0]

        # create fake AccessRecord
        acc_rec = AccessRecord.objects.get_or_create(name=web_pg, date=f_date)[0]

if __name__ == '__main__':
    print('Populating tables')
    populate(20)
    print('Populating complete')
