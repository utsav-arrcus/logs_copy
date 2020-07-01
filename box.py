import boxsdk
import os
from boxsdk import OAuth2
import sys
import Utility

CLIENT_ID = '39bhn7zfittzq9zh9b3rsi5zzvf1r73x'
CLIENT_SECRET = 'sQV0aWmzHj2qGABoWJAXNd7FIFlDkYmW',
REDIRECT_URI = "https://arrcus.app.box.com"
REDIRECT_URL = 'https://account.box.com/api/oauth2/authorize?client_id={}&redirect_uri={}&response_type=code'.format(CLIENT_ID, REDIRECT_URI)

# auth_url, csrf_token = boxsdk.auth.oauth2.get_authorization_url(REDIRECT_URL)

#authentication function
def authenticateAdmin(oauth_class=OAuth2):
    oauth = oauth_class(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, store_tokens=save_tokens,)
    #reading the tokens from the file
    print("Reading tokens...")
    os.system('cls')
    at,rt = read_tokens_from_file()

    oauth._access_token=at
    oauth._refresh_token=rt
    return oauth, at, rt

#save token to a file
def save_tokens(access_token,refresh_token):
    print("Refreshing tokens...")
    target = open(Utility.get_path() +"AdminToken.txt", 'w')
    target.truncate()
    tokens = access_token+'#'+refresh_token
    target.write(tokens)
    target.close()

#reads tokens from a file
def read_tokens_from_file():
    try:
        with open(Utility.get_path() + "AdminToken.txt", 'r') as f:
            tokens=f.readline()
        return tokens.split('#')
    except:
        print("Read token error:" + str(sys.exc_info()))
        return "null","null"

client = authenticateAdmin()