"""See https://docs.djangoproject.com/en/dev/topics/db/multi-db/#using-routers 
for details on db routers."""

class Contacto_Router(object): 
    """
    AJ/models.py => AJdb, others => default
     #Usar route_app_labels = {'ajdb', 'contenttypes'} si hay mas bases de datos de APPs

    """

    route_app_labels = {'Contacto'}
    

    def db_for_read(self, model, **hints):
        "Point all operations on aj models to 'ajdb'"
        if model._meta.app_label in self.route_app_labels:
            return 'bd_contacto'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on aj models to 'ajbd'"
        if model._meta.app_label in self.route_app_labels:
            return 'bd_contacto'
        return 'default' #tambien se puede usar return None
    
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in aj app"
        if obj1._meta.app_label in self.route_app_labels and obj2._meta.app_label in self.route_app_labels:
            return True
        # Allow if neither is aj app
        elif self.route_app_labels not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'bd_contacto' or model._meta.app_label in self.route_app_labels:
            return False 
        else: 
            return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
            Make sure the Contacto_Clientes apps only appear in the
            'bd_contacto' database.
            """
        if app_label in self.route_app_labels:
            return db == 'bd_contacto'
        return None
       
        

           

            


            