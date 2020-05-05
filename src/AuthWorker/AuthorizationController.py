from kivy.uix.boxlayout import BoxLayout

from .authorizationNetworkController import authorizationNetworkController
from kivy.lang import Builder 

with open('C:\Work\Bachelor\KievVol\src\AuthWorker\AuthorizationController.kv', encoding='utf-8') as f:
    presentation = Builder.load_string(f.read())

class AuthorizationController():
    def __init__(self, mainWindow, session, authorizedCallback):
        self.session = session
        self.mainWindow = mainWindow
        self.authorizedCallback = authorizedCallback

        self.authNetwork = authorizationNetworkController(self.endAuthorizationCallback, self.endRegistrationCallback)
        #WORK WINDOWS
        self.authWindow = AuthWindow()
        self.registWindow = RegistrationWindow()

    def setRegistrationWindow(self):
        self.removeWindow(self.authWindow)
        self.addNewWindow(self.registWindow)

    def setAuthWindow(self):
        self.removeWindow(self.registWindow)
        self.addNewWindow(self.authWindow)

    def addNewWindow(self, widget):
        self.mainWindow.add_widget(widget)

    def removeWindow(self, widget):
        self.mainWindow.remove_widget(widget)

    def endAuthorizationCallback(self):                 ##DOBAVIT NETWORK
        self.removeWindow(self.authWindow)
        self.authorizedCallback()

    def endRegistrationCallback(self):
        self.removeWindow(self.registWindow)
        self.addNewWindow(self.authWindow)

##AUTHORIZATION
    def tryToRegister(self, login, password):
        self.authNetwork.register(login, password)


    def tryToAuthorize(self, login, password):
        self.authNetwork.authorize(login, password)

###SESSION CONTROLLER METHODS
    def setAuthorizationStatus(self, status):
        self.session.setAuthorizationStatus(status)
    

class AuthWindow(BoxLayout):
    def __init__(self):
        super(AuthWindow, self).__init__()

class RegistrationWindow(BoxLayout):
    def __init__(self):
        super(RegistrationWindow, self).__init__()