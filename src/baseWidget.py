import tkinter as tk
import logging
from abc import ABC, abstractmethod

class EquipmentWidget(ABC, tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.items = []
        self.selected_item = None
        self._setup_base_widget()
        
    def _setup_base_widget(self):
        """Configuration de base commune aux widgets"""
        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.pack(side=tk.LEFT, padx=2, pady=2)
        
        self.details_frame = tk.LabelFrame(self, text=self._get_details_title())
        self.details_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.details_text = tk.Text(self.details_frame, wrap=tk.WORD, width=30, height=15)
        self.details_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.canvas.bind('<Button-1>', self._on_click)
        
    @abstractmethod
    def _get_details_title(self) -> str:
        """Retourne le titre du cadre de détails"""
        pass
        
    @abstractmethod
    def draw_items(self, items: list):
        """Dessine les équipements"""
        pass
        
    @abstractmethod
    def _on_click(self, event):
        """Gère le clic sur un équipement"""
        pass
        
    @abstractmethod
    def show_item_details(self, item: dict):
        """Affiche les détails d'un équipement"""
        pass
        
    def _validate_items(self, items) -> list:
        """Valide la liste d'équipements"""
        if not isinstance(items, list):
            logging.error(f"Items invalides: {items}")
            return []
        return items
        
    def _clear_canvas(self):
        """Efface le canvas"""
        self.canvas.delete("all")
        
    def _show_error(self, message: str):
        """Affiche un message d'erreur sur le canvas"""
        self.canvas.create_text(
            self.canvas.winfo_width()//2,
            self.canvas.winfo_height()//2,
            text=message,
            fill="red",
            font=("Arial", 14, "bold")
        )