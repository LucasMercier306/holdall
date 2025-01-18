from utils import Utils

class PermissionHandler:

    def __init__(self):

        # Charger le fichier des rôles
        self.roles = Utils.load_yaml("/Users/lucas/Desktop/py/src/role.yaml")
        

        self.object_data_dict = {}

        self.object_ids = [
        "/Users/lucas/Desktop/py/src/yaml_load/abc.yaml",
        "/Users/lucas/Desktop/py/src/yaml_load/def.yaml",
        "/Users/lucas/Desktop/py/src/yaml_load/rbk.yaml",
        "/Users/lucas/Desktop/py/src/yaml_load/vsphere.yaml"
        ]

        breakpoint()

        for file in self.object_ids:
            self.object_data_dict.update(Utils.load_yaml(file))
        
        breakpoint()

        # Créer la table de hashage
        self.hashed_other = Utils.hashtable_obj(self.object_data_dict)

        breakpoint()


    def return_object_id(self, object_name):
        """
        Retourne l'ID d'un objet à partir de son nom en recherchant dans les données fusionnées.
        :param object_name: Nom de l'objet.
        :return: ID de l'objet ou None si non trouvé.
        """
        return self.hashed_other.get(object_name)