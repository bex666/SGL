
import os
import time
import random
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

def perform_search_selenium(keywords, _, location):
    profile_path = "/home/sgl/.config/selenium_profile"
    os.makedirs(profile_path, exist_ok=True)

    options = Options()
    options.add_argument(f"--user-data-dir={profile_path}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    print("🚀 Lancement du navigateur Chrome...")
    try:
        print("🚀 Lancement de Chrome avec session persistante...")
        driver = uc.Chrome(options=options, user_data_dir=profile_path)
    except Exception as e:
        print(f"⚠️ Échec de lancement avec profil. Raison : {e}")
        print("🧹 Nettoyage du cache...")
        import shutil
        shutil.rmtree(profile_path, ignore_errors=True)
        driver = uc.Chrome(options=options)  # fallback sans profil
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
        "latitude": location['latitude'],
        "longitude": location['longitude'],
        "accuracy": 100
    })
    actions = ActionChains(driver)

    driver.get("https://www.google.com")
    time.sleep(random.uniform(2.5, 4.5))
    tabs = [driver.current_window_handle]

    for i, keyword in enumerate(keywords):
        if i > 0 and i % 3 == 0:
            pause = random.uniform(10, 25)
            print(f'⏸️  Pause simulateur : {pause:.1f} secondes')
            time.sleep(pause)
        print(f"🔎 Recherche : {keyword}")
        use_tab = random.random() > 0.4  # 60% chance d'utiliser le même onglet

        if not use_tab:
            # Ouvre un nouvel onglet
            driver.execute_script("window.open('https://www.google.com', '_blank');")
            driver.switch_to.window(driver.window_handles[-1])
            tabs.append(driver.current_window_handle)
            time.sleep(random.uniform(2, 4))
        else:
            # Revenir à l'onglet initial
            tab_to_use = random.choice(tabs)
            driver.switch_to.window(tab_to_use)
            driver.get("https://www.google.com")
            time.sleep(random.uniform(2, 3))

        try:
            search_box = driver.find_element(By.NAME, "q")
            search_box.clear()
            for char in keyword:
                search_box.send_keys(char)
                time.sleep(random.uniform(0.05, 0.2))
            search_box.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"❌ Erreur : {e}")
            continue

        time.sleep(random.uniform(3.5, 5.5))

        for _ in range(random.randint(3, 5)):
            driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(random.uniform(1, 2))

        # Possibilité de fermer un onglet aléatoirement après recherche
        if len(driver.window_handles) > 2 and random.random() < 0.3:
            tab_to_close = random.choice([t for t in driver.window_handles if t != driver.current_window_handle])
            driver.switch_to.window(tab_to_close)
            driver.close()
            tabs.remove(tab_to_close)
            driver.switch_to.window(tabs[-1])
            print("🧹 Onglet fermé pour simuler un comportement humain.")
            time.sleep(1.5)

        time.sleep(random.uniform(2, 4))

    print("✅ Toutes les recherches ont été effectuées.")
    try:
    input("🔚 Appuyez sur Entrée pour fermer le navigateur...")
    driver.quit()
except Exception as e:
    print(f"ℹ️ Le navigateur a probablement été fermé manuellement. ({e})")
    print("🔁 Retour au menu principal...")
