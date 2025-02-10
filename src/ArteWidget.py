import logging
from baseWidget import EquipmentWidget

class ArteWidget(EquipmentWidget):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.canvas.configure(width=300, height=150)
        
    def _get_details_title(self) -> str:
        return "Détails de l'artefact"
        
    def draw_items(self, artifacts: list):
        self.items = self._validate_items(artifacts)
        self._clear_canvas()
        
        try:
            self._draw_artifacts()
        except Exception as e:
            logging.error(f"Erreur dessin des artefacts: {e}")
            self._show_error("Erreur d'affichage")
            
    def _draw_artifacts(self):
        """Dessine les emplacements d'artefacts"""
        positions = [(100, 75), (200, 75)]
        
        for i, pos in enumerate(positions):
            self._draw_artifact_slot(i, pos)
                
    def _draw_artifact_slot(self, index: int, pos: tuple):
        """Dessine un emplacement d'artefact"""
        x, y = pos
        slot_number = index + 1
        artifact = next((a for a in self.items 
                     if a.get('slot') == slot_number), None)
        
        if self._is_valid_artifact(artifact):
            self._draw_filled_slot(x, y, slot_number, artifact)
        else:
            self._draw_empty_slot(x, y, slot_number)
            
    def _is_valid_artifact(self, artifact: dict) -> bool:
        """Vérifie si un artefact est valide"""
        return (artifact and all(k in artifact for k in 
                ['slot', 'type', 'primary_effect']))
                
    def _draw_filled_slot(self, x: int, y: int, slot: int, artifact: dict):
        """Dessine un emplacement avec artefact"""
        self.canvas.create_oval(
            x-30, y-30, x+30, y+30,
            fill="purple", outline="darkviolet",
            tags=f"artifact_{slot}"
        )
        self.canvas.create_text(
            x, y,
            text=str(slot),
            font=("Arial", 14, "bold"),
            fill="white"
        )
        self.canvas.create_text(
            x, y+40,
            text=artifact['type'],
            font=("Arial", 10)
        )
                
    def _draw_empty_slot(self, x: int, y: int, slot: int):
        """Dessine un emplacement vide"""
        self.canvas.create_oval(
            x-30, y-30, x+30, y+30,
            outline="gray",
            tags=f"artifact_{slot}"
        )
        self.canvas.create_text(
            x, y,
            text=str(slot),
            font=("Arial", 14),
            fill="gray"
        )
            
    def _on_click(self, event):
        """Gère le clic sur un artefact"""
        x, y = event.x, event.y
        items = self.canvas.find_closest(x, y)
        if not items:
            return
            
        tags = self.canvas.gettags(items[0])
        for tag in tags:
            if not tag.startswith("artifact_"):
                continue
                
            slot_number = int(tag.split("_")[1])
            artifact = next((a for a in self.items 
                         if a.get('slot') == slot_number), None)
            if artifact:
                self.show_item_details(artifact)
                break
                
    def show_item_details(self, artifact: dict):
        """Affiche les détails d'un artefact"""
        self.details_text.delete(1.0, "end")
        
        # Informations de base
        self.details_text.insert("end", f"Artefact Slot {artifact['slot']}\n")
        self.details_text.insert("end", f"Type: {artifact['type']}\n\n")
        
        # Effets
        if artifact.get('primary_effect'):
            self.details_text.insert("end", "Effet Principal:\n")
            self.details_text.insert("end", f"{artifact['primary_effect']}\n\n")
        
        if artifact.get('secondary_effects'):
            self.details_text.insert("end", "Effets Secondaires:\n")
            for effect in artifact['secondary_effects']:
                self.details_text.insert("end", f"- {effect}\n")