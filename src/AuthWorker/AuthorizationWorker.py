from kivy.uix.boxlayout import BoxLayout

from .authorizationNetworkController import authorizationNetworkController
from kivy.lang import Builder 

with open('C:\Work\Bachelor\KievVol\src\AuthWorker\AuthorizationWidget.kv', encoding='utf-8') as f:
    presentation = Builder.load_string(f.read())

class AuthorizationWorker():
    def __init__(self, mainWindow, authorizedCallback):
        self.mainWindow = mainWindow
        self.authorizedCallback = authorizedCallback

        self.authNetwork = authorizationNetworkController(self.endAuthorizationCallback, self.endRegistrationCallback)
        #WORK WINDOWS
        self.authWindow = AuthWindow()
        self.registWindow = RegistrationWindow()
        self.goodWidget = GoodResultPage()

        self.userRegion = 'Шевченківський'

    def setUserRegion(self, region):
        self.userRegion = region 
        print(region)
    
    def getUserRegion(self):
        return self.userRegion

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

    def setAuthWindowAfReg(self):
        self.removeWindow(self.goodWidget)
        self.addNewWindow(self.authWindow)

    def endRegistrationCallback(self):
        self.removeWindow(self.registWindow)
        self.addNewWindow(self.goodWidget)

##AUTHORIZATION
    def tryToRegister(self, login, password):
        self.authNetwork.register(login, password)


    def tryToAuthorize(self, login, password):
        self.authNetwork.authorize(login, password)

class UserRegionDropDown(BoxLayout):
    pass

class GoodResultPage(BoxLayout):
    def __init__(self):
        super(GoodResultPage, self).__init__()

class AuthWindow(BoxLayout):
    def __init__(self):
        super(AuthWindow, self).__init__()

class RegistrationWindow(BoxLayout):
    def __init__(self):
        super(RegistrationWindow, self).__init__()