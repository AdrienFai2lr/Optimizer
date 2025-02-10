# unit_manager.py
import json
from unit import Unit
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')

class UnitManager:
    def __init__(self):
        self.units = []
        self.current_wizard_id = None
    
    def load_from_json(self, file_path):
        self.units = []  # Réinitialiser la liste
        try:
            logging.info(f"Tentative de lecture du fichier: {file_path}")
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Essayer de parser le JSON directement
                try:
                    data = json.loads(content)
                    logging.info("Fichier JSON chargé avec succès")
                    
                    if "unit_list" in data:
                        unit_list = data["unit_list"]
                        logging.info(f"Nombre d'unités trouvées dans le JSON: {len(unit_list)}")
                        
                        for unit_data in unit_list:
                            self._add_unit(unit_data)
                        
                        logging.info(f"Nombre d'unités chargées: {len(self.units)}")
                        return len(self.units)
                    else:
                        logging.warning("Pas de 'unit_list' trouvée dans le JSON")
                        return 0
                        
                except json.JSONDecodeError as e:
                    logging.error(f"Erreur de décodage JSON: {str(e)}")
                    return 0
        
        except Exception as e:
            logging.error(f"Erreur lors du chargement du fichier: {str(e)}")
            raise Exception(f"Erreur lors du chargement du fichier: {str(e)}")

    def _add_unit(self, unit_data):
        """Ajoute une unité si elle est valide"""
        try:
            if 'unit_id' in unit_data and 'wizard_id' in unit_data:
                # Stocker le wizard_id du premier monstre
                if self.current_wizard_id is None:
                    self.current_wizard_id = unit_data['wizard_id']
                    logging.info(f"Premier wizard_id trouvé: {self.current_wizard_id}")
                
                # Ne garder que les monstres du même compte
                if unit_data['wizard_id'] == self.current_wizard_id:
                    unit = Unit(unit_data)
                    self.units.append(unit)
                    logging.debug(f"Unité ajoutée: ID {unit.unit_id}, Level {unit.unit_level}, Stars {unit.stars}")
        except Exception as e:
            logging.error(f"Erreur lors de l'ajout d'une unité: {str(e)}")

    def get_unit_by_id(self, unit_id):
        """Récupère une unité par son ID"""
        return next((unit for unit in self.units if unit.unit_id == unit_id), None)

    def get_units_by_stars(self, stars):
        """Récupère toutes les unités avec un nombre spécifique d'étoiles"""
        return [unit for unit in self.units if unit.stars == stars]

    def get_units_by_level(self, level):
        """Récupère toutes les unités d'un niveau spécifique"""
        return [unit for unit in self.units if unit.unit_level == level]

    def get_units_by_attribute(self, attribute):
        """Récupère toutes les unités d'un attribut spécifique"""
        return [unit for unit in self.units if unit.attribute == attribute]

    def get_stats(self):
        """Retourne des statistiques sur les unités chargées"""
        if not self.units:
            return "Aucune unité chargée"
            
        stats = {
            "total": len(self.units),
            "par_étoiles": {},
            "par_niveau": {},
            "par_attribut": {}
        }
        
        for unit in self.units:
            # Comptage par étoiles
            stars = unit.stars
            stats["par_étoiles"][stars] = stats["par_étoiles"].get(stars, 0) + 1
            
            # Comptage par niveau
            level = unit.unit_level
            stats["par_niveau"][level] = stats["par_niveau"].get(level, 0) + 1
            
            # Comptage par attribut
            attr = unit.attribute
            stats["par_attribut"][attr] = stats["par_attribut"].get(attr, 0) + 1
        
        return stats