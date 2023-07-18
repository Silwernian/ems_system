import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Solution Data", page_icon='\U00002705')

st.header(':green[Solution Data] ✅')
st.markdown(
    """
ในแง่ Structure ตัว Solution จะเหมือนกับ Exercises เลย ต่างกันที่
- เพิ่มความสามารถในการ Upload VDO Solution ได้
- ถ้าเป็นไปได้อยากให้มีการ Upload ภาพได้หลายภาพ แล้วกดเล่นทีละภาพ Step-by-step แบบ Mini Animation 
"""
)




st.divider()

tab = st.tabs(['Soln 1: Typical Solution', 'Ex 2: VDO Solution'])

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
        ans1 = st.radio('ตัวเลือก',options)
        st.write(":orange[คำตอบของฉันคือ: ]",ans1)
        st.success('คำตอบที่ถูกต้องคือ ข้อ 8.')
        st.write('เพราะว่า')
        st.write('bla bla bla')
        st.write('.')
        st.write('.')

with tab[1]:
    st.write('Exercises 2: จากข้อมูลที่ให้มา จงเติมตัวเลขลงในตารางให้ถูกต้อง')
    col2 = st.columns(2)
    with col2[0]:
        st.image('table_question.png')
    with col2[1]:
        df = pd.read_csv('cattles.csv')
        st.dataframe(df)
        st.success('พี่ Meth จะมาเฉลยให้ด้านล่างเลยจ้าาา')
        st.video('meth_soln.mp4')

st.divider()

    