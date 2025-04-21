import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

def view_location_on_google_maps(location):
    options = Options()
    options.add_argument("--user-data-dir=/home/sgl/.config/selenium_profile")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = uc.Chrome(options=options, user_data_dir="/home/sgl/.config/selenium_profile")
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
        "latitude": location['latitude'],
        "longitude": location['longitude'],
        "accuracy": 100
    })
    driver.get("https://www.google.com/maps")
    input("Appuyez sur Entrée pour fermer le navigateur...")
    driver.quit()
