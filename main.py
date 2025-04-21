import json
import os
from pprint import pprint
from modules.ip_check import check_ip, is_tor_used, get_ip_info
from modules.location import choose_location
from modules.search_selenium import perform_search_selenium
from modules.scheduler import run_scheduled_search
from modules.keyword_manager import edit_keywords
from modules.maps_viewer import view_location_on_google_maps
from actions import menu_actions, afficher_menu

def load_config():
    with open("settings/config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def lancer_recherche():
    config = load_config()
    loc = config.get("location") or choose_location()
    keywords = open(config.get("keywords_file", "settings/mots_cles.txt")).read().splitlines()
    results = perform_search_selenium(keywords, None, loc)
    for r in results:
        print(r)

def planifier_recherche():
    config = load_config()
    run_scheduled_search(config)

def choisir_localisation():
    choose_location()
    input("✅ Appuyez sur Entrée pour revenir au menu...")

def afficher_localisation():
    config = load_config()
    loc = config.get("location") or choose_location()
    view_location_on_google_maps(loc)

def infos_ip():
    info = get_ip_info()
    print("📡 Détails IP :")
    pprint(info)
    input("Appuyez sur Entrée pour revenir au menu...")

def modifier_keywords():
    edit_keywords()

def quitter():
    print("❌ Sortie")
    exit()


def main():
    while True:
        config = load_config()
        ip = check_ip()
        tor = is_tor_used()
        loc = config.get("location") or choose_location()

        print("🌐 SGL - Search Google Legitimately (Selenium)")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"🌍 IP : {ip}   🛡️ TOR : {'Oui' if tor else 'Non'}")
        print(f"📍 Localisation : {loc.get('city', '')}, {loc.get('region', '')}, {loc.get('country', '')}")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        afficher_menu()
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        choix = input("Votre choix : ")
        action = menu_actions.get(choix)
        if action:
            action[1]()
        else:
            print("❌ Choix invalide.")

if __name__ == "__main__":
    main()
