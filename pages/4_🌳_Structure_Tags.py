import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Structure Tags", page_icon='\U0001F333')

st.header(':green[**Structure Tag**] 🌳')
st.divider()
st.subheader(':blue[Master Structure]')
st.markdown(
    '''
:blue[Master Structure] เป็นโครงสร้างหลักที่บอกว่า Exercises ในแต่ละข้อนั้นอยู่ในส่วนไหนของเนื้อหา   
โดย :orange[Head of Subject] จะเป็นคงสร้าง Structure ตัวนี้ไว้ว่ามีอะไรบ้าง คนคีย์ข้อมูลเลือกเอาจากโครงสร้างที่ Pre-Defined นี้
:blue[Master Structure Hierarchy]
* :red[Subject:]   
บอกว่า Exercises ข้อนี้อยู่ในวิชาไหน
* :red[Zone:]   
บอกว่า Exercises ข้อนี้อยู่ในหมวดไหน เช่น Geometry, Algebras, Number Theory, . . . (ไม่มีในโครงสร้างปัจจุบัน)
* :red[Main Topic:]   
บอกว่า Exercises ข้อนี้อยู่ใน หัวข้อหลัก ไหน (เทียบเท่า Level ในปัจจุบัน)
* :red[Sub Topic:]   
บอกว่า Exercises ข้อนี้อยู่ใน หัวข้อย่อย ไหน (เทียบเท่า SubLevel ในปัจจุบัน)
* :red[Lesson:]   
บอกว่า Exercises ข้อนี้อยู่ใน บทเรียน ไหน (เทียบเท่า Sheet ในปัจจุบัน)   
'''
)

master = {'UID': ['001','002','003'],
          'Subject': ['Eng','Physics','Math'],
          'Zone': ['Part of Speech', 'Mechanics', 'Geometry'],
          'MainTopic': ['Verbs','Work-Energy','Euclidean Shape'],
          'SubTopic': ['Type of Verbs','Work','Triangle'],
          'Lesson':['Infinitive','Work of a constant Force','Properties of a Triangle']}
st.table(master)

st.divider()

st.header(':blue[Keyword Pools]')
st.markdown(
    '''
:blue[Keyword Pool] จะเป็น Additional Information ต่อท้ายตัว Exercises ที่มีที่อยู่ใน :blue[Master Structure] แล้ว   
หลักการคือ สำหรับแต่ละ :violet[**Lesson**] ตัว :orange[Head of Subject] จะสร้าง :blue[**Keyword Pool**] ขึ้นมากองหนึ่ง   
จากนั้นคนคีย์ข้อมูลจะเลือกจาก Keyword พวกนี้เพื่อแปะต่อท้าย Exercises แต่ละข้อ (เพิ่มเป็นอีก Column ใน DataFrame)    
- :blue[Keyword] จะเป็นตัวที่ใช้สำหรับ Search / Link Exercises เข้ากับระบบอื่นๆในระบบ
- สาเหตุที่ต้องมี :blue[Master Structure] และ :blue[Keyword Pool] คือความ Uniform ของ Keyword ที่จะแปะกับ Exercises ในแต่ละข้อ
- การที่คนคีย์ข้อมูลเลือกจาก Pre-Defined Structure ทำให้เรามั่นใจได้ว่าจะไม่มีกรณีที่แต่ละคนจะคีย์ไม่เหมือนกัน ได้  

:red[**Important Note:**] Keyword สำหรับ Exercises ในแต่ละข้อ :red[ต้องมี Hierarchy] คือ Keyword ตัวแรกต้องมีน้ำหนักในการ Search มากกว่าตัวอื่นๆ
เพราะฉะนั้นในการเก็บ DataBase ต้องมีข้อมูลเรื่อง Heirarchy ของ Keyword ตัวนี้อยู่ด้วย   
:orange[**ตัวอย่างเช่น**] โจทย์เรื่อง Matrix อาจจะมี #การแก้สมการ #รากที่สอง ผสมอยู่ด้วย แต่ว่าจะอยู่ในตัวท้ายๆ เพราะฉะนั้นเวลาระบบจะ Search หา #การแก้สมการ ก็ควรจะเอาตัวอื่นที่มี #การแก้สมการ เป็น Keyword ตัวแรกๆก่อน
แล้วค่อยมาหยิบเอาโจทย์ข้อนี้ หากไม่มีข้ออื่นเหลือจริงๆ
'''
)
st.divider()