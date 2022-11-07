from typing import Dict
import json as json

def get_all_autos() -> Dict:
    with open("automobiliu_data.json") as auto_data:
        data = json.load(auto_data)

    return data
