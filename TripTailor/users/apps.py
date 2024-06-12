from django.apps import AppConfig

class UsersConfig(AppConfig):
    """
    Configuration for the Users application.

    Attributes:
        default_auto_field (str): Specifies the default type
        for auto-generated primary keys.
        name (str): The name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        """
        Method to perform initialization tasks when the app is ready.

        This method imports the `users.signals` module,
        which is typically used
        to register signal handlers for the application.

        Note:
            This method is called once Django has loaded all apps.
        """
        import users.signals