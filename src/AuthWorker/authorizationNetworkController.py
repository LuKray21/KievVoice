class authorizationNetworkController():
    def __init__(self, endAuthorizationCallback, endRegistrationCallback):
        self.endAuthorizationCallback = endAuthorizationCallback
        self.endRegistrationCallback = endRegistrationCallback

    def register(self, login, password):
        self.endRegistrationCallback()

    def authorize(self, login, password):
        self.endAuthorizationCallback()