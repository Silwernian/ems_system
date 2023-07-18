import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Exercises Mapping System", page_icon='\U0001F64A')

st.title(':violet[Exercises Mapping System]')
st.caption(':violet[-Database Request]')

st.divider()

st.markdown('')
st.markdown(
    '''
Pages นี้สร้างขึ้นมาเพื่อใช้ประกอบ Request ขอ Database ใหม่สำหรับ Exercises Pool เพื่อใช้ใน Exercises Mapping System (EMS)
'''
)
st.markdown(
    '''
:violet[**Contents Pages:**]
1. \U00002753 :red[**Exercises Data**]
    - เป็นตัวอย่าง Exercises เพื่อแสดง Components ต่างๆในหน้า Exercise.
2. \U00002705 :green[**Solution Data**]
    - เป็นตัวอย่าง Solutions เพื่อแสดง Components ต่างๆในหน้า Solution.
3. \U00002728 :orange[**Hint Data**]
    - เป็นตัวอย่างหน้า Hint (incomplete: wait MCK).
4. \U0001F333 :green[**Structure Tags**]
    - ประกอบด้วย Master Structure และ Keyword Pool ซึ่งเป็น Tags หลักที่ใช้ Connect ทุกอย่างเข้าหากัน.
5. \U0001F4D1 **Other Tags**
    - Tags อื่นๆสำหรับ Generate Exercises On-Demand.

เข้าชม Pages ต่างๆได้ผ่าน Side Bar ด้านซ้ายมือ
'''
)
st.write(':orange[**Plz view this page in dark mode, ปรับได้ที่มุมบนขวา**]')

st.divider()