import streamlit as st
import numpy as np
import time

st.set_page_config("Dad Joke Database", "🤣", "wide", "expanded")

def addJoke(p1, p2):
    
    currentjokes = open("jokes.txt", "r").read()
    newjokes = currentjokes + f"\n{p1} | {p2}"

    open("jokes.txt", "w").write(newjokes)

def pause(secs):
    try:
        time.sleep(secs)
    except:
        pass

st.title("Dad Joke Database")
st.write("---")

sidebar = st.sidebar
mode = st.radio("**Mode:**", ["Get a Joke", "Add a Joke"])

read = open("jokes.txt", "r").read()
rawlst = read.split("\n")
linelst = []
jokes = []

for line in rawlst:
    if line != "":
        linelst.append(line)

for joke in linelst:

    addjoke = []

    for part in joke.split(" | "):
        addjoke.append(part)

    jokes.append(addjoke)

st.write(jokes)

if mode == "Get a Joke":

    jokeindex = np.random.randint(0, len(jokes))

    if st.button("**Get a Joke**"):

        st.write(jokes[jokeindex][0])
        pause(2)
        st.write(jokes[jokeindex][1])

else:
    
    st.write(":grey[Note: Markdown bold and/or italic text formats are supported.]")

    c1, c2 = st.columns(2)

    p1 = c1.text_input("**Question/Context:**")
    p2 = c2.text_input("**Answer/Punchline:**")

    if st.button("Add Joke"):
            
        if p1 == "":
            st.write("**You need a question or context!**")

        elif p2 == "":
            st.write("**You need a punchline or an answer!**")

        else:

            try:
                addJoke(p1, p2)
                st.success("The joke was added successfully.")
            except:
                st.error("The joke could not be added.")

if sidebar.button("Refresh"):
    sidebar.success("Page refreshed successfully.")

if sidebar.download_button("Download Jokes", open("jokes.txt", "r").read(), "jokes.txt"):
    sidebar.success("Jokes downloaded successfully.")
