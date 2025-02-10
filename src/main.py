import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import logging
from unit_manager import UnitManager
from RuneCircleWidget import RuneCircleWidget
from ArteWidget import ArteWidget

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.unit_manager = UnitManager()
        self.setup_gui()
        
    def setup_gui(self):
        self.title("Gestionnaire d'Unités")
        self.geometry("1200x800")
        
        self._create_frames()
        self._setup_controls()
        self._setup_unit_selector()
        self._setup_details_area()
        
    def _create_frames(self):
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(expand=True, fill='both', padx=10, pady=5)
        
        self.control_frame = tk.Frame(self.main_frame)
        self.control_frame.pack(fill='x', pady=5)
        
        self.stats_frame = tk.LabelFrame(self.main_frame, text="Statistiques", padx=5, pady=5)
        self.stats_frame.pack(fill='x', pady=5)
        
        self.selection_frame = tk.Frame(self.main_frame)
        self.selection_frame.pack(fill='x', pady=5)
        
        self.details_frame = tk.Frame(self.main_frame)
        self.details_frame.pack(expand=True, fill='both', pady=5)
        
    def _setup_controls(self):
        tk.Button(self.control_frame, text="Charger JSON", 
                 command=self.load_json).pack(side=tk.LEFT, padx=5)
        
        self.show_max_only = tk.BooleanVar(value=True)
        tk.Checkbutton(self.control_frame, text="Unités 6★ niveau 40 uniquement", 
                      variable=self.show_max_only, 
                      command=self.update_unit_selector).pack(side=tk.LEFT, padx=5)
        
        self.info_label = tk.Label(self.control_frame, text="")
        self.info_label.pack(side=tk.LEFT, padx=10)
        
    def _setup_unit_selector(self):
        tk.Label(self.selection_frame, text="Sélectionner une unité:").pack(side=tk.LEFT, padx=5)
        self.unit_selector = ttk.Combobox(self.selection_frame, width=50)
        self.unit_selector.pack(side=tk.LEFT, padx=5)
        self.unit_selector.bind('<<ComboboxSelected>>', self.on_unit_selected)
        
    def _setup_details_area(self):
        self.info_frame = tk.Frame(self.details_frame)
        self.info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(self.info_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.details_text = tk.Text(self.info_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        self.details_text.pack(expand=True, fill='both')
        scrollbar.config(command=self.details_text.yview)
        
        right_frame = tk.Frame(self.details_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.rune_widget = RuneCircleWidget(right_frame)
        self.rune_widget.pack(fill=tk.BOTH, expand=True)
        
        self.arte_widget = ArteWidget(right_frame)
        self.arte_widget.pack(fill=tk.BOTH, expand=True)
        
    def load_json(self):
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers JSON", "*.json")])
        if not file_path:
            return
            
        try:
            num_units = self.unit_manager.load_from_json(file_path)
            if num_units > 0:
                self.update_unit_selector()
                self.update_stats()
                self.info_label.config(
                    text=f"Compte: {self.unit_manager.current_wizard_id} - {num_units} unités chargées")
            else:
                messagebox.showwarning("Attention", "Aucune unité n'a été chargée du fichier.")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
            logging.error(f"Erreur lors du chargement du JSON: {e}")
            
    def update_unit_selector(self):
        units = []
        display_units = (self.unit_manager.get_max_level_units() 
                        if self.show_max_only.get() else self.unit_manager.units)
        
        for unit in display_units:
            stars = "★" * unit.stars
            unit_str = f"ID: {unit.unit_id} - Monster ID: {unit.unit_master_id} - Niveau: {unit.unit_level} - {stars}"
            units.append((unit_str, unit.unit_id))
        
        self.unit_selector['values'] = [u[0] for u in units]
        if units:
            self.unit_selector.set(units[0][0])
            self.display_unit_details(units[0][1])
            filtered_count = len(display_units)
            total_count = len(self.unit_manager.units)
            self.info_label.config(
                text=f"Compte: {self.unit_manager.current_wizard_id} - "
                     f"Affichées: {filtered_count}/{total_count} unités")
                     
    def on_unit_selected(self, event):
        selection = self.unit_selector.get()
        if selection:
            unit_id = int(selection.split(" - ")[0].split(": ")[1])
            self.display_unit_details(unit_id)
            
    def display_unit_details(self, unit_id):
        unit = self.unit_manager.get_unit_by_id(unit_id)
        if not unit:
            logging.warning(f"Unité non trouvée: {unit_id}")
            return
            
        self._display_unit_info(unit)
        self._update_equipment_widgets(unit)
        
    def _display_unit_info(self, unit):
        self.details_text.delete(1.0, tk.END)
        
        # Informations principales
        self.details_text.insert(tk.END, "Informations principales:\n")
        main_info = {
            'ID': unit.unit_id,
            'Nom': unit.name,
            'Famille': unit.family,
            'Élément': unit.element,
            'Type': unit.type,
            'Niveau': unit.unit_level,
            'Étoiles': '★' * unit.stars
        }
        for key, value in main_info.items():
            self.details_text.insert(tk.END, f"{key}: {value}\n")
        
        # Stats
        self.details_text.insert(tk.END, "\nStats:\n")
        stats_order = ['hp', 'atk', 'def', 'spd', 'critical_rate', 
                      'critical_damage', 'resist', 'accuracy']
        for stat in stats_order:
            value = unit.stats[stat]
            if stat in ['resist', 'accuracy', 'critical_rate', 'critical_damage']:
                self.details_text.insert(tk.END, f"{stat.replace('_', ' ').title()}: {value}%\n")
            else:
                self.details_text.insert(tk.END, f"{stat.upper()}: {value}\n")
        
        # Skills
        if unit.skills:
            self.details_text.insert(tk.END, "\nCompétences:\n")
            for skill in unit.skills:
                self.details_text.insert(tk.END, f"ID {skill[0]}: Niveau {skill[1]}\n")
    def _update_equipment_widgets(self, unit):
        if hasattr(unit, 'runes'):
            self.rune_widget.draw_items(unit.runes)
        else:
            logging.warning(f"Pas de runes pour l'unité {unit.unit_id}")
            self.rune_widget.draw_items([])
            
        if hasattr(unit, 'artifacts'):
            self.arte_widget.draw_items(unit.artifacts)
        else:
            logging.warning(f"Pas d'artefacts pour l'unité {unit.unit_id}")
            self.arte_widget.draw_items([])
            
    def update_stats(self):
        for widget in self.stats_frame.winfo_children():
            widget.destroy()
            
        stats = self.unit_manager.get_stats()
        if isinstance(stats, str):
            tk.Label(self.stats_frame, text=stats).pack()
            return
            
        tk.Label(self.stats_frame, text=f"Total: {stats['total']} unités").pack(side=tk.LEFT, padx=10)
        
        stars_text = "Par étoiles: " + ", ".join(f"{k}★: {v}" 
                    for k, v in sorted(stats['par_étoiles'].items()))
        tk.Label(self.stats_frame, text=stars_text).pack(side=tk.LEFT, padx=10)
        
        attr_text = "Par attribut: " + ", ".join(f"{k}: {v}" 
                   for k, v in sorted(stats['par_attribut'].items()))
        tk.Label(self.stats_frame, text=attr_text).pack(side=tk.LEFT, padx=10)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                       format='%(asctime)s - %(levelname)s - %(message)s')
    app = Application()
    app.mainloop()