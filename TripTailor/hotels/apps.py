from django.apps import AppConfig


class HotelsConfig(AppConfig):
    """
    Configuration for the Hotels application.

    Attributes:
        default_auto_field (str): Specifies the default type for
        auto-generated primary keys.
        name (str): The name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hotels'
