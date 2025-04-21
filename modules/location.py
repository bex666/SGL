
def get_predefined_locations():
    return {
        "France": [
            {"city": "Paris", "region": "Île-de-France", "country": "France", "latitude": 48.8566, "longitude": 2.3522},
            {"city": "Lyon", "region": "Auvergne-Rhône-Alpes", "country": "France", "latitude": 45.7640, "longitude": 4.8357},
            {"city": "Marseille", "region": "Provence-Alpes-Côte d'Azur", "country": "France", "latitude": 43.2965, "longitude": 5.3698},
            {"city": "Toulouse", "region": "Occitanie", "country": "France", "latitude": 43.6047, "longitude": 1.4442},
            {"city": "Nice", "region": "Provence-Alpes-Côte d'Azur", "country": "France", "latitude": 43.7102, "longitude": 7.2620},
            {"city": "Nantes", "region": "Pays de la Loire", "country": "France", "latitude": 47.2184, "longitude": -1.5536},
            {"city": "Strasbourg", "region": "Grand Est", "country": "France", "latitude": 48.5734, "longitude": 7.7521},
            {"city": "Montpellier", "region": "Occitanie", "country": "France", "latitude": 43.6108, "longitude": 3.8767},
            {"city": "Bordeaux", "region": "Nouvelle-Aquitaine", "country": "France", "latitude": 44.8378, "longitude": -0.5792},
            {"city": "Rennes", "region": "Bretagne", "country": "France", "latitude": 48.1173, "longitude": -1.6778}
        ],
        "Europe": [
            {"city": "Berlin", "region": "Berlin", "country": "Germany", "latitude": 52.5200, "longitude": 13.4050},
            {"city": "Madrid", "region": "Community of Madrid", "country": "Spain", "latitude": 40.4168, "longitude": -3.7038},
            {"city": "Rome", "region": "Lazio", "country": "Italy", "latitude": 41.9028, "longitude": 12.4964},
            {"city": "London", "region": "England", "country": "United Kingdom", "latitude": 51.5074, "longitude": -0.1278},
            {"city": "Amsterdam", "region": "North Holland", "country": "Netherlands", "latitude": 52.3676, "longitude": 4.9041},
            {"city": "Vienna", "region": "Vienna", "country": "Austria", "latitude": 48.2082, "longitude": 16.3738},
            {"city": "Lisbon", "region": "Lisbon", "country": "Portugal", "latitude": 38.7169, "longitude": -9.1399},
            {"city": "Brussels", "region": "Brussels-Capital", "country": "Belgium", "latitude": 50.8503, "longitude": 4.3517},
            {"city": "Zurich", "region": "Zurich", "country": "Switzerland", "latitude": 47.3769, "longitude": 8.5417},
            {"city": "Oslo", "region": "Oslo", "country": "Norway", "latitude": 59.9139, "longitude": 10.7522}
        ],
        "Monde": [
            {"city": "New York", "region": "New York", "country": "USA", "latitude": 40.7128, "longitude": -74.0060},
            {"city": "Los Angeles", "region": "California", "country": "USA", "latitude": 34.0522, "longitude": -118.2437},
            {"city": "Tokyo", "region": "Tokyo", "country": "Japan", "latitude": 35.6895, "longitude": 139.6917},
            {"city": "Seoul", "region": "Seoul", "country": "South Korea", "latitude": 37.5665, "longitude": 126.9780},
            {"city": "Sydney", "region": "New South Wales", "country": "Australia", "latitude": -33.8688, "longitude": 151.2093},
            {"city": "Toronto", "region": "Ontario", "country": "Canada", "latitude": 43.6532, "longitude": -79.3832},
            {"city": "São Paulo", "region": "São Paulo", "country": "Brazil", "latitude": -23.5505, "longitude": -46.6333},
            {"city": "Cape Town", "region": "Western Cape", "country": "South Africa", "latitude": -33.9249, "longitude": 18.4241},
            {"city": "Istanbul", "region": "Istanbul", "country": "Turkey", "latitude": 41.0082, "longitude": 28.9784},
            {"city": "Dubai", "region": "Dubai", "country": "UAE", "latitude": 25.276987, "longitude": 55.296249}
        ]
    }

def choose_location():
    import json
    locations = get_predefined_locations()
    print("🌍 Choisissez une localisation :")

    options = []
    for continent, cities in locations.items():
        print(f"🗺️ {continent}")
        for i, city in enumerate(cities, start=len(options) + 1):
            options.append(city)
            print(f"   {i}. {city['city']}, {city['country']}")

    try:
        choix = int(input("Entrez le numéro de la ville : "))
        selected = options[choix - 1]
        print(f"✅ Localisation sélectionnée : {selected['city']} ({selected['country']})")
        with open("settings/config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
        config["location"] = selected
        with open("settings/config.json", "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
        return selected
    except Exception as e:
        print("❌ Erreur de sélection :", e)
        return None
