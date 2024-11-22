import streamlit as st

#Create form and submit it

Employee_Name=st.text_input("Enter your name :")
Company_name=st.text_input("Enter your company name :")
Office_Address= st.text_area("Enter your address : ")   #text_area for large data 
Department_name=st.selectbox("Enter your department : ",('IT','Sales','Finance','HR'))
button=st.button("Submit")
if button:
    st.markdown(f"""
                Employee Name: {Employee_Name}
                Company name: {Company_name}     
                Office Address: {Office_Address} 
                Department: {Department_name}  
                """  
                )
