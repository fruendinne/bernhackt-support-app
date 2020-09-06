# Quickline Support Backend
##### Based on DRFx project template

## First-time setup

1.  Make sure Python 3.7x and Pipenv are already installed. [See here for help](https://djangoforbeginners.com/initial-setup/).
2.  Clone the repo and configure the virtual environment:

```
$ git clone https://github.com/fruendinne/bernhackt-support-app.git
$ cd code/backend
$ pipenv install
$ pipenv shell
```

Set up the initial migration for our custom user models in users and build the database.

```
(env) $ python manage.py migrate
(env) $ python manage.py createsuperuser
(env) $ python manage.py runserver
```

Fill in some mock data:

```
(env) $ python manage.py generate_mock_data // This deletes all other data!
```

**Endpoints**

Data structures are managed by the django admin page on http://127.0.0.1:8000/admin.

- Start a new Flow - http://127.0.0.1:8000/api/v1/support/start_flow
- Get next TLB for Flow - http://127.0.0.1:8000/api/v1/support/next_tlb/<pk>
- Mark Flow as Successful - http://127.0.0.1:8000/api/v1/support/set_success/<pk>

5.  Template-based Endpoints
- See generated help pages (for indexing) - http://127.0.0.1:8000/api/v1/support/helppages

There is also a management command to auto-generate static help pages from pre-learned successful flows:
```
(env) $ python manage.py generate_static_help_pages
```
