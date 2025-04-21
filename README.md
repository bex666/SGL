
# 🌐 SGL – Search Google Legitimately

**SGL** est un projet conçu pour simuler le comportement humain sur Google dans le but de légitimer une adresse IP, souvent utilisée depuis un serveur distant, une machine virtuelle ou un VPS.

---

## 🎯 Objectif

Le but de ce projet n’est **pas de scraper Google**, mais de **faire croire à Google qu’un vrai utilisateur effectue des recherches légitimes**, pour renforcer la crédibilité comportementale d’une IP ou d’un environnement.

---

## 🛠️ Fonctionnalités

- ✅ Recherche Google en Selenium avec frappe réaliste
- ✅ Clics aléatoires dans les résultats + navigation réelle
- ✅ Localisation géographique simulée (30 villes prédéfinies)
- ✅ Planification de recherches (heures de bureau, continu, etc.)
- ✅ Affichage IP, TOR, et géolocalisation en haut du menu
- ✅ Interface CLI intuitive
- ✅ Vérification automatique de Google Maps avec position simulée
- ✅ Détection de blocage Google (/sorry/, captchas)

---

## 📦 Installation

### ✅ Testé sur :
- **Ubuntu Desktop 20.04.6 LTS**
- Navigateur : **Google Chrome stable**
- Python : **>= 3.8**

### 🔧 Dépendances :

```bash
sudo apt update && sudo apt install -y python3 python3-pip unzip xvfb
pip3 install -r requirements.txt
playwright install  # (si tu veux tester Playwright)
```

### 📥 Installation automatique :

```bash
chmod +x install/setup.sh
./install/setup.sh
```

---

## 🚀 Utilisation

Lance simplement :

```bash
python3 main.py
```

### Menu CLI :

```
RECHERCHE
1 - Lancer une recherche immédiate
2 - Planificateur de recherches

LOCALISATION
3 - Choisir une localisation (France, Europe, Monde)
4 - Vérifier la position dans Google Maps

RÉSEAU
5 - Informations IP & TOR

CONFIGURATION
6 - Modifier les mots-clés (ouvre le fichier)
```

---

## 🧭 Roadmap

Tu peux consulter [ROADMAP.md](ROADMAP.md) pour suivre l'évolution du projet.

---

## 🛑 Disclaimer

Ce projet est uniquement destiné à simuler **un comportement utilisateur**. Il **ne doit pas être utilisé pour scraper, contourner des systèmes de sécurité, ou violer les CGU de Google.**

Utilisation à des fins éducatives, de test ou de recherche uniquement.

---

✨ Projet propulsé avec ❤️ par l'automatisation Python.
