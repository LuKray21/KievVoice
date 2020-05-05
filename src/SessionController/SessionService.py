#Realization

class SessionService():
    def __init__(self):
        self.authorized = False
        
    def setAuthorizationStatus(self, status):       #Boolean
        self.authorized = True
    
    def getAuthorizationStatus(self):               #Boolean
        return self.authorized