import streamlit as st
from PIL import Image

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