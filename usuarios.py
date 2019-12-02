class Usuario:
    
    def __init__(self,user,comando,timestamp,ipserver):
        self.user = user
        self.comando = comando
        self.timestamp = timestamp
        self.ipserver = ipserver
    
    def toDBCollection(self):
        return {
            "user":self.user,
            "comando":self.comando,
            "timestamp":self.timestamp,
            "ipserver":self.ipserver
        }
    def __str__(self):
        return "User: %s - Comando: %s - Timestamp: %i - Ipserver: %i"\
            %(self.user, self.comando, self.timestamp, self.ipserver)