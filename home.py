import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt


add_selectbox = st.sidebar.selectbox(
    "목차",
    ("체질량 계산기", "갭 마인더", "마이 페이지")
)

if add_selectbox == '체질량 계산기':
    



    st.write(" # 체질량 계산기")

    height = st.number_input('키를 입력하세요. (cm)',50,300,170)
    st.write('키:', height,'cm')

    weight = st.number_input('몸무게를 입력하세요. (kg)')
    st.write('몸무게:',weight,'kg')

    bmi = weight/((height/100)**2)

    def bmi_call(bmi):
        if bmi >= 30:
            st.write('당신은 초고도비만입니다.')
        elif bmi >= 25:
            st.write('당신은 고도비만입니다.')
        elif bmi >= 23:
            st.write('당신은 과체중입니다.')
        elif bmi >= 18.5:
            st.write('당신은 정상입니다.')
        else:
            st.write('당신은 저체중입니다.')


    if st.button('계산'):
        st.balloons()
        st.write('당신의 체질량 지수는',round(bmi,2),'입니다.')
        bmi_call(bmi)
        image = Image.open('gun.jpg')

        st.image(image, caption='get start new game')

elif add_selectbox == '갭 마인더':
    st.write('# 여기는 갭 마인더입니다.')

    data = pd.read_csv('gapminder.csv')

    st.write(data)

    colors = []
    for x in data['continent']:
        if x == 'Asia':
            colors.append('tomato')
        elif x == 'Europe':
            colors.append('blue')
        elif x == 'Africa':
            colors.append('olive')
        elif x == 'Americas':
            colors.append('green')
        else:
            colors.append('orange')
    data['colors'] = colors

    year = st.slider('년도를 선택하세요.', 1952, 2007, 1952, step = 5)
    st.write("선택 년도는", year, '입니다.')


    data = data[data['year']==year]

    fig, ax = plt.subplots()

    ax.scatter(data['gdpPercap'],data['lifeExp'],s=data['pop']*0.000002, color = data['colors'])
    ax.set_title('How Does Gdp per Capital relate to Life Expetancy?')
    ax.set_xlabel('Gdp per Capital')
    ax.set_ylabel('Life Expectancy')
    st.pyplot(fig)



else:
    st.write('# 여기는 마이 페이지입니다.')