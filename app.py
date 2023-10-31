import numpy as np
import streamlit as st

st.video("https://static.streamlit.io/examples/star.mp4", autoplay=True)

sample_rate = 44100  # 44100 samples per second
seconds = 5  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate, autoplay=True)

