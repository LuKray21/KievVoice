from src.NetworkController.HttpWorker import HttpWorker

class authorizationNetworkController():
    def __init__(self):
        self.networkWorker = HttpWorker()

    def register(self, login, name, surname, region, age, phone, email, password):
        print('РЕГИСТРУЮСЬ')
        if self.networkWorker.addUser( login, name, surname, region, age, phone, email, password) == 200:
            return True
        else:
            return False
        

    def authorize(self, login, password):
        userData = self.networkWorker.authorize(login, password)
        if userData is not None: 
            # self.endAuthorizationCallback()
            return userData
        else:
            print('Не зайшов')
            return None
         