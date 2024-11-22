import streamlit as st
import pandas as pd

################################################

#Display data on web page

st.title("Welcome to Unique Python Classes !!")
st.header("Python")
st.subheader("Python is Awsome!!!strea")
st.markdown("Let's learn Python")
st.code(""" for in range(1,10,2):
               print("Hello All...")) """)

#################################################

#Display csv file data on web page

data=pd.read_csv("sample.csv")
st.dataframe(data)

###############################################

#Create form and submit it

Name=st.text_input("Enter your name :")
F_name=st.text_input("Enter your father name :")
Address= st.text_area("Enter your address : ")   #text_area for large data 
Class_name=st.selectbox("Enter your Class : ",(1,2,3,4,5,6,7,8,9,10))
button=st.button("Submit")
if button:
    st.markdown(f"""
                Name: {Name}
                Father name: {F_name}     
                Address: {Address} 
                Class: {Class_name}  
                """  
                )
