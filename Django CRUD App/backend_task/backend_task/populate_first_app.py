import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","backend_task.settings")

import django
django.setup()

import random
from first_app.models import New_Project
from faker import Faker
fakegen = Faker()


def populate(N):
    for entry in range(N):
        fake_SNo = Faker.random_digit_not_null()
        fake_pr_name = Faker.company()
        fake_st_date = Faker.date()
        fake_deadline = Faker.date() 

        data = New_Project.objects.get_or_create(SNo=fake_SNo,Project_Name=fake_pr_name,Start_Date=fake_st_date,Deadline=fake_deadline)

if __name__ == '__main__':
    print('Populating...')
    populate(10)
    print('Completed populating')