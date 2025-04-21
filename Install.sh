#!/bin/bash

echo "🔧 Installation des dépendances SGL..."

# Mettez à jour la liste des paquets
sudo apt update

# Installez les dépendances système
sudo apt install -y python3 python3-pip git unzip curl xvfb fonts-dejavu-core

# Installer Google Chrome si non installé
if ! command -v google-chrome &> /dev/null; then
    echo "🌐 Installation de Google Chrome..."
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i google-chrome-stable_current_amd64.deb || sudo apt -f install -y
    rm google-chrome-stable_current_amd64.deb
fi

# Installer ChromeDriver
echo "📦 Installation de ChromeDriver..."
CHROME_VERSION=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+')
CHROMEDRIVER_VERSION=$(curl -s "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json" | grep -B 1 "$CHROME_VERSION" | grep version | head -n1 | cut -d '"' -f4)
wget -O chromedriver.zip "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/$CHROMEDRIVER_VERSION/linux64/chromedriver-linux64.zip"
unzip chromedriver.zip -d chromedriver_temp
sudo mv chromedriver_temp/chromedriver-linux64/chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver
rm -rf chromedriver.zip chromedriver_temp

# Installer les dépendances Python
echo "🐍 Installation des dépendances Python..."
pip3 install -r requirements.txt
playwright install

echo "✅ Installation terminée avec succès."
