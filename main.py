from posixpath import expanduser
from threading import Condition
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit Start")

st.write("Progress Bar")
"Start"

latest_iteration=st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f"Iteration{i+1}")
  bar.progress(i+1)
  time.sleep(0.3)

"Done!!!"
  

left_column,central_column,right_column = st.columns(3)
button = left_column.button("右カラムに文字を表示")
if button:
  left_column.write("ここは左からむ")
  central_column.write("ここは中央からむ")
  right_column.write("ここは右からむ")
  
expander1 = st.expander("問い合わせ1")
expander1.write("問い合わせ内容を書く")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ内容を書く")
expander3 = st.expander("問い合わせ3")
expander3.write("問い合わせ内容を書く")

# text = st.text_input("あなたの趣味を教えてください")
# condition=st.slider("あなたの今の調子は?",0,100,20)
# "あなたの趣味は",text,"です"
# "コンディション", condition,"です"