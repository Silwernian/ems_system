import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Exercises Data", page_icon='\U00002753')

st.header(':red[**Exercises Data**] ❓')
st.markdown(
    '''
หน้านี้จะเป็นตัวอย่าง Exercises และ Components ต่างๆที่อยากให้มีใน Exercises''')
st.markdown(
    '''
Idea หลักคือ: :blue[อยากให้คนออกโจทย์สามารถ Design หน้าตาของโจทย์เองได้]
''')

st.markdown(
    '''
ในที่นี้อยากให้มองแต่ละ Components ของ Exercises แยกออกจากกันเป็นกล่องๆใน Container ตัวหนึ่ง โดย
* มี Layout มาให้ว่า มีกี่กล่อง แต่ละกล่องเรียงยังไง แต่ให้ User(คนออกโจทย์) เติม Contents ลงใน Container เอง
* Container แบ่งออกเป็น 3 ประเภทหลักๆ คือ:
    - Markdown Box: เป็น Container สำหรับ Text และ LaTeX ใช้สำหรับพิมพ์โจทย์
    - Figure Box: เป็น Container สำหรับ Upload Figure ประกอบโจทย์
    - Interactive Box: เป็น Container สำหรับ Plot กราฟ, วีดีโอ, Radio Buttons, Chk box, Data Table, . . .

ด้านล่างนี้จะเป็นตัวอย่างแค่ Layout เดียวคือ 3 กล่อง (1 กล่องใหญ่ด้านบน, 2 กล่องเล็กด้านซ้าย/ขวา)
'''
)

st.divider()

tab = st.tabs(['Ex 1: Interactive Plot', 'Ex 2: Table Answer','Layout'])

with tab[2]:
    question0 = st.form('My Form')
    with question0:
        st.header(':blue[. . . . . . นี่คือตัวอย่าง Markdown Box . . .  . . . . ]')
        st.write('ทำเป็น Container เปล่าๆตาม Template ไว้ แล้วให้คนออกโจทย์เลือกเองว่าจะเติมอะไรลงไปด้านใน')
        st.write('**Exercises 1: . . . . . . . . . . . . . . **')
        st.write('$Equation 1$')
        st.write('.')
        st.write('.')
        st.write('.')
        st.write('The question is . . .')
        submit00 = st.form_submit_button("Confirm ตัวโจทย์")

    col0 = st.columns(2)
    with col0[0]:
        with st.form('form01'):
            st.subheader(':blue[Figure Box]')
            st.write('.')
            st.write('.')
            st.write('.')
            st.write('.')
            submit00 = st.form_submit_button("Confirm ภาพประกอบโจทย์")

        fig0 = st.file_uploader(label='Zone สำหรับ Upload Figure ประกอบโจทย์')
    
    with col0[1]:
        with st.form('form02'):
            st.subheader(':blue[Zone สำหรับเขียน Choices]')
            st.write('.')
            st.write('.')
            st.write('.')
            st.write('.')
            st.write('.')
            st.write('.')
            st.write('.')
            submit00 = st.form_submit_button("Confirm Choices")

with tab[0]:
    st.markdown(
        '''
Exercises 1: ภาพด้านล่างแสดง Surface Plot ของ Function พร้อม Contour Line ของมัน
'''
    )
    st.write('จงหาว่าฟังก์ชันนี้คืออะไร')

    col1 = st.columns(2)
    with col1[0]:
        X = np.linspace(-50,50,200)
        Y = np.linspace(-50,50,200)
        y,x = np.meshgrid(X,Y)
        z = x**2 - y**2
        surface = go.Surface(x=x,y=y,z=z)
        fig = go.Figure(surface)
        fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))

        fig.update_layout(template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
        st.caption('สามารถ Interact กับ Plot นี้ได้')

    with col1[1]:
        options = [
        "1. $ f (x,y) = x^2 + y^2 $",
        "2. $ f (x,y) = x^2 - y^2 $",
        "3. $ f (x,y) = 2x - 2y $",
        "4. $ f (x,y) = 2x + 2y $"
        ]
        st.write('ลองฝึกจับเวลาดูไหม. . .')
        cc = st.columns(2)
        with cc[0]:
            st.button(':green[เริ่มจับเวลา]')
        with cc[1]:
            st.button(':red[หยุดเวลา]')
        ans1 = st.radio('ตัวเลือก',options)
        st.write(":orange[คำตอบของฉันคือ: ]",ans1)
        st.button('ส่งคำตอบ')
    st.write('ฟังเพลงเพลินๆระหว่างคิดเลข . . .')
    st.audio('gate_of_steiner.mp3', start_time=0)

with tab[1]:
    st.write('Exercises 2: จากข้อมูลที่ให้มา จงเติมตัวเลขลงในตารางให้ถูกต้อง')
    col2 = st.columns(2)
    with col2[0]:
        st.image('table_question.png')
    with col2[1]:
        df = pd.read_csv('cattles.csv')
        st.dataframe(df)
        st.caption('ถ้า Interact กับตารางได้จะดีมาก เช่น Click แล้ว Source Data')

st.divider()

    
   