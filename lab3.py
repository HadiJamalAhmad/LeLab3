import time
import streamlit as st
import streamlit.components.v1 as components
# importing numpy and pandas to work with sample data.
import numpy as np
import pandas as pd 
import codecs, threading
from functools import wraps


st.title('lab3')


st.text('This is the lab3.  ')

data = pd.read_csv("uber-raw-data-apr14.csv")

data["Date/Time"] = data["Date/Time"].map(pd.to_datetime)

def get_dom(dt):
    return dt.day
def get_weekday(dt):
    return dt.weekday()
def get_hours(dt):
    return dt.hour

@st.cache(allow_output_mutation=True)
# (allow_output_mutation=True) to suppress cache error
def benchmark(fn):
    def _timing(*a, **kw):
        st = time.perf_counter()
        r = fn(*a, **kw)
        print(f"{fn.__name__} execution: {time.perf_counter() - st} seconds")
        print(f"function benchmark : {fn.__name__} execution: {time.perf_counter() - st} seconds", file=open("tplab3.txt", "a"))
        return r

    return _timing

@benchmark
def your_test():
    print("IN")
    time.sleep(1)
    print("OUT")

your_test()   

@st.cache(allow_output_mutation=True)
# (allow_output_mutation=True) to suppress cache error
def data_hours(data):
    data["hours"] = data["Date/Time"].map(get_hours)
    def benchmark(fn):
        def _timing(*a, **kw):
            st = time.perf_counter()
            r = fn(*a, **kw)
            print(f"{fn.__name__} execution: {time.perf_counter() - st} seconds")
            print(f"function data_hours : {fn.__name__} execution: {time.perf_counter() - st} seconds", file=open("tplab3.txt", "a"))
            return r
        
        return _timing

    @benchmark
    def your_test():
        print("IN")
        time.sleep(1)
        print("OUT")

    your_test()
  
        
    return data



data_hours_var = data_hours(data)


def data_dom(data):
    data["dom"] = data["Date/Time"].map(get_dom)
    return data

data_dom_var = data_dom(data)

def data_weekday(data):
    data["weekday"] = data["Date/Time"].map(get_weekday)
    return data

data_weekday_var = data_dom(data)




chart_data = pd.DataFrame(
np.random.randn(20, 3),
columns=['hours', 'dom', 'weekday'])
st.line_chart(chart_data)


map_data = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
columns=['lat', 'lon'])
st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
np.random.randn(20, 3),
columns=['lat', 'lon', 'hours'])
chart_data

option = st.sidebar.selectbox(
'Which number do you like best?',
data_hours_var)
'You selected:', option

left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
           right_column.write("Woohoo!")
expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
# Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
bar.progress(i + 1)
time.sleep(0.1)

components.iframe("https://docs.streamlit.io/en/latest")
components.iframe("https://www.efrei.fr/?gclid=CjwKCAjwhaaKBhBcEiwA8acsHESfvOBDYrZ-7ZgvmAuCgP4xCmNNxqPW85hpLz8W2LE4HVfpZgYV9xoCWV8QAvD_BwE")

'...and now we\'re done!'





    





