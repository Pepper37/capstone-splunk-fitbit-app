import fitbit

# gather_keys_oauth2.py file needs to be in the same directory. 
# also needs to install cherrypy: https://pypi.org/project/CherryPy/
# pip install CherryPy
import gather_keys_oauth2 as Oauth2
import pandas as pd 
from datetime import datetime

# YOU NEED TO PUT IN YOUR OWN CLIENT_ID AND CLIENT_SECRET
CLIENT_ID='238G4V'
CLIENT_SECRET='59f3e7e9621cdabcc0bf307d1f678dda'

server=Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN=str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN=str(server.fitbit.client.session.token['refresh_token'])
auth2_client=fitbit.Fitbit(CLIENT_ID,CLIENT_SECRET,oauth2=True,access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN)

oneDate = pd.datetime(year = 2022, month = 11, day = 26)
# oneDate = datetime(year = datetime.now().year, month = datetime.now().month, day = datetime.now().day)

#########################################################################
# Activities_Calories
# calories - The top level time series for calories burned inclusive of 
# BMR, tracked activity, and manually logged activities.
#########################################################################
#

date_list = []
df_list = []
CalorieData = auth2_client.intraday_time_series('activities/calories',oneDate,detail_level='1min')
df = pd.DataFrame(CalorieData['activities-calories-intraday']['dataset'])
date_list.append(oneDate)   
df_list.append(df)  
final_df_list = []
for date, df in zip(date_list, df_list):

    if len(df) == 0:
        continue
    df.loc[:, 'date'] = pd.to_datetime(date)
    final_df_list.append(df)

final_df = pd.concat(final_df_list, axis = 0)
final_df.to_csv('~/capstone/splunk/etc/apps/Capstone/lookups/' + 'Activities_Calories' + '.csv', index = False)

#########################################################################
# Activities_Distance
#########################################################################
#

date_list = []
df_list = []
DistanceData = auth2_client.intraday_time_series('activities/distance',oneDate,detail_level='15min')
df = pd.DataFrame(DistanceData['activities-distance-intraday']['dataset'])
date_list.append(oneDate)   
df_list.append(df)  
final_df_list = []
for date, df in zip(date_list, df_list):

    if len(df) == 0:
        continue
    df.loc[:, 'date'] = pd.to_datetime(date)
    final_df_list.append(df)

final_df = pd.concat(final_df_list, axis = 0)
final_df.to_csv('~/capstone/splunk/etc/apps/Capstone/lookups/' + 'Activities_Distance' + '.csv', index = False)

#########################################################################
# Activities_Elevation
#########################################################################
#

date_list = []
df_list = []
ElevationData = auth2_client.intraday_time_series('activities/elevation',oneDate,detail_level='15min')
df = pd.DataFrame(ElevationData['activities-elevation-intraday']['dataset'])
date_list.append(oneDate)   
df_list.append(df)  
final_df_list = []
for date, df in zip(date_list, df_list):

    if len(df) == 0:
        continue
    df.loc[:, 'date'] = pd.to_datetime(date)
    final_df_list.append(df)

final_df = pd.concat(final_df_list, axis = 0)
final_df.to_csv('~/capstone/splunk/etc/apps/Capstone/lookups/' + 'Activities_Elevation' + '.csv', index = False)

#########################################################################
# Activities_Floors
#########################################################################
#

date_list = []
df_list = []
FloorsData = auth2_client.intraday_time_series('activities/floors',oneDate,detail_level='15min')
df = pd.DataFrame(FloorsData['activities-floors-intraday']['dataset'])
date_list.append(oneDate)   
df_list.append(df)  
final_df_list = []
for date, df in zip(date_list, df_list):

    if len(df) == 0:
        continue
    df.loc[:, 'date'] = pd.to_datetime(date)
    final_df_list.append(df)

final_df = pd.concat(final_df_list, axis = 0)
final_df.to_csv('~/capstone/splunk/etc/apps/Capstone/lookups/' + 'Activities_Floors' + '.csv', index = False)

#########################################################################
# Activities_Heartrate
#########################################################################
#

date_list = []
df_list = []
HeartRateData = auth2_client.intraday_time_series('activities/heart', oneDate, detail_level='1sec')
df = pd.DataFrame(HeartRateData['activities-heart-intraday']['dataset'])
date_list.append(oneDate)   
df_list.append(df)  
final_df_list = []
for date, df in zip(date_list, df_list):

    if len(df) == 0:
        continue
    df.loc[:, 'date'] = pd.to_datetime(date)
    final_df_list.append(df)

final_df = pd.concat(final_df_list, axis = 0)
final_df.to_csv('~/capstone/splunk/etc/apps/Capstone/lookups/' + 'Activities_Heartrate' + '.csv', index = False)

#########################################################################
# Activities_Steps
#########################################################################
#

date_list = []
df_list = []
StepsData = auth2_client.intraday_time_series('activities/steps',oneDate,detail_level='1min')
df = pd.DataFrame(StepsData['activities-steps-intraday']['dataset'])
date_list.append(oneDate)   
df_list.append(df)  
final_df_list = []
for date, df in zip(date_list, df_list):

    if len(df) == 0:
        continue
    df.loc[:, 'date'] = pd.to_datetime(date)
    final_df_list.append(df)

final_df = pd.concat(final_df_list, axis = 0)
final_df.to_csv('~/capstone/splunk/etc/apps/Capstone/lookups/' + 'Activities_Steps' + '.csv', index = False)

#########################################################################
# Weight
#########################################################################
#
# date_list = []
# df_list = []
# WeightData = auth2_client.get_bodyweight(base_date=None, user_id=None, period='7d', end_date=None)                                   
# df = pd.DataFrame(WeightData)
# date_list.append(oneDate)   
# df_list.append(df)  
# final_df_list = []
# for date, df in zip(date_list, df_list):

#     if len(df) == 0:
#         continue
#     df.loc[:, 'date'] = pd.to_datetime(date)
#     final_df_list.append(df)

# final_df = pd.concat(final_df_list, axis = 0)
# df.to_csv('~/capstone/splunk/etc/apps/Capstone/lookups/' + 'Weight' + '.csv', index = False)

#########################################################################
# Sleep
#########################################################################
#
date_list = []
df_list = []
stages_df_list = []

oneDayData = auth2_client.sleep(date=oneDate)
# get number of minutes for each stage of sleep and such. 
stages_df = pd.DataFrame(oneDayData['summary'])
df = pd.DataFrame(oneDayData['sleep'][0]['minuteData'])   
date_list.append(oneDate)   
df_list.append(df)  
stages_df_list.append(stages_df)   
final_df_list = []
final_stages_df_list = []

for date, df, stages_df in zip(date_list, df_list, stages_df_list):

    if len(df) == 0:
        continue
    df.loc[:, 'date'] = pd.to_datetime(date)
    stages_df.loc[:, 'date'] = pd.to_datetime(date)
    final_df_list.append(df)
    final_stages_df_list.append(stages_df)

final_df = pd.concat(final_df_list, axis = 0)
final_stages_df = pd.concat(final_stages_df_list, axis = 0)
columns = final_stages_df.columns[~final_stages_df.columns.isin(['date'])].values
columns
pd.concat([final_stages_df[columns] + 2, final_stages_df[['date']]], axis = 1)
final_df.to_csv('~/capstone/splunk/etc/apps/Capstone/lookups/' + 'minuteSleep' + '.csv', index = False)
final_stages_df.to_csv('~/capstone/splunk/etc/apps/Capstone/lookups/' + 'minutesStagesSleep' + '.csv', index = True)

#########################################################################
# Active Minutes
#########################################################################
#
SedentaryData = auth2_client.intraday_time_series('activities/minutesSedentary',oneDate)
df = pd.DataFrame(SedentaryData['activities-minutesSedentary'])
df.rename(columns={"dateTime": "date"}, inplace=True)
df.to_csv('~/capstone/splunk/etc/apps/Capstone/lookups/' + 'Activities_Minutes_Sedentary_Active' + '.csv', index = False)

LightData = auth2_client.intraday_time_series('activities/minutesLightlyActive',oneDate)
df = pd.DataFrame(LightData['activities-minutesLightlyActive'])
df.rename(columns={"dateTime": "date"}, inplace=True)
df.to_csv('~/capstone/splunk/etc/apps/Capstone/lookups/' + 'Activities_Minutes_Lightly_Active' + '.csv', index = False)

FairlyData = auth2_client.intraday_time_series('activities/minutesFairlyActive',oneDate)
df = pd.DataFrame(FairlyData['activities-minutesFairlyActive'])
df.rename(columns={"dateTime": "date"}, inplace=True)
df.to_csv('~/capstone/splunk/etc/apps/Capstone/lookups/' + 'Activities_Minutes_Fairly_Active' + '.csv', index = False)

VeryData = auth2_client.intraday_time_series('activities/minutesVeryActive',oneDate)
df = pd.DataFrame(VeryData['activities-minutesVeryActive'])
df.rename(columns={"dateTime": "date"}, inplace=True)
df.to_csv('~/capstone/splunk/etc/apps/Capstone/lookups/' + 'Activities_Minutes_Very_Active' + '.csv', index = False)

#########################################################################
# Daily Water
#########################################################################
#
# date_list = []
# df_list = []
# WaterData = auth2_client.foods_log_water(date=oneDate)
# df = pd.DataFrame(WaterData['water'])
# date_list.append(oneDate)   
# df_list.append(df)  
# final_df_list = []
# for date, df in zip(date_list, df_list):

#     if len(df) == 0:
#         continue
#     df.loc[:, 'date'] = pd.toHours Slept_datetime(date)
#     final_df_list.append(df)

# final_df = pd.concat(final_df_list, axis = 0)
# final_df.to_csv('~/capstone/splunk/etc/apps/Capstone/lookups/' + 'Water' + '.csv', index = False)

# #########################################################################
# # Daily Food
# #########################################################################
# #
# FoodData = auth2_client.foods_log(date=oneDate)
# df = pd.DataFrame(FoodData['foods'])
# df.to_csv('~/capstone/splunk/etc/apps/Capstone/lookups/' + 'Food' + '.csv', index = False)

#########################################################################
# Activities
#########################################################################
#
ActivityData = auth2_client.activities(date=oneDate)
df = pd.DataFrame(ActivityData['activities'])
df.to_csv('~/capstone/splunk/etc/apps/Capstone/lookups/' + 'Activities' + '.csv', index = False)


