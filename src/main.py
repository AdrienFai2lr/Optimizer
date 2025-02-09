import tkinter as tk
from tkinter import messagebox, filedialog
import json
from game_data import GameData  # Assurez-vous que GameData est correctement défini
from rune import Rune  # Importez la classe Rune

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Paramètres de l'application
        self.title("Affichage des Unités")
        self.geometry("600x400")

        # Zone de texte pour afficher les informations
        self.text_area = tk.Text(self, wrap=tk.WORD, height=20, width=60)
        self.text_area.pack(pady=10)
        
        # Bouton pour charger et afficher les données d'un fichier JSON
        self.load_button = tk.Button(self, text="Charger un fichier JSON", command=self.load_json)
        self.load_button.pack(pady=10)
    
    def load_json(self):
        # Ouvrir une fenêtre pour choisir un fichier JSON
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers JSON", "*.json")])  # Sélectionner un fichier JSON
        
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    json_data = json.load(file)
                
                # Créer une instance de GameData à partir du fichier JSON
                game_data = GameData.from_json(json_data)
                
                # Afficher les informations du compte dans la zone de texte
                self.display_account_info(game_data)
            except FileNotFoundError:
                messagebox.showerror("Erreur", f"Le fichier {file_path} n'a pas été trouvé.")
            except json.JSONDecodeError:
                messagebox.showerror("Erreur", "Erreur de décodage JSON. Veuillez vérifier la structure du fichier.")
            except Exception as e:
                messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
    
    def display_account_info(self, game_data):
        """Affiche les informations du compte dans la zone de texte"""
        self.text_area.delete(1.0, tk.END)  # Efface l'ancienne info
        self.text_area.insert(tk.END, "Informations du compte :\n\n")
        
        # Affichage des informations essentielles de l'unité
        self.text_area.insert(tk.END, f"WIZARD ID: {game_data.unit.wizard_id}\n")
        self.text_area.insert(tk.END, f"Île ID: {game_data.unit.island_id}\n")
        self.text_area.insert(tk.END, f"Position: X={game_data.unit.pos_x}, Y={game_data.unit.pos_y}\n")
        self.text_area.insert(tk.END, f"Niveau: {game_data.unit.unit_level}\n")
        self.text_area.insert(tk.END, f"Classe: {game_data.unit.class_type}\n")
        self.text_area.insert(tk.END, "\n")

        # Affichage des compétences
        self.text_area.insert(tk.END, f"Compétences : \n")
        for skill in game_data.unit.skills:
            self.text_area.insert(tk.END, f"  - Skill ID: {skill[0]}, Niveau: {skill[1]}\n")

        # Affichage des runes
        if game_data.unit.runes:
            self.text_area.insert(tk.END, f"Runes : \n")
            for rune_data in game_data.unit.runes:
                # On suppose que Rune.from_json() est appelé pour chaque rune_data
                rune = Rune.from_json(rune_data)
                self.text_area.insert(tk.END, f"  - Rune ID: {rune.rune_id}, Set: {rune.set_id}, Slot: {rune.slot_no}, Rank: {rune.rank}\n")
                self.text_area.insert(tk.END, f"    Effet principal: {rune.pri_eff}\n")
                self.text_area.insert(tk.END, f"    Effet préfixe: {rune.prefix_eff}\n")
                self.text_area.insert(tk.END, f"    Effets secondaires: {rune.sec_eff}\n")
                self.text_area.insert(tk.END, f"    Extra: {rune.extra}\n")

        # Afficher d'autres données supplémentaires que tu souhaites
        self.text_area.insert(tk.END, f"\nAutres données...\n")

# Lancer l'application
if __name__ == "__main__":
    app = Application()
    app.mainloop()
