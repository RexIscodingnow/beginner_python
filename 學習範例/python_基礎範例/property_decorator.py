class Property_Characteristic():
    '''
    @property 裝飾器，特性與使用
    '''
    def __init__(self, username="", password=None):
        self._username = username
        self._password = int(password)

    @property
    def level(self):
        '''
        宣告 level，其屬性為 "唯讀 (Only getter)"
        '''
        return "30 歲魔法師 => 咒語: 去去武器走~"

    @property
    def username(self):
        '''
        宣告 username，並設定屬性為 "讀取 (getter)"
        '''
        return self._username

    @username.setter
    def username(self, username):
        '''
        username 屬性，設為 "寫入 (setter)"
        '''
        self._username = username

    @username.deleter
    def username(self):
        '''
        刪除 username 屬性
        '''
        del self._username

    ''' --------------------------------------------- '''
    @property
    def _password(self):
        raise AttributeError("password is not readable")

    @_password.setter
    def _password(self, password):
        self.password_hash = password + 94865231

username = input("用戶名稱: ")
password = input("密碼: ")

user = Property_Characteristic(
    username = username,
    password = password
)
print("------------------")
print("username: ", user.username)
print("password: ", user.password_hash)
print("等級: ", user.level)

print("------------------")
del user.username   # 執行 property 的 deleter 功能

try:
    print("username: ", user.username)
    print("password: ", user.password_hash)
    print("等級: ", user.level)

except Exception:
    print("username is delete")
    print("password: ", user.password_hash)
    print("等級: ", user.level)

