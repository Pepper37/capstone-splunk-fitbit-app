#import matplotlib.pyplot as plt
import fitbit

# gather_keys_oauth2.py file needs to be in the same directory. 
# also needs to install cherrypy: https://pypi.org/project/CherryPy/
# pip install CherryPy
import gather_keys_oauth2 as Oauth2
import pandas as pd 
from datetime import datetime


# YOU NEED TO PUT IN YOUR OWN CLIENT_ID AND CLIENT_SECRET
CLIENT_ID='238B6M'
CLIENT_SECRET='ef096e7ecae2a50b32f704f2d812626a'

server=Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN=str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN=str(server.fitbit.client.session.token['refresh_token'])
auth2_client=fitbit.Fitbit(CLIENT_ID,CLIENT_SECRET,oauth2=True,access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN)

# You will have to modify this 
# depending on when you started to use a fitbit
# Update this line and replace 'today' with base_date=oneDate
oneDate = pd.datetime(year = 2022, month = 9, day = 28)
#oneDate = datetime(year = datetime.now().year, month = datetime.now().month, day = datetime.now().day)

FoodData = auth2_client.foods_log(date=oneDate)
df = pd.DataFrame(FoodData['foods'])
df.to_csv('/opt/splunk/etc/apps/Capstone/lookups/' + 'Food' + '.csv', index = False)




