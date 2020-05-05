#Calls
from .SessionService import SessionService

class SessionController():
    def __init__(self):
        super(SessionController, self).__init__()
        self.service = SessionService()
    
    def setAuthorizationStatus(self, status):       #Boolean
        self.service.setAuthorizationStatus(status)
    
    def getAuthorizationStatus(self):               #Boolean
        return self.service.getAuthorizationStatus()