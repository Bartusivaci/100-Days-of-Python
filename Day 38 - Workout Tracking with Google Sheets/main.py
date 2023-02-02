import requests
from datetime import datetime

APP_ID = "4219de1d"
API_KEY = "2eed09e040255d19fafe45c332fa3292"

GENDER = "male"
WEIGHT_KG = 64.8
HEIGHT_CM = 170
AGE = 23

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/5123fc8021a470fb0e0f6bbf656eef42/workoutTracking/workouts"

parameters = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_header = {
        "Authorization": "Bearer ADAS&$DMK'?MDKDAK%KFS321i49109"
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=bearer_header)

    print(sheet_response.text)