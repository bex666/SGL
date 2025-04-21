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
    print("📡 Détails IP :")
    pprint(info)
    input("Appuyez sur Entrée pour revenir au menu...")

def modifier_keywords():
    edit_keywords()

def quitter():
    print("❌ Sortie")
    exit()


def verifier_navigateur():
    config = load_config()
    loc = config.get("location") or choose_location()

    options = Options()
    options.add_argument("--user-data-dir=/home/sgl/.config/selenium_profile")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    try:
        print("🚀 Lancement du navigateur de test...")
        driver = uc.Chrome(options=options, user_data_dir="/home/sgl/.config/selenium_profile")
    except Exception as e:
        print(f"⚠️ Erreur : {e}")
        return

    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
        "latitude": loc['latitude'],
        "longitude": loc['longitude'],
        "accuracy": 100
    })

    driver.get("https://www.google.com/maps")
    input("🔎 Vérifie la localisation dans le navigateur, puis appuie sur Entrée...")
    driver.quit()


menu_actions = {
    "1": ("Lancer la recherche immédiatement", lancer_recherche),
    "2": ("Planificateur de recherche", planifier_recherche),
    "3": ("Choisir une localisation", choisir_localisation),
    "4": ("Vérifier la localisation (Google Maps)", afficher_localisation),
    "5": ("Vérification et informations IP", infos_ip),
    "6": ("Modifier la bibliothèque de mots-clés", modifier_keywords),
    "9": ("Vérifier le navigateur et la localisation", verifier_navigateur),
    "0": ("Quitter le programme", quitter)
}
