import django
from faker import Faker
from AppTwo.models import User
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')
django.setup()

fakegen = Faker()


def populate(N):
    for entry in range(N):

        fake_fname = fakegen.name()
        fake_lname = fakegen.name()
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_fname,
                                          last_name=fake_lname,
                                          email=fake_email)
        user.save()


if __name__ == '__main__':
    print('populating data...  please wait')
    populate(20)
    print('populating complete')
