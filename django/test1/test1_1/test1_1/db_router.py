

# User accounts may be stored in the default database.

class DB_Router:
    def db_for_read(self, model, **hints):

        if model._meta.app_label == "appTest1":
            return "test1"
        # elif model._meta.app_label == 'appTCohort1':
        #     return 'tcohort1'


    def db_for_write(self, model, **hints):

        if model._meta.app_label == "appTest1":
            return "test1"
        # elif model._meta.app_label == 'appTCohort1':
        #     return 'tcohort1'

    def allow_relation(self, obj1, obj2, **hints):

        if obj1._meta.app_label == 'appTest1' or \
           obj2._meta.app_label == 'appTest1':
           return True

        # if obj1._meta.app_label == 'appTCohort1' or \
        #    obj2._meta.app_label == 'appTCohort1':
        #    return True

    def allow_migrate(self, db, app_label, model=None, **hints):

        if app_label == "appTest1":
            return db == "test1"
        # elif app_label == 'appTCohort1':
        #     return db == 'tcohort1'