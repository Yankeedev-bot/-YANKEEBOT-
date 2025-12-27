# 🤖 Syzygy Bot Premium - Structure Modulaire

**Bot Facebook Messenger en français 🇫🇷**  
Développé par ★LORD‡YANKEE†HELLS ★ ❤️

---

## 📁 Structure du Projet

```
syzygy-bot/
│
├── bot.py                      # ⭐ Fichier principal à exécuter
├── config.py                   # 🔧 Gestion de la configuration
├── utils.py                    # 🛠️ Fonctions utilitaires
│
├── commands.py                 # 📋 Gestionnaire principal des commandes
├── commands_utils.py           # 💬 Commandes utilitaires (menu, ping, info)
├── commands_economy.py         # 💰 Commandes d'économie (coins, travail)
├── commands_gacha.py           # 🎲 Commandes gacha (claim, harem)
├── commands_fun.py             # 🎉 Commandes fun (stickers, téléchargements)
├── commands_anime.py           # 🎭 Commandes réactions anime
│
├── config.json                 # ⚙️ Configuration (créé automatiquement)
├── menu.jpg                    # 🖼️ Image du menu (optionnel)
└── README.md                   # 📖 Ce fichier
```

---

## 🚀 Installation Rapide

### 1️⃣ Installer les dépendances

**Sur Termux :**
```bash
pkg update && pkg upgrade -y
pkg install python git -y
pip install fbchat requests
```

**Sur Kali Linux :**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
pip3 install fbchat requests
```

### 2️⃣ Télécharger le bot

```bash
# Créer le dossier
mkdir ~/syzygy-bot
cd ~/syzygy-bot

# Télécharger tous les fichiers
# (Copie chaque fichier .py dans ce dossier)
```

### 3️⃣ Lancer le bot

```bash
python bot.py
```

Lors du premier lancement, le bot va te demander :
- 📧 Email Facebook
- 🔑 Mot de passe
- 🤖 Nom du bot
- 👤 Ton nom
- ⚡ Préfixe des commandes
- 🖼️ Chemin de l'image du menu

---

## 📦 Description des Fichiers

### `bot.py` - Fichier Principal ⭐
- Point d'entrée du programme
- Gère la connexion à Facebook
- Écoute et traite les messages
- **C'est le fichier à exécuter !**

### `config.py` - Configuration 🔧
- Charge et sauvegarde `config.json`
- Gère la configuration initiale
- Fonctions : `load_config()`, `save_config()`, `setup_first_time()`

### `utils.py` - Utilitaires 🛠️
- Fonctions utilitaires communes
- Affichage du banner
- Envoi d'images avec messages
- Formatage de données

### `commands.py` - Gestionnaire de Commandes 📋
- Classe `CommandHandler`
- Enregistre toutes les commandes
- Route les commandes vers les bons modules

### `commands_utils.py` - Commandes Utilitaires 💬
- Menu principal
- Ping, status, botinfo
- Commandes d'information

### `commands_economy.py` - Économie 💰
- Balance (voir ses coins)
- Daily (récompense quotidienne)
- Work (travailler)
- Crime (commettre un crime)
- Steal (voler quelqu'un)

### `commands_gacha.py` - Gacha 🎲
- Claim (réclamer un personnage)
- Harem (voir sa collection)
- Roll (obtenir un personnage aléatoire)

### `commands_fun.py` - Fun 🎉
- Sticker (créer des stickers)
- Toimage (convertir sticker en image)
- Play (télécharger musique YouTube)
- TikTok, Facebook, Instagram (téléchargements)

### `commands_anime.py` - Réactions Anime 🎭
- Hug (câlin)
- Kiss (bisou)
- Pat (caresser)
- Slap (gifler)
- Cry, Laugh, Dance...

---

## ⚙️ Configuration (`config.json`)

Exemple de fichier créé automatiquement :

```json
{
  "email": "ton_email@gmail.com",
  "password": "ton_mot_de_passe",
  "bot_name": "Syzygy",
  "owner": "LightningNeko",
  "prefix": "#",
  "menu_image": "/sdcard/menu.jpg",
  "language": "fr"
}
```

### Modifier la configuration

Tu peux éditer directement `config.json` :

```bash
nano config.json
```

Ou utiliser Python :

```python
from config import update_config_value

update_config_value('prefix', '!')
update_config_value('bot_name', 'MonBot')
```

---

## 🎨 Personnalisation

### Ajouter une Nouvelle Commande

**Exemple : Ajouter une commande `#joke` (blague)**

1. **Dans `commands_fun.py`**, ajoute :

```python
def joke(self, args, author_id, thread_id):
    """Raconter une blague"""
    jokes = [
        "Pourquoi les plongeurs plongent-ils toujours en arrière ?\nParce que sinon ils tombent dans le bateau !",
        "Qu'est-ce qu'un crocodile qui surveille la pharmacie ?\nUn Lacoste garde !"
    ]
    import random
    return f"""╭┈ ↷ Blague
│ ✐ 😂 {random.choice(jokes)}
╰─────────────────"""
```

2. **Dans `commands.py`**, dans `_register_commands()`, ajoute :

```python
f"{p}joke": self.fun.joke,
f"{p}blague": self.fun.joke,
```

3. **Redémarre le bot !**

### Changer le Style des Réponses

Toutes les réponses utilisent ce format :

```python
f"""╭┈ ↷ Titre
│ ✐ Ligne 1
│ ✐ Ligne 2
╰─────────────────"""
```

Tu peux le modifier dans chaque fichier `commands_*.py`

---

## 🔧 Utilisation Avancée

### Exécuter en Arrière-Plan

**Termux :**
```bash
nohup python bot.py > bot.log 2>&1 &
```

**Kali avec screen :**
```bash
screen -S syzygy
python bot.py
# Ctrl+A puis D pour détacher
# screen -r syzygy pour réattacher
```

### Voir les Logs

```bash
tail -f bot.log
```

### Arrêter le Bot

```bash
pkill -f bot.py
```

---

## 🐛 Dépannage

### Erreur : Module not found

```bash
pip install fbchat requests
```

### Erreur : No module named 'config'

Assure-toi que tous les fichiers `.py` sont dans le même dossier !

```bash
ls -la
# Tu dois voir : bot.py, config.py, commands.py, etc.
```

### Le bot ne répond pas

1. Vérifie qu'il est lancé : `ps aux | grep bot.py`
2. Regarde les logs : `tail -f bot.log`
3. Vérifie le préfixe : par défaut c'est `#`

### Facebook bloque la connexion

1. Utilise un **mot de passe d'application**
2. Crée un **compte Facebook dédié**
3. Active l'**authentification à 2 facteurs**

---

## 📝 Commandes Disponibles

### Utilitaires
- `#menu` - Menu principal avec image
- `#ping` - Test de connexion
- `#status` - État du bot
- `#info` - Informations sur le bot

### Économie
- `#balance` - Voir ses coins
- `#daily` - Récompense quotidienne
- `#work` - Travailler
- `#crime` - Commettre un crime
- `#voler @user` - Voler quelqu'un

### Gacha
- `#claim` - Réclamer un personnage
- `#harem` - Voir sa collection
- `#roll` - Personnage aléatoire

### Fun
- `#sticker` - Créer un sticker
- `#play <chanson>` - Télécharger musique
- `#tiktok <lien>` - Télécharger TikTok
- `#facebook <lien>` - Télécharger Facebook
- `#instagram <lien>` - Télécharger Instagram

### Anime
- `#calin @user` - Faire un câlin
- `#bisou @user` - Faire un bisou
- `#caresser @user` - Caresser
- `#gifle @user` - Gifler
- `#pleurer` - Pleurer
- `#rire` - Rire
- `#danser` - Danser

---

## 🔒 Sécurité

1. ✅ **N'utilise PAS ton compte Facebook personnel**
2. ✅ Crée un **compte dédié** pour le bot
3. ✅ Active l'**authentification à 2 facteurs**
4. ✅ Utilise un **mot de passe d'application**
5. ❌ **Ne partage JAMAIS** ton `config.json`
6. ❌ **Ne publie PAS** tes identifiants sur GitHub

---

## 🆙 Mettre à Jour

Pour mettre à jour un seul fichier :

```bash
cd ~/syzygy-bot

# Sauvegarder l'ancien
cp commands_fun.py commands_fun.py.backup

# Éditer le fichier
nano commands_fun.py

# Redémarrer le bot
pkill -f bot.py
python bot.py
```

---

## 💝 Crédits

**Développé avec ❤️ par ★LORD‡YANKEE†HELLS ★**

- 🌐 Site : https://nekos.club
- 📢 Telegram : https://t.me/nekosclub
- 🐙 GitHub : [@LordYankeeHells](https://github.com/lordyankeehells)

---

## 📄 Licence

MIT License - Libre d'utilisation et de modification

---

## 🆘 Besoin d'Aide ?

1. Lis cette documentation complètement
2. Vérifie les logs : `tail -f bot.log`
3. Cherche l'erreur sur Google
4. Rejoins notre canal Telegram

---

**🚀 Profite bien de ton bot Syzygy ! ✨**
