import requests
import json
import uuid
import time

class HttpWorker():
    def __init__(self):
        super(HttpWorker, self).__init__()
        self.host = "http://localhost:8080/"
        self.headers = {'Content-Type': 'application/json'}

    def addUser(self, login, name, surname, region, age, phone, email, password):
        try:
            data = json.dumps({"id": str(uuid.uuid4()), "login": str(login), "name": str(name), "surname": str(surname), "region": str(region), "age":str(age), "phone":str(phone), "email":str(email), "password":str(password)})
            url = self.host + '/users'
            return (requests.post(url, data, headers = self.headers)).status_code
        except Exception as err:
            print("NETWORK ERROR: ", err)
            return 400

    def authorize(self, login, password):
        try:
            url = self.host + '/users/' + str(login) + "/" + str(password)
            r = requests.get(url)
            if r.status_code == 200:
                return r.text
            else:
                return None
        except Exception as err:
            print("NETWORK ERROR: ", err)
            return None
    
    def addEvent(self, title, description, phone, region, address, email, eventDay, eventMonth, eventTime, userId):
        try:
            eventDate = self.getConstructedTimeFormat(eventDay, eventMonth, eventTime)
            data = json.dumps({"id": str(uuid.uuid4()), "title": str(title), "description": str(description), "timestamp": str(int(time.time())), "eventDate": str(eventDate), "eventPhone":str(phone), "eventEmail":str(email), "eventRegion":str(region), "eventAddress":str(address)})
            url = self.host + '/users/{}/events'.format(userId)
            return (requests.post(url, data, headers = self.headers)).status_code
        except Exception as err:
            print("NETWORK ERROR: ", err)
            return 400
    
    def getAllEvents(self):
        try:
            url = self.host + '/users/events'
            r = requests.get(url)
            if r.status_code == 200:
                return r.text
            else:
                return None
        except Exception as err:
            print("NETWORK ERROR: ", err)
            return None

    def getConstructedTimeFormat(self, day, month, time): 
        return day + ' ' + month + " о " +  time