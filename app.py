import os

import streamlit as st
from dotenv import load_dotenv

from apputil import *


st.write(
'''
# Week x: [Title]

...
''')

load_dotenv()

# constants
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

# Exercise 1
genius = Genius(access_token=ACCESS_TOKEN)

# Exercise 2
genius.get_artist("Radiohead")

# Exercise 3
genius.get_artists(['Rihanna', 'Tycho', 'Seal', 'U2'])
