import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TP_208.settings')

application = get_wsgi_application()

try:
    from django.core.management import call_command
    call_command('collectstatic', '--no-input')
    call_command('migrate', '--no-input')
    from django.contrib.auth import get_user_model
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', '', 'admin1234')
        print("Superutilisateur admin créé !")
except Exception as e:
    print(f"Erreur : {e}")
