#create database router to destinguish between dynamic and fixed database
class Router(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'eveassets':
            return 'eveassets'
        elif model._meta.app_label == 'metrics':
            return 'metrics'
        return "default"

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'eveassets':
            return 'eveassets'
        elif model._meta.app_label == 'metrics':
            return 'metrics'
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, model):
        if db == 'eveassets':
            return model._meta.app_label == 'eveassets'
        elif db == 'metrics':
            return model._meta.app_label == 'metrics'
        elif model._meta.app_label == 'eveassets':
            return False
        elif model._meta.app_label == 'metrics':
            return False
        return True
