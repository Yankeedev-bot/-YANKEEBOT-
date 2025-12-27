# 🚀 DÉMARRAGE RAPIDE - SYZYGY BOT

**Par ★LORD‡YANKEE†HELLS ★** 💝

---

## ⚡ Installation en 3 Minutes

### 📱 Sur Termux (Android)

```bash
# 1. Installation automatique
curl -o install.sh https://ton-site.com/install.sh
chmod +x install.sh
./install.sh

# 2. Copier les fichiers
cd ~/syzygy-bot
# Copie tous les fichiers .py ici

# 3. Lancer le bot
python bot.py
```

### 🐧 Sur Kali Linux

```bash
# 1. Installation automatique
wget https://ton-site.com/install.sh
chmod +x install.sh
./install.sh

# 2. Copier les fichiers
cd ~/syzygy-bot
# Copie tous les fichiers .py ici

# 3. Lancer le bot
python3 bot.py
```

---

## 📦 Liste des Fichiers Nécessaires

✅ `bot.py` - Fichier principal  
✅ `config.py` - Configuration  
✅ `utils.py` - Utilitaires  
✅ `commands.py` - Gestionnaire  
✅ `commands_utils.py` - Commandes utils  
✅ `commands_economy.py` - Économie  
✅ `commands_gacha.py` - Gacha  
✅ `commands_fun.py` - Fun  
✅ `commands_anime.py` - Anime  

---

## ⚙️ Configuration Initiale

Au premier lancement, entre :

```
📧 Email Facebook : ton_email@gmail.com
🔑 Mot de passe : ton_password
🤖 Nom du bot : Syzygy
👤 Ton nom : [Appuie sur Entrée pour ★LORD‡YANKEE†HELLS ★]
⚡ Préfixe : #
🖼️ Image menu : /sdcard/menu.jpg (optionnel)
```

---

## 🎮 Commandes Principales

```
#menu      - Menu complet
#ping      - Test
#balance   - Voir ses coins
#daily     - Récompense quotidienne
#work      - Travailler
#claim     - Réclamer un personnage
#harem     - Voir sa collection
#calin     - Faire un câlin
```

---

## 🖼️ Ajouter une Image de Menu

### Option 1 : Image Locale
```bash
cp /sdcard/Download/mon_image.jpg ~/syzygy-bot/menu.jpg
```

Puis dans `config.json` :
```json
"menu_image": "menu.jpg"
```

### Option 2 : Image en Ligne
```json
"menu_image": "https://i.imgur.com/ton_image.jpg"
```

---

## 🔧 Lancer en Arrière-Plan

### Termux
```bash
nohup python bot.py > bot.log 2>&1 &
```

### Kali (avec screen)
```bash
screen -S syzygy
python3 bot.py
# Ctrl+A puis D pour détacher
```

---

## 🐛 Problèmes Courants

### ❌ Erreur : Module not found
```bash
pip install fbchat requests
```

### ❌ Erreur : No module named 'config'
```bash
# Vérifie que tous les .py sont dans le même dossier
ls -la
```

### ❌ Bot ne répond pas
```bash
# Vérifie le préfixe (défaut: #)
# Envoie: #ping
```

---

## 📞 Support

🌐 Site : https://nekos.club  
📢 Telegram : https://t.me/nekosclub  
📧 Email : support@nekos.club

---

## 💝 Crédits

**Créé avec ❤️ par ★LORD‡YANKEE†HELLS ★**

🇫🇷 Version Française • 2024 • MIT License

---

**C'est tout ! Profite bien de ton bot ! 🎉**
