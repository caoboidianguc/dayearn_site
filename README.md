#this first project with django
should run python v12
python3 -m venv venv --prompt=dayearn

Mac source ./venv/bin/activate
Win venv\Scripts\activate

pip install -r requirements.txt
django-admin startproject



Add to INSTALLED_APPS:
'crispy_forms',
'schedule',
"crispy_bootstrap5",
'phonenumber_field',


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = 'US'

Add to TEMPLATE_CONTEXT_PROCESSORS:
"django.template.context_processors.request"