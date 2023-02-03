## //* Speech to text application where user speaks a prompt for the AI image creator and it creates an image and displays it automatically, kind of like a real-time art show—- imagine if there was a big screen standing up in front of you and you spoke ehat you wanted to see and it would create it and display a few seconds later, could be acool thing to have in house
# //* Make with python

# //* Dont need a database, or can have a very simple MongoDB one where users can store the image

### info about how to do text to speech and speech to text
# https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/

# the application will ask out in speech "What would you like to create?"
#You speak your details "a man in a blue sweater and red hat in the ocean"
# application shows the words on the screen and asks you to confirm
# if confirm then it creataes the AI pic

import streamlit as st

st.set_page_config(layout="wide")


st.title("AI Art")
st.subheader("A speech to AI art creator")
st.write("Welcome to AI Art. An application where you can tell the computer what image you would like to be created and then it will appear right before you. This is using the power of speech-to-text and then word-to-art AI art generator.")

st.subheader("Here are just a few examples of art and their speech prompts...")

col1, col2 = st.columns(2)


with col1:
    st.image("images/Burning Man.png", width=200)
    st.write("Burning Man music festival infront of the galaxy")
    st.image("images/Cyborg.png", width=200)
    st.write("A cyborg smoking a cigarette while standing in a train station")

with col2:
    st.image("images/Jumping.png", width=200)
    st.write("A man jumping off a cliff into a nebula")
    st.image("images/Nostalgia.png", width=200)
    st.write("Listening to nostalgic music in the style of Salvador Dali")
