import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Hint Data", page_icon='\U00002728')

st.header(':orange[Hint Data] ✨')

st.markdown(
    """
ในส่วนของตัว Hint อยาก Design ไว้แค่ Typical Hint ก่อน
- เหมือนตัวกล่อง Markdown ของ Exercises ที่พิมพ์ลงไปได้
- Upload ภาพประกอบลงไปได้ และแดสงผลแบบต่อเนื่องได้ (โชว์ทีละภาพ ต่อๆกัน)

อาจต้องมีที่เก็บข้อมูลเพิ่มเติมสำหรับตัว AI Hint ที่จะเข้ามา :violet[@Micky]
"""
)
