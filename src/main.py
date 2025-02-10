# main.py
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from unit_manager import UnitManager
import logging

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.unit_manager = UnitManager()
        self.setup_gui()
    
    def setup_gui(self):
        self.title("Gestionnaire d'Unités")
        self.geometry("800x600")
        
        # Frame principale
        main_frame = tk.Frame(self)
        main_frame.pack(expand=True, fill='both', padx=10, pady=5)
        
        # Frame pour les contrôles
        control_frame = tk.Frame(main_frame)
        control_frame.pack(fill='x', pady=5)
        
        # Bouton de chargement
        tk.Button(control_frame, text="Charger JSON", command=self.load_json).pack(side=tk.LEFT, padx=5)
        
        # Labels d'information
        self.info_label = tk.Label(control_frame, text="")
        self.info_label.pack(side=tk.LEFT, padx=10)
        
        # Frame pour les statistiques
        self.stats_frame = tk.LabelFrame(main_frame, text="Statistiques", padx=5, pady=5)
        self.stats_frame.pack(fill='x', pady=5)
        
        # Frame pour la sélection et l'affichage
        selection_frame = tk.Frame(main_frame)
        selection_frame.pack(fill='x', pady=5)
        
        # Label et Combobox pour la sélection d'unité
        tk.Label(selection_frame, text="Sélectionner une unité:").pack(side=tk.LEFT, padx=5)
        self.unit_selector = ttk.Combobox(selection_frame, width=50)
        self.unit_selector.pack(side=tk.LEFT, padx=5)
        self.unit_selector.bind('<<ComboboxSelected>>', self.on_unit_selected)
        
        # Zone de détails
        details_frame = tk.Frame(main_frame)
        details_frame.pack(expand=True, fill='both', pady=5)
        
        # Scrollbar et Text pour les détails
        scrollbar = tk.Scrollbar(details_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.details_text = tk.Text(details_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        self.details_text.pack(expand=True, fill='both')
        scrollbar.config(command=self.details_text.yview)
    
    def load_json(self):
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers JSON", "*.json")])
        if not file_path:
            return
            
        try:
            num_units = self.unit_manager.load_from_json(file_path)
            if num_units > 0:
                self.update_unit_selector()
                self.update_stats()
                self.info_label.config(text=f"Compte: {self.unit_manager.current_wizard_id} - {num_units} unités chargées")
            else:
                messagebox.showwarning("Attention", "Aucune unité n'a été chargée du fichier.")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
    
    def update_unit_selector(self):
        """Met à jour la liste déroulante des unités"""
        units = []
        for unit in self.unit_manager.units:
            # Format: "ID: xxx - Monster ID: xxx - Niveau: xx - ★★★★★★"
            stars = "★" * unit.stars
            unit_str = f"ID: {unit.unit_id} - Monster ID: {unit.unit_master_id} - Niveau: {unit.unit_level} - {stars}"
            units.append((unit_str, unit.unit_id))
        
        self.unit_selector['values'] = [u[0] for u in units]
        if units:
            self.unit_selector.set(units[0][0])
            self.display_unit_details(units[0][1])
    
    def on_unit_selected(self, event):
        """Gère la sélection d'une unité dans la liste déroulante"""
        selection = self.unit_selector.get()
        if selection:
            unit_id = int(selection.split(" - ")[0].split(": ")[1])
            self.display_unit_details(unit_id)
    
    def display_unit_details(self, unit_id):
        """Affiche les détails de l'unité sélectionnée"""
        unit = self.unit_manager.get_unit_by_id(unit_id)
        if not unit:
            return
            
        self.details_text.delete(1.0, tk.END)
        
        # Informations principales
        self.details_text.insert(tk.END, "Informations principales:\n")
        self.details_text.insert(tk.END, f"- ID: {unit.unit_id}\n")
        self.details_text.insert(tk.END, f"- Monster ID: {unit.unit_master_id}\n")
        self.details_text.insert(tk.END, f"- Niveau: {unit.unit_level}\n")
        self.details_text.insert(tk.END, f"- Étoiles: {'★' * unit.stars}\n")
        self.details_text.insert(tk.END, f"- Attribut: {unit.attribute}\n")
        
        # Stats
        self.details_text.insert(tk.END, "\nStats:\n")
        self.details_text.insert(tk.END, f"- HP: {unit.stats['hp']} (base: {unit.stats['hp_base']})\n")
        self.details_text.insert(tk.END, f"- ATK: {unit.stats['atk']}\n")
        self.details_text.insert(tk.END, f"- DEF: {unit.stats['def']}\n")
        self.details_text.insert(tk.END, f"- SPD: {unit.stats['spd']}\n")
        self.details_text.insert(tk.END, f"- Résistance: {unit.stats['resist']}%\n")
        self.details_text.insert(tk.END, f"- Précision: {unit.stats['accuracy']}%\n")
        self.details_text.insert(tk.END, f"- Taux Critique: {unit.stats['critical_rate']}%\n")
        self.details_text.insert(tk.END, f"- Dégâts Critiques: {unit.stats['critical_damage']}%\n")
        
        # Skills
        self.details_text.insert(tk.END, "\nCompétences:\n")
        for skill in unit.skills:
            self.details_text.insert(tk.END, f"- ID {skill[0]}: Niveau {skill[1]}\n")
        
        # Runes
        if unit.runes:
            self.details_text.insert(tk.END, "\nRunes:\n")
            for rune in unit.runes:
                self.details_text.insert(tk.END, 
                    f"- Slot {rune['slot']}: Set {rune['set_id']}, "
                    f"{rune['stars']}★, Rang {rune['rank']}\n")
        
        # Artefacts
        if unit.artifacts:
            self.details_text.insert(tk.END, "\nArtefacts:\n")
            for artifact in unit.artifacts:
                self.details_text.insert(tk.END, 
                    f"- Slot {artifact['slot']}: Type {artifact['type']}\n")
    
    def update_stats(self):
        """Met à jour l'affichage des statistiques"""
        for widget in self.stats_frame.winfo_children():
            widget.destroy()
            
        stats = self.unit_manager.get_stats()
        if isinstance(stats, str):
            tk.Label(self.stats_frame, text=stats).pack()
            return
            
        # Afficher les statistiques
        tk.Label(self.stats_frame, text=f"Total: {stats['total']} unités").pack(side=tk.LEFT, padx=10)
        
        # Par étoiles
        stars_text = "Par étoiles: " + ", ".join(f"{k}★: {v}" for k, v in sorted(stats['par_étoiles'].items()))
        tk.Label(self.stats_frame, text=stars_text).pack(side=tk.LEFT, padx=10)
        
        # Par attribut
        attr_text = "Par attribut: " + ", ".join(f"Type {k}: {v}" for k, v in sorted(stats['par_attribut'].items()))
        tk.Label(self.stats_frame, text=attr_text).pack(side=tk.LEFT, padx=10)

if __name__ == "__main__":
    app = Application()
    app.mainloop()