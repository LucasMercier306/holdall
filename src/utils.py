import yaml

class Utils:

    def __init__(self):
        pass

    @staticmethod
    def load_yaml(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
                return data
        except FileNotFoundError:
            print(f"Erreur : Le fichier '{file_path}' est introuvable.")
        except yaml.YAMLError as e:
            print(f"Erreur lors du chargement du fichier YAML : {e}")
        except Exception as e:
            print(f"Une erreur inattendue s'est produite : {e}")
        return None
    
    @staticmethod
    def hashtable_obj(host_data):
        """
        Crée un hash table (dictionnaire) à partir des données du fichier host.yaml.
        :param host_data: Dictionnaire contenant les données du fichier host.yaml.
        :return: Dictionnaire clé-valeur {nom_objet: id_objet}.
        """
        return {key: value for key, value in host_data.items()}


 