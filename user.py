from datetime import datetime
from flask_login import UserMixin

MOCK_TABLES = [{"_id": "1", "number": "1", "owner":"veliyev.yasin@gmail.com",
                "url": "mockurl"}]



MOCK_REQUESTS = [{"_id": "1", "table_number": "1","table_id": "1",
 "time": datetime.now()}]

class User(UserMixin):
    MOCK_USERS = [{'id':1, 'email':'veliyev.yasin@gmail.com', 'password':'pbkdf2:sha256:150000$ZIP60QTk$e9490f05e853eb904f60a97a375b96d4bf20d70a8fb5ee235e6ccfec58b3245d'}]
    
    def __init__(self,email):
        super().__init__()
        self.email = email
        

    @classmethod
    def get_user_by_email(cls, email):
        for user in cls.MOCK_USERS:
            if user['email'] == email:
                cls.id = user['id']
                return user
    
    @classmethod
    def set_id(cls):
        cls.id = cls.MOCK_USERS[-1]['id'] + 1

    @classmethod
    def get_user_by_id(cls, id):
        for user in cls.MOCK_USERS:
            if user['id'] == id:
                cls.id = id
                return cls(user['email'])


    @classmethod
    def add_user(cls, user):
        cls.MOCK_USERS.append(user)
        cls.MOCK_USERS[-1]['id'] = cls.id

    def get_id(self):
        return self.id

    def check_password(self, password):
        pass
    
    @staticmethod
    def add_table(number, owner):
        MOCK_TABLES.append({"_id":str(number), "number":number, "owner":owner})
        return number

    @staticmethod
    def update_table( _id, url):
        for table in MOCK_TABLES:
            if table.get("_id") == _id:
                table['url'] = url
        
    @staticmethod  
    def get_tables(owner_id):
        return MOCK_TABLES
    
    @staticmethod 
    def delete_table(table_id):
        for i, table in enumerate(MOCK_TABLES):
            if table.get("_id") == table_id:
                del MOCK_TABLES[i]
    @staticmethod
    def add_request(tid, time):
        MOCK_REQUESTS.append({"_id": tid, "table_number": tid,"table_id": tid,"time": time})

    @staticmethod 
    def get_request(owner_id):
        return MOCK_REQUESTS
    
    @staticmethod 
    def delete_request(request_id):
        for i, request in enumerate(MOCK_REQUESTS):
            if request.get('_id') == request_id:
                del MOCK_REQUESTS[i]
    