import streamlit as st
import datetime
import requests
import json
'''
# Welcome to your NY taxi fare prediction!
'''

st.markdown('''
In the following, we will need your route information to predict your estimated taxi fare.

Please provide your information to us:
''')


d = st.date_input(
    "On which day are you going to take a cab?",
    datetime.date(2024, 9, 10))
st.write('On the following day: ', d)
t = st.time_input('At which time are you going?', datetime.time(8, 45))
st.write('Time: ', t)
pickup_time = f"{d} {t}"
st.write("Datetime: ", pickup_time)


option = st.slider('Select the total number of passengers:', 1, 8, 1)
st.write('The current number is ', option)
passenger_count = option


"In the following, enter the pickoff and dropoff coordinates. Values must be between 40 and 41 for latitude and -73 and -75 for longitude"
pickup_longitude = st.number_input('Pickup longitude: ', key = 1)
pickup_latitude = st.number_input('Pickup latitude: ',  key = 2)
dropoff_longitude = st.number_input('Dropoff longitude',  key = 3)
dropoff_latitude = st.number_input('Dropoff latitude', key = 4)



url = 'https://taxifare.lewagon.ai/predict'

#Dict with Params
params = {"pickup_datetime":pickup_time, "pickup_longitude":pickup_longitude, "pickup_latitude": pickup_latitude,
         "dropoff_longitude":dropoff_longitude, "dropoff_latitude": dropoff_latitude,  "passenger_count": passenger_count}

#API request
x = requests.get(url, params = params)

#Output results
output = x.content
data = json.loads(output)
fare = data["fare"]

st.write("Your fare will be: ", fare)
