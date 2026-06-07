from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    def ready(self):
        # The import MUST stay inside this ready method
        # so Django doesn't read it until the apps are fully loaded!
        import profiles.signals
