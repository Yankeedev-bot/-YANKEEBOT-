#!/usr/bin/env python3
"""
Syzygy Bot Premium - Fichier Principal
Compatible Termux & Kali Linux
Développé par ★LORD‡YANKEE†HELLS ★ ❤️
Version Française 🇫🇷
"""

import os
import sys
from datetime import datetime

try:
    from fbchat import Client, Message, ThreadType
    from fbchat.models import *
except ImportError:
    print("❌ Modules non installés !")
    print("Installation : pip install fbchat requests")
    sys.exit(1)

# Importer les modules du bot
from config import load_config, save_config, setup_first_time
from commands import CommandHandler
from utils import send_with_image, display_banner


class SyzygyBot(Client):
    """Bot Premium Syzygy"""
    
    def __init__(self, email, password, config):
        super().__init__(email, password)
        self.config = config
        self.bot_name = config.get('bot_name', 'Syzygy')
        self.owner = config.get('owner', 'LightningNeko')
        self.prefix = config.get('prefix', '#')
        self.menu_image = config.get('menu_image', '')
        
        # Initialiser le gestionnaire de commandes
        self.cmd_handler = CommandHandler(self)
        
        display_banner(self.bot_name)
        print(f"✅ {self.bot_name} Bot connecté !")
        print(f"👤 UID : {self.uid}")
        print(f"🎯 Préfixe : {self.prefix}")
    
    def onMessage(self, mid=None, author_id=None, message_text=None, 
                  message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        """Gestion des messages reçus"""
        
        # Ignorer ses propres messages
        if author_id == self.uid:
            return
        
        if not message_text:
            return
        
        # Log du message
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] 📨 {message_text[:50]}...")
        
        # Traiter la commande
        parts = message_text.split(maxsplit=1)
        cmd = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        
        # Vérifier si c'est une commande
        if cmd.startswith(self.prefix):
            try:
                response = self.cmd_handler.handle_command(cmd, args, author_id, thread_id)
                
                if response:
                    # Si c'est le menu, envoyer avec image
                    menu_commands = [f"{self.prefix}menu", f"{self.prefix}aide", 
                                   f"{self.prefix}help", f"{self.prefix}commandes"]
                    
                    if cmd in menu_commands and self.menu_image:
                        send_with_image(self, response, self.menu_image, thread_id, thread_type)
                    else:
                        self.send(Message(text=response), thread_id=thread_id, thread_type=thread_type)
                    
                    print(f"[{timestamp}] ✅ Réponse envoyée")
            
            except Exception as e:
                print(f"[{timestamp}] ❌ Erreur : {e}")
                error_msg = f"❌ Erreur lors de l'exécution de la commande : {str(e)}"
                self.send(Message(text=error_msg), thread_id=thread_id, thread_type=thread_type)


def main():
    """Fonction principale"""
    os.system('clear' if os.name != 'nt' else 'cls')
    
    # Charger ou créer la configuration
    config = load_config()
    
    # Configuration initiale si nécessaire
    if not config.get('email') or not config.get('password'):
        config = setup_first_time()
    
    # Démarrer le bot
    try:
        print("\n🔄 Connexion en cours...\n")
        bot = SyzygyBot(config['email'], config['password'], config)
        
        print("\n✨ Syzygy Bot actif !")
        print(f"⚡ Préfixe : {config['prefix']}")
        print(f"📝 Utilise {config['prefix']}menu pour voir les commandes\n")
        print("Appuie sur Ctrl+C pour arrêter\n")
        print("─" * 60)
        
        # Écouter les messages
        bot.listen()
        
    except KeyboardInterrupt:
        print("\n\n👋 Arrêt du bot...")
    except Exception as e:
        print(f"\n❌ Erreur : {e}")
        print("\n💡 Conseils :")
        print("  - Vérifie tes identifiants")
        print("  - Utilise un mot de passe d'application")
        print("  - Vérifie ta connexion internet")


if __name__ == "__main__":
    main()
