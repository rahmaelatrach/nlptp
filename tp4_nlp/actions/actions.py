from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from Capital import Capital  # Assurez-vous que le fichier se nomme capital.py et non Capital.py
from Weather import Weather
class ActionGetCountryCapital(Action):
    def name(self) -> Text:
        return "get_country_capital"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities = tracker.latest_message.get('entities', [])
        country_entity = next((e for e in entities if e['entity'] == 'country'), None)
        
        if country_entity:
            country = country_entity['value']
            capital = Capital().get_country_capital(country)  # Utiliser la fonction get_country_capital de la classe Capital

            if capital:
                dispatcher.utter_message(template="utter_capital", country=country, capital=capital)
            else:
                dispatcher.utter_message(text=f"Any capital of {country}.")
        else:
            dispatcher.utter_message(text="Sorry,I did'nt understand which country you want")

        return []
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city=tracker.latest_message['text']
        temp=int(Weather(city)['temp']-273)
        dispatcher.utter_template("utter_temp",
            tracker,city=city,temp=temp)

        return [] 
class ActionAskHelp(Action):
    def name(self) -> Text:
        return "action_ask_help"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Thank you for asking, but I am a bot. I can help. To show you how I can assist you, type 'help'.")
        return []
