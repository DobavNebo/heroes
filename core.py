import requests
from typing import List, Dict, Optional

def get_all_heroes() -> Optional[List[Dict]]:
    try:
        response = requests.get("https://akabab.github.io/superhero-api/api/all.json", timeout=10)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Ошибка HTTP: {response.status_code}")
            return None
            
    except requests.exceptions.Timeout:
        print("Превышено время ожидания")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None

def find_tallest(gender: str, has_job: bool) -> Optional[Dict]:
    
    heroes = get_all_heroes()
    if heroes:
        target = -1
        target_height = -1

        for hero in heroes:
            job = hero['work']['occupation'] != "-"
            tall = float(hero['appearance']['height'][1].split()[0])
            if tall >= target_height and hero['appearance']['gender'] == gender and job == has_job:
                target = hero
                target_height = tall
        if target != -1:
            return target
        else:
            return None
    else:
        return None
