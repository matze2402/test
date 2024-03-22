import os
import yaml


def generate_sidebar(folder_path):
    entries = []

    # Durchsuche den Ordner nach Markdown-Dateien
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                entry = {"title": os.path.splitext(file)[0], "url": os.path.join(root, file)}
                entries.append(entry)

    # Erstelle die YAML-Struktur
    sidebar_data = {"entries": entries}

    return sidebar_data

if __name__ == "__main__":
    # Passe den Ordnerpfad entsprechend deiner Struktur an
    folder_path = "filesr"
    
    # Generiere die Sidebar-Daten
    sidebar_data = generate_sidebar(folder_path)

    # Speichere die Sidebar-Daten in einer YAML-Datei
    with open("sidebar_data.yaml", "w") as file:
        yaml.dump(sidebar_data, file)
