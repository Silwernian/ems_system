import streamlit as st
import os
from PIL import Image

import numpy as np
import plotly.express as px
import pandas as pd

st.set_page_config(page_title='Training Prototype', page_icon=None, layout="wide")

#----Header Zone----#
st.title('ยินดีต้อนรับเข้าสู่ระบบ :violet[**Exercise Designer**]')

st.divider()

#----Tagging Zone----#
st.subheader(':red[Tagging Zone]')

Subj_list = ['Physics']
Zone_list = ['Zone_1','Zone_2','Zone_3']
Topic_list = ['Top_1','Top_2','Top_3']
SubTopic_ist = ['Sub_1','Sub_2','Sub_3']
Lesson_list = ['Lesson_1','Lesson_2','Lesson_3']

master = st.columns(5)
master[0].selectbox(':orange[**Subject**]',Subj_list,key='Subject')
master[1].selectbox(':orange[**Zone**]',Zone_list,key='Zone')
master[2].selectbox(':orange[**Topic**]', Topic_list,key='Topic')
master[3].selectbox(':orange[**Subtopic**]',SubTopic_ist,key='Subtopic')
master[4].selectbox(':orange[**Lesson**]',Lesson_list,key='Lesson')

keyword_pool = ['เต่า','กระต่าย','หมา','แมว','หมู','แอปเปิ้ล','มะละกอ','กล้วย','ส้ม']

keyword = st.columns(5)
keyword[0].selectbox(':orange[**$1^{st} Keyword$**]',keyword_pool,key='kw1')
keyword[1].selectbox(':orange[**$2^{nd} Keyword$**]',keyword_pool,key='kw2')
keyword[2].selectbox(':orange[**$3^{rd} Keyword$**]',keyword_pool,key='kw3')
keyword[3].selectbox(':orange[**$4^{th} Keyword$**]',keyword_pool,key='kw4')
keyword[4].selectbox(':orange[**$5^{th} Keyword$**]',keyword_pool,key='kw5')

diff_col = st.columns([1,5])
diff_lvl = diff_col[0].number_input('Difficulty Score',min_value=0,max_value=10,step=1,key='diff_lvl')
if diff_lvl >= 0 and diff_lvl <= 2:
    diff_col[1].subheader('')
    diff_rank = diff_col[1].subheader('Difficulty Grade: :green[C]')
elif diff_lvl >= 3 and diff_lvl <= 5:
    diff_col[1].subheader('')
    diff_rank = diff_col[1].subheader('Difficulty Grade: :blue[B]')
elif diff_lvl >= 6 and diff_lvl <= 8:
    diff_col[1].subheader('')
    diff_rank = diff_col[1].subheader('Difficulty Grade: :orange[A]')
elif diff_lvl >= 9 and diff_lvl <= 10:
    diff_col[1].subheader('')
    diff_rank = diff_col[1].subheader('Difficulty Grade: :red[S]')

st.divider()

#----Design and Preview Zone----#
st.subheader(':red[Design Zone]')
design, preview = st.columns(2,gap='medium')

example_txt = ''':monkey: :blue[**Exercises 1:**] This is an example on how to create a markdown exercises . . .   
This is an example of how to type in an :orange[Inline LaTeX Equation:] :red[$\; y=mx+c\;$]   
and this is an example of a :orange[multiple lines equation]      
$$
Riemann \; Sum = \sum_{i=1}^{n} f(x_i)\Delta x_i \\;
$$

Which choice is the :red[*Incorrect*] answer :question:
'''
question = design.text_area(':balloon: :green[**พิมพ์โจทย์ที่นี่ (ในรูป Markdown)**] :balloon:',example_txt,height=200)
preview.write(':balloon: :green[**Exercise Preview**] :balloon:')
question_preview = preview.markdown(question)


with design:
    design_choice, design_image = st.columns(2)
    ch_width = design_choice.number_input("Left Width", min_value=1, max_value=10, step=1,key='ch_width')
    image_width = design_image.number_input("Right Width", min_value=1, max_value=10, step=1,key='img_width')
    buff_width = design_image.number_input("Buffer Width", min_value=1, max_value=10, step=1,key='buffer_width')
    illus_upload = design_image.file_uploader('Upload your image here !!')
    ch1 = design_choice.text_area('Choice 1','this is your first choice',height=10)
    ch2 = design_choice.text_area('Choice 2','my answer is $\\int f(x)dx$',height=10)
    ch3 = design_choice.text_area('Choice 3','I choose this answer',height=10)
    ch4 = design_choice.text_area('Choice 4','choice 4',height=10)
    ch5 = design_choice.text_area('Choice 5','choice 5',height=10)

    ch_correct = design_choice.number_input('The Correct Answer Is:', min_value=1, max_value=5)

    choice = [ch1, ch2, ch3, ch4, ch5]

with preview:
    preview_choice, preview_image, preview_buffer = st.columns([ch_width,image_width,buff_width])
    if illus_upload is not None:
        illus = Image.open(illus_upload)
        preview_image.image(illus,use_column_width=True)

    ch_preview = []
    for i in range(5):
        ch_preview.append(preview_choice.checkbox(f'{i+1} . {choice[i]}', key=f'ch_preview{i}'))

    for i in range(5):
        if i+1 != int(ch_correct):
            if ch_preview[i] == True:
                preview_choice.write(':sob: :blue[**Noooooooo**] :sob:')
        elif i+1 == int(ch_correct) and ch_preview[i] == True:
            preview_choice.write(':balloon: :green[**CongratZ!!**] :balloon:')
            st.balloons()


      
    
    
