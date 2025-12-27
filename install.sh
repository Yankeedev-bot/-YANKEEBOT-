#!/bin/bash

# Script d'installation automatique de Syzygy Bot
# Compatible Termux et Kali Linux
# Par LightningNeko ❤️

clear

echo "╔═══════════════════════════════════════════╗"
echo "║   🤖 SYZYGY BOT - INSTALLATION 🇫🇷        ║"
echo "║   💝 Par ★LORD‡YANKEE†HELLS ★ ❤️         ║"
echo "╚═══════════════════════════════════════════╝"
echo ""

# Détection du système
if [ -d "/data/data/com.termux" ]; then
    SYSTEM="termux"
    echo "📱 Système détecté : Termux (Android)"
else
    SYSTEM="linux"
    echo "🐧 Système détecté : Linux"
fi

echo ""
echo "🔄 Installation en cours..."
echo ""

# Mise à jour des paquets
echo "📦 Étape 1/4 : Mise à jour des paquets..."
if [ "$SYSTEM" = "termux" ]; then
    pkg update -y > /dev/null 2>&1
    pkg upgrade -y > /dev/null 2>&1
else
    sudo apt update -y > /dev/null 2>&1
    sudo apt upgrade -y > /dev/null 2>&1
fi
echo "✅ Paquets mis à jour !"

# Installation de Python
echo ""
echo "🐍 Étape 2/4 : Installation de Python et Git..."
if [ "$SYSTEM" = "termux" ]; then
    pkg install python git -y > /dev/null 2>&1
else
    sudo apt install python3 python3-pip git -y > /dev/null 2>&1
fi
echo "✅ Python et Git installés !"

# Installation des modules Python
echo ""
echo "📚 Étape 3/4 : Installation des modules Python..."
pip install fbchat requests --quiet 2>&1
if [ $? -ne 0 ]; then
    pip3 install fbchat requests --quiet 2>&1
fi
echo "✅ Modules Python installés !"

# Création du dossier du bot
echo ""
echo "📁 Étape 4/4 : Création du dossier du bot..."
BOT_DIR="$HOME/syzygy-bot"
mkdir -p "$BOT_DIR"
cd "$BOT_DIR"
echo "✅ Dossier créé : $BOT_DIR"

# Instructions finales
echo ""
echo "╔═══════════════════════════════════════════╗"
echo "║   ✅ INSTALLATION TERMINÉE !              ║"
echo "╚═══════════════════════════════════════════╝"
echo ""
echo "📝 Prochaines étapes :"
echo ""
echo "1️⃣  Copie tous les fichiers .py dans le dossier :"
echo "    $BOT_DIR"
echo ""
echo "2️⃣  Navigue vers le dossier :"
echo "    cd $BOT_DIR"
echo ""
echo "3️⃣  Lance le bot :"
if [ "$SYSTEM" = "termux" ]; then
    echo "    python bot.py"
else
    echo "    python3 bot.py"
fi
echo ""
echo "📸 (Optionnel) Ajoute une image pour le menu :"
echo "    cp /chemin/vers/ton/image.jpg $BOT_DIR/menu.jpg"
echo ""
echo "═══════════════════════════════════════════"
echo "💡 Fichiers nécessaires :"
echo "  - bot.py"
echo "  - config.py"
echo "  - utils.py"
echo "  - commands.py"
echo "  - commands_utils.py"
echo "  - commands_economy.py"
echo "  - commands_gacha.py"
echo "  - commands_fun.py"
echo "  - commands_anime.py"
echo "═══════════════════════════════════════════"
echo ""
echo "🆘 Besoin d'aide ? Rejoins : https://t.me/nekosclub"
echo ""
echo "💝 Merci d'utiliser Syzygy Bot !"
echo ""
