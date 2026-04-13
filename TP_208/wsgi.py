import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TP_208.settings')

# Exécuter les migrations automatiquement au démarrage
try:
    from django.db import connection
    from django.db.migrations.executor import MigrationExecutor
    executor = MigrationExecutor(connection)
    plan = executor.migration_plan(executor.loader.graph.leaf_nodes())
    if plan:
        from django.core.management import call_command
        call_command('migrate', '--no-input')
        # Créer le superutilisateur si inexistant
        from django.contrib.auth import get_user_model
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', '', 'admin1234')
except Exception as e:
    print(f"Migration error: {e}")

application = get_wsgi_application()
