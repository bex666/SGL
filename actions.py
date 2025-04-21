import json
from pprint import pprint
from modules.ip_check import check_ip, is_tor_used, get_ip_info
from modules.location import choose_location
from modules.search_selenium import perform_search_selenium
from modules.scheduler import run_scheduled_search
from modules.keyword_manager import edit_keywords
from modules.maps_viewer import view_location_on_google_maps

def load_config():
    with open("settings/config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_infos():
    config = load_config()
    ip = check_ip()
    tor = is_tor_used()
    loc = config.get("location") or choose_location()
    print("🌐 SGL - Search Google Legitimately (Selenium)")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🌍 IP : {ip}   🛡️ TOR : {'Oui' if tor else 'Non'}")
    print(f"📍 Localisation : {loc.get('city', '')}, {loc.get('region', '')}, {loc.get('country', '')}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def lancer_recherche():
    config = load_config()
    loc = config.get("location") or choose_location()
    keywords = open(config.get("keywords_file", "settings/mots_cles.txt")).read().splitlines()
    perform_search_selenium(keywords, None, loc)

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

    if "error" in info:
        print("❌ Impossible de récupérer les infos IP :", info["error"])
        return

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🌐 INFORMATIONS SUR L'ADRESSE IP")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🔸 IP Publique : {info.get('query', 'N/A')}")
    print(f"📍 Pays       : {info.get('country', 'N/A')} ({info.get('countryCode', 'N/A')})")
    print(f"🏙️  Région     : {info.get('regionName', 'N/A')} ({info.get('region', 'N/A')})")
    print(f"🌆 Ville      : {info.get('city', 'N/A')}")
    print(f"🛰️ FAI        : {info.get('isp', 'N/A')}")
    print(f"📡 Organisation : {info.get('org', 'N/A')}")
    print(f"🔁 TOR utilisé : {'Oui' if is_tor_used() else 'Non'}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    input("Appuyez sur Entrée pour revenir au menu...")

def modifier_keywords():
    edit_keywords()

def quitter():
    print("❌ Sortie")
    exit()







def afficher_menu():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🎛️  MENU PRINCIPAL")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("")
    print("🔍 RECHERCHE :")
    print("  [96m[1][0m Lancer la recherche immédiatement")
    print("  [96m[2][0m Lancer une recherche planifiée")
    print("")
    print("🛠️ CONFIGURATION :")
    print("  [96m[3][0m Choisir une localisation")
    print("  [96m[4][0m Configurer le navigateur et/ou vérifier la localisation (Google Maps)")
    print("  [96m[6][0m Modifier la bibliothèque de mots-clés")
    print("")
    print("🌐 INFORMATIONS :")
    print("  [96m[5][0m Vérification et informations IP")
    print("")
    print("❌ QUITTER :")
    print("  [91m[0][0m Quitter le programme")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


menu_actions = {
    "1": ("Lancer la recherche immédiatement", lancer_recherche),
    "2": ("Planificateur de recherche", planifier_recherche),
    "3": ("Choisir une localisation", choisir_localisation),
    "4": ("Configurer le navigateur et/ou vérifier la localisation (Google Maps)", afficher_localisation),
    "6": ("Modifier la bibliothèque de mots-clés", modifier_keywords),
    "5": ("Vérification et informations IP", infos_ip),
    "0": ("Quitter le programme", quitter)
}
