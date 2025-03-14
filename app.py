import streamlit as st

st.set_page_config(page_title= "Growth Mindset Project", page_icon = "★")
st.title("Growth Mindset Ai project")

st.header("Welcome to the Your Growth Journey")
st.write("Embarce challege, learn from mistakes, and unlock your full potential. this is AI-powered app helps you build growth mindset wit reflection,callenge and achivement")

st.header("Today's Growt MIndset Quote")
st.write(" “sucess is not final, failure is not fatel: it is the courage to contiue.”  - Winston Churuchill")
 
st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

#condition
if user_input :
    st.success(f"you;re are facing : {user_input}. keep pusing forward toward your goal")
else :
    st.warning("Tell us about yuor challenge to get started!")

    #reflection

    st.header("Reflection on your Learning")
    reflection = st.text_area("write your reflection here:")
    
    if reflection :
        st.sucess(f"great inside! your reflection {reflection}")
    else:
        st.info("Reflection on past experience hep you grwo! share your difficulties")

        #achinement
        st.header("Celebrate your Wins!")
        achivement = st.text_area("share something you've recently accomplished")

        if achivement:
            st.success(f"amazing! you achivement {achivement}")
        else:
            st.info("Big or small , every achivement counts! share one now")

            #footer
           
        st.write('- - - ')
        st.write('keep believe in yourself. Growt is a journy, nt a destination')
        st.write("**created by Shaheryar**")
