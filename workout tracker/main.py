import requests
from datetime import datetime
GENDER = "Male"
WEIGHT_KG = 75
HEIGHT_CM = 172
AGE = 22

APP_ID = "bb4f2620"
API_KEY = "8e5cdfba1112a3fd50448cd31f68b075"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
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
sheet_endpoint = "https://api.sheety.co/9f856e76c1e0a716aee9998a35134ab8/myWorkouts/workouts"
bearer_headers = {
"Authorization": "Bearer kabiralhavat.123"
}
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
)
# print(sheet_response.text)


output_response =  requests.get(f"{sheet_endpoint}/7",headers=bearer_headers)
print(output_response.text)