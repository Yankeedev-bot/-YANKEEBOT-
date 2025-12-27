"""
config.py - Gestion de la configuration du bot
"""

import os
import json


def load_config():
    """Charger la configuration depuis config.json"""
    config_file = "config.json"
    default_config = {
        "email": "",
        "password": "",
        "bot_name": "Syzygy",
        "owner": "★LORD‡YANKEE†HELLS ★",
        "prefix": "#",
        "menu_image": "",
        "language": "fr"
    }
    
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Erreur de lecture du config : {e}")
            return default_config
    
    return default_config


def save_config(config):
    """Sauvegarder la configuration dans config.json"""
    try:
        with open('config.json', 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        print("✅ Configuration sauvegardée !")
        return True
    except Exception as e:
        print(f"❌ Erreur de sauvegarde : {e}")
        return False


def setup_first_time():
    """Configuration initiale du bot"""
    print("╔═══════════════════════════════════════════╗")
    print("║   🔐 CONFIGURATION SYZYGY BOT 🇫🇷        ║")
    print("╚═══════════════════════════════════════════╝\n")
    
    config = {}
    
    # Email et mot de passe
    config['email'] = input("📧 Email Facebook : ").strip()
    config['password'] = input("🔑 Mot de passe : ").strip()
    
    # Nom du bot
    bot_name = input("🤖 Nom du bot (Syzygy) : ").strip()
    config['bot_name'] = bot_name if bot_name else "Syzygy"
    
    # Propriétaire
    owner = input("👤 Ton nom (★LORD‡YANKEE†HELLS ★) : ").strip()
    config['owner'] = owner if owner else "★LORD‡YANKEE†HELLS ★"
    
    # Préfixe
    prefix = input("⚡ Préfixe (#) : ").strip()
    config['prefix'] = prefix if prefix else "#"
    
    # Image du menu
    print("\n📸 Image du menu (optionnel) :")
    print("Exemples :")
    print("  - /sdcard/menu.jpg")
    print("  - https://i.imgur.com/ton_image.jpg")
    print("  - Laisse vide pour aucune image")
    config['menu_image'] = input("🖼️  Chemin de l'image : ").strip()
    
    # Langue
    config['language'] = 'fr'
    
    # Sauvegarder
    save_config(config)
    
    return config


def get_config_value(key, default=None):
    """Obtenir une valeur de configuration"""
    config = load_config()
    return config.get(key, default)


def update_config_value(key, value):
    """Mettre à jour une valeur de configuration"""
    config = load_config()
    config[key] = value
    return save_config(config)
