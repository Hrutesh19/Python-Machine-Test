# Django-Python-Machine-Test
Assignment for Nimap Infotech

Consider the following scenario where we have 3 entities in our system.

    User

    Client

    Project

We have the number of users registered in our system.

You can use Django’s default admin template to create/register users but not other entities or you can make REST APIs for users as well if you want.

You have to perform the following tasks :

    Register a client

    Fetch clients info

    Edit/Delete client info

    Add new projects for a client and assign users to those projects.

    Retrieve assigned projects to logged-in users.

Things to consider :

    The system has many users.

    The system has many clients.

    A client can have many projects

    A single project can be assigned to many users.




Installation Process****

python -m venv env_name

source venv/Scripts/activate

pip install django

pip install djangorestframework

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py 


![Screenshot (368)](https://github.com/16shashikant16/Django-Python-Machine-Test/assets/55691120/5f0d3971-56fe-433e-b1e8-ffe14db85f94)



![Screenshot (369)](https://github.com/16shashikant16/Django-Python-Machine-Test/assets/55691120/3242efe6-e853-4f0c-9bbe-070de3921b69)


![Screenshot (370)](https://github.com/16shashikant16/Django-Python-Machine-Test/assets/55691120/70a9d260-a46f-418b-9f58-50f06a96981e)


![Screenshot (371)](https://github.com/16shashikant16/Django-Python-Machine-Test/assets/55691120/7066f3fb-aa83-40f4-bfd9-0b30f7465651)


![Screenshot (372)](https://github.com/16shashikant16/Django-Python-Machine-Test/assets/55691120/c3b92e59-593e-444f-8d35-d7efcd9b8798)
