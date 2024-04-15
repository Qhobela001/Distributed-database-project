class QuthingRouter:
    """
    A router to control database operations for the 'quthing_db' database.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read 'quthing_db' models go to 'quthing_db' database.
        """
        if model._meta.app_label == 'quthing_app':
            return 'quthing_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write 'quthing_db' models go to 'quthing_db' database.
        """
        if model._meta.app_label == 'quthing_app':
            return 'quthing_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both models are in the 'quthing_db' database.
        """
        if obj1._meta.app_label == 'quthing_app' and obj2._meta.app_label == 'quthing_app':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the 'quthing_db' database is not used for migrations.
        """
        if app_label == 'quthing_app':
            return db == 'quthing_db'
        return None


class MaseruRouter:
    """
    A router to control database operations for the 'maseru_db' database.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read 'maseru_db' models go to 'maseru_db' database.
        """
        if model._meta.app_label == 'maseru_app':
            return 'maseru_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write 'maseru_db' models go to 'maseru_db' database.
        """
        if model._meta.app_label == 'maseru_app':
            return 'maseru_app'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both models are in the 'maseru_db' database.
        """
        if obj1._meta.app_label == 'maseru_app' and obj2._meta.app_label == 'maseru_app':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the 'maseru_db' database is not used for migrations.
        """
        if app_label == 'maseru_app':
            return db == 'maseru_app'
        return None


class MafetengRouter:
    """
    A router to control database operations for the 'mafeteng_db' database.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read 'mafeteng_db' models go to 'mafeteng_db' database.
        """
        if model._meta.app_label == 'mafeteng_app':
            return 'mafeteng_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write 'mafeteng_db' models go to 'mafeteng_db' database.
        """
        if model._meta.app_label == 'mafeteng_app':
            return 'mafeteng_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both models are in the 'mafeteng_db' database.
        """
        if obj1._meta.app_label == 'mafeteng_app' and obj2._meta.app_label == 'mafeteng_app':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the 'mafeteng_db' database is not used for migrations.
        """
        if app_label == 'mafeteng_app':
            return db == 'mafeteng_db'
        return None
