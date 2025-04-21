
import time
import json
import random
from datetime import datetime
from modules.search_selenium import perform_search_selenium

def run_scheduled_search(config):
    keywords_file = config.get("keywords_file", "settings/mots_cles.txt")
    location = config.get("location")
    mode = config.get("schedule_mode", 1)
    interval_minutes = config.get("interval_minutes", 15)

    with open(keywords_file, "r", encoding="utf-8") as f:
        keywords = [line.strip() for line in f if line.strip()]

    print("🕒 Démarrage du planificateur de recherches...")

    if mode == 1:
        start = datetime.strptime("09:00", "%H:%M").time()
        end = datetime.strptime("17:30", "%H:%M").time()
        while True:
            now = datetime.now().time()
            if start <= now <= end:
                lancer_recherche(keywords, location)
            time.sleep(interval_minutes * 60)

    elif mode == 2:
        heure_debut = config.get("custom_start", "08:00")
        heure_fin = config.get("custom_end", "20:00")
        start = datetime.strptime(heure_debut, "%H:%M").time()
        end = datetime.strptime(heure_fin, "%H:%M").time()
        while True:
            now = datetime.now().time()
            if start <= now <= end:
                lancer_recherche(keywords, location)
            time.sleep(interval_minutes * 60)

    elif mode == 3:
        while True:
            lancer_recherche(keywords, location)
            time.sleep(interval_minutes * 60)

    elif mode == 4:
        cycles = config.get("cycles", 5)
        for _ in range(cycles):
            lancer_recherche(keywords, location)
            time.sleep(interval_minutes * 60)

def lancer_recherche(keywords, location):
    print("🔁 Nouvelle recherche planifiée...")
    ua = None  # user-agent supprimé
    perform_search_selenium(keywords, ua, location)
