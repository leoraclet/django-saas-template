from django.conf import settings
from django.core.cache import caches
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.db import DEFAULT_DB_ALIAS


class Command(BaseCommand):
    def handle(self, **options):
        if "postgresql" not in settings.DATABASES[DEFAULT_DB_ALIAS]["ENGINE"]:
            raise CommandError(
                "This command can be used only with PostgreSQL databases."
            )

        # 2. Reset database to nothing
        self.stdout.write("Reset schema")
        call_command("reset_schema", interactive=False)

        # 3. Rebuild database
        call_command("migrate", interactive=False)

        # 4. Clear caches
        for cache in caches.all():
            cache.clear()

        # 6. Change the admin password (in case it's different in this environment)
        call_command("reset_admin_password")
