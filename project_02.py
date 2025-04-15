import streamlit as st
import re

st.title ("PASSWORD STRENGHT METER")
st.markdown("""## HI!
            
HERE'S Easy To Make Your Password Stronger.
            """)
password =st.text_input("Enter Your Password", type="password")

feedback = []

score = 0

if password :
    if len(f'(password)') >=9:
        score +=1
    else:
        feedback.append("wrong, password should be atleast 8 character long.")
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]' , password):
        score +=1
    else:
        feedback.append(" wrong, password should contain include both upper and lower case character.")
    if re.search(r'[\d]',password):
        score +=1
    else:
        feedback.append("wrong, password should contain atleast one digit.")
    if re.search(r'[@$&":/.]',password):
        score +=1
    else:
        feedback.append("wrong, you must have use some special chsracter.")


    if score == 4:
        feedback.append("now! your password is stronger.")
    elif score == 3:
        feedback.append("if your password is medium strenght,it could be break.")
    else:
        feedback.append("your password is loser , please! make it stronger.")
    if feedback:
        st.markdown("## improvement suggestion.")
        for tip in feedback:
            st.write(tip)        

else:
    st.info("enter your password to get started.")
    