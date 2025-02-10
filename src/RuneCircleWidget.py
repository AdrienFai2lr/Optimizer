from math import cos, sin, pi
import logging
from baseWidget import EquipmentWidget

class RuneCircleWidget(EquipmentWidget):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.canvas.configure(width=400, height=400)
        
    def _get_details_title(self) -> str:
        return "Détails de la rune"
        
    def draw_items(self, runes: list):
        self.items = self._validate_items(runes)
        self._clear_canvas()
        
        try:
            self._draw_rune_circle()
        except Exception as e:
            logging.error(f"Erreur dessin des runes: {e}")
            self._show_error("Erreur d'affichage")
            
    def _draw_rune_circle(self):
        """Dessine le cercle de runes"""
        center_x, center_y = 200, 200
        radius = 150
        
        # Cercle de base
        self.canvas.create_oval(
            center_x-radius, center_y-radius,
            center_x+radius, center_y+radius,
            outline="gray", width=2
        )
        
        # Dessine chaque emplacement
        for i in range(6):
            self._draw_rune_slot(i, center_x, center_y, radius)
                
    def _draw_rune_slot(self, index: int, cx: int, cy: int, radius: int):
        """Dessine un emplacement de rune"""
        angle = (index - 1) * (2 * pi / 6)
        x = cx + radius * sin(angle)
        y = cy - radius * cos(angle)
        
        slot_number = index + 1
        rune = next((r for r in self.items if r.get('slot') == slot_number), None)
        
        if self._is_valid_rune(rune):
            self._draw_filled_slot(x, y, slot_number, rune)
        else:
            self._draw_empty_slot(x, y, slot_number)
            
    def _is_valid_rune(self, rune: dict) -> bool:
        """Vérifie si une rune est valide"""
        return (rune and all(k in rune for k in 
                ['slot', 'set_id', 'rank', 'stars']))
                
    def _draw_filled_slot(self, x: int, y: int, slot: int, rune: dict):
        """Dessine un emplacement avec rune"""
        self.canvas.create_oval(
            x-25, y-25, x+25, y+25,
            fill="gold", outline="brown",
            tags=f"rune_{slot}"
        )
        self.canvas.create_text(
            x, y,
            text=str(slot),
            font=("Arial", 12, "bold"),
            fill="black"
        )
        self.canvas.create_text(
            x, y+35,
            text=f"Set {rune['set_id']}",
            font=("Arial", 8)
        )
                
    def _draw_empty_slot(self, x: int, y: int, slot: int):
        """Dessine un emplacement vide"""
        self.canvas.create_oval(
            x-25, y-25, x+25, y+25,
            outline="gray",
            tags=f"rune_{slot}"
        )
        self.canvas.create_text(
            x, y,
            text=str(slot),
            font=("Arial", 12),
            fill="gray"
        )
            
    def _on_click(self, event):
        """Gère le clic sur une rune"""
        x, y = event.x, event.y
        items = self.canvas.find_closest(x, y)
        if not items:
            return
            
        tags = self.canvas.gettags(items[0])
        for tag in tags:
            if not tag.startswith("rune_"):
                continue
                
            slot_number = int(tag.split("_")[1])
            rune = next((r for r in self.items 
                     if r.get('slot') == slot_number), None)
            if rune:
                self.show_item_details(rune)
                break
                
    def show_item_details(self, rune: dict):
        """Affiche les détails d'une rune"""
        self.details_text.delete(1.0, "end")
        
        # Informations de base
        self.details_text.insert("end", f"Rune Slot {rune['slot']}\n")
        self.details_text.insert("end", f"{'★' * rune['stars']}\n\n")
        
        # Set et rang
        self.details_text.insert("end", f"Set: {rune['set_id']}\n")
        self.details_text.insert("end", f"Rang: {rune['rank']}\n\n")
        
        # Effets
        if rune.get('primary_effect'):
            self.details_text.insert("end", "Effet Principal:\n")
            self.details_text.insert("end", f"{rune['primary_effect']}\n\n")
        
        if rune.get('secondary_effects'):
            self.details_text.insert("end", "Effets Secondaires:\n")
            for effect in rune['secondary_effects']:
                self.details_text.insert("end", f"- {effect}\n")