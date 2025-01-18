from utils import Utils

class PermissionHandler:
    def __init__(self, role_file, *other_files):
        """
        :param role_file: Le fichier YAML des rôles.
        :param other_files: Liste des autres fichiers YAML à charger.
        """
        # Charger le fichier des rôles
        self.roles = Utils.load_yaml(role_file)
        
        # Charger et fusionner les autres fichiers YAML
        self.other_data = {}
        for file in other_files:
            self.other_data.update(Utils.load_yaml(file))  # Fusionner les données des autres fichiers

        # Créer la table de hashage pour les autres fichiers
        self.hashed_other = Utils.hashtable_obj(self.other_data)  # Table de hachage pour les autres fichiers

    def return_object_id(self, object_name):
        """
        Retourne l'ID d'un objet à partir de son nom en recherchant dans les données fusionnées.
        :param object_name: Nom de l'objet.
        :return: ID de l'objet ou None si non trouvé.
        """
        return self.hashed_other.get(object_name)

    def index(self):
        """
        Parcourt les rôles et affiche les permissions avec leurs IDs correspondants.
        """
        for role_name, role_data in self.roles.items():
            print(f"Role: {role_name}")
            
            permissions = role_data.get('permissions', {}).get('accept', [])
            print("Permissions:")
            for permission in permissions:
                object_id = self.return_object_id(permission)
                print(f"  - {permission}: {object_id}")