# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests
#
#
class weatherapi(Action):

     def name(self) -> Text:
         return "action_get_weather"
#
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         api_key = 'd1dcf6f5f9e6f85f1aa51222e18cd4c6s'
         loc = tracker.get_slot('location')
         current = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(loc, api_key)).json()
         print(current)
         country = current['sys']['country']
         condition = current['weather'][0]['main']
         city = current['name']
         temperature_c = current['main']['temp']
         humidity = current['main']['humidity']
         wind_mph = current['wind']['speed']
         response = """The current weather {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
         
         dispatcher.utter_message(response)
     
         return [SlotSet('location', loc)]
