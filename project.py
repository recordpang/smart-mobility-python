import streamlit as st          # streamlit 라이브러리 불러오기
import matplotlib.pyplot as plt # matplotlib 라이브러리 불러오기
import pandas as pd             # pandas 라이브러리 불러오기

add_selectbox = st.sidebar.selectbox(
    "페이지 선택",
    ("MBTI 궁합보기", "한국의 MBTI비율과 인구수")
)

if add_selectbox == 'MBTI 궁합보기':
    st.write("# MBTI 궁합보기")


    mbti = st.select_slider( # 자신의 MBTI를 선택하기
        '자신의 MBTI를 선택해주세요.',
        options=['INFP','ENFP','INFJ','ENFJ','INTJ','ENTJ','INTP','ENTP','ISFP','ESFP','ISTP','ESTP','ISFJ','ESFJ','ISTJ','ESTJ'])
    st.write('당신의 MBTI는', mbti,'입니다.')

    oppo_mbti = st.select_slider( #상대방의 MBTI를 선택하기
        '상대방의 MBTI를 선택해주세요.',
        options=['INFP','ENFP','INFJ','ENFJ','INTJ','ENTJ','INTP','ENTP','ISFP','ESFP','ISTP','ESTP','ISFJ','ESFJ','ISTJ','ESTJ'])
    st.write('상대방의 MBTI는', oppo_mbti,'입니다.')

    st.write('궁합 점수는 1점부터 5점까지입니다.') #점수 안내
    if st.button('궁합보기'):   # 궁합보기 버튼을 누르면 선택한 MBTI에 따라 조건문을 통해 점수를 매겨줌
        if mbti == 'INFP' and oppo_mbti == 'INFP':
            st.write('4점!')
        elif mbti == 'INFP' and oppo_mbti == 'ENFP' or mbti == 'ENFP' and oppo_mbti == 'INFP':
            st.write('4점!')
        elif mbti == 'INFP' and oppo_mbti == 'INFJ' or mbti == 'INFJ' and oppo_mbti == 'INFP':
            st.write('4점!')
        elif mbti == 'INFP' and oppo_mbti == 'ENFJ' or mbti == 'ENFJ' and oppo_mbti == 'INFP':
            st.write('5점!')
        elif mbti == 'INFP' and oppo_mbti == 'INTJ' or mbti == 'INTJ' and oppo_mbti == 'INFP':
            st.write('4점!')
        elif mbti == 'INFP' and oppo_mbti == 'ENTJ' or mbti == 'ENTJ' and oppo_mbti == 'INFP':
            st.write('5점!')
        elif mbti == 'INFP' and oppo_mbti == 'INTP' or mbti == 'INTP' and oppo_mbti == 'INFP':
            st.write('1점!')
        elif mbti == 'INFP' and oppo_mbti == 'ENTP' or mbti == 'ENTP' and oppo_mbti == 'INFP':
            st.write('4점!')
        elif mbti == 'INFP' and oppo_mbti == 'ISFP' or mbti == 'ISFP' and oppo_mbti == 'INFP':
            st.write('1점!')
        elif mbti == 'INFP' and oppo_mbti == 'ESFP' or mbti == 'ESFP' and oppo_mbti == 'INFP':
            st.write('1점!')
        elif mbti == 'INFP' and oppo_mbti == 'ISTP' or mbti == 'ISTP' and oppo_mbti == 'INFP':
            st.write('1점!')
        elif mbti == 'INFP' and oppo_mbti == 'ESTP' or mbti == 'ESTP' and oppo_mbti == 'INFP':
            st.write('1점!')
        elif mbti == 'INFP' and oppo_mbti == 'ISFJ' or mbti == 'ISFJ' and oppo_mbti == 'INFP':
            st.write('1점!')
        elif mbti == 'INFP' and oppo_mbti == 'ESFJ' or mbti == 'ESFJ' and oppo_mbti == 'INFP':
            st.write('1점!')
        elif mbti == 'INFP' and oppo_mbti == 'ISTJ' or mbti == 'ISTJ' and oppo_mbti == 'INFP':
            st.write('1점!')
        elif mbti == 'INFP' and oppo_mbti == 'ESTJ' or mbti == 'ESTJ' and oppo_mbti == 'INFP':
            st.write('1점!')
        elif mbti == 'ENFP' and oppo_mbti == 'ENFP':
            st.write('4점!')
        elif mbti == 'ENFP' and oppo_mbti == 'INFJ' or mbti == 'INFJ' and oppo_mbti == 'ENFP':
            st.write('5점!')
        elif mbti == 'ENFP' and oppo_mbti == 'ENFJ' or mbti == 'ENFJ' and oppo_mbti == 'ENFP':
            st.write('4점!')
        elif mbti == 'ENFP' and oppo_mbti == 'INTJ' or mbti == 'INTJ' and oppo_mbti == 'ENFP':
            st.write('5점!')
        elif mbti == 'ENFP' and oppo_mbti == 'ENTJ' or mbti == 'ENTJ' and oppo_mbti == 'ENFP':
            st.write('4점!')
        elif mbti == 'ENFP' and oppo_mbti == 'INTP' or mbti == 'INTP' and oppo_mbti == 'ENFP':
            st.write('1점!')
        elif mbti == 'ENFP' and oppo_mbti == 'ENTP' or mbti == 'ENTP' and oppo_mbti == 'ENFP':
            st.write('4점!')
        elif mbti == 'ENFP' and oppo_mbti == 'ISFP' or mbti == 'ISFP' and oppo_mbti == 'ENFP':
            st.write('1점!')
        elif mbti == 'ENFP' and oppo_mbti == 'ESFP' or mbti == 'ESFP' and oppo_mbti == 'ENFP':
            st.write('1점!')
        elif mbti == 'ENFP' and oppo_mbti == 'ISTP' or mbti == 'ISTP' and oppo_mbti == 'ENFP':
            st.write('1점!')
        elif mbti == 'ENFP' and oppo_mbti == 'ESTP' or mbti == 'ESTP' and oppo_mbti == 'ENFP':
            st.write('1점!')
        elif mbti == 'ENFP' and oppo_mbti == 'ISFJ' or mbti == 'ISFJ' and oppo_mbti == 'ENFP':
            st.write('1점!')
        elif mbti == 'ENFP' and oppo_mbti == 'ESFJ' or mbti == 'ESFJ' and oppo_mbti == 'ENFP':
            st.write('1점!')
        elif mbti == 'ENFP' and oppo_mbti == 'ISTJ' or mbti == 'ISTJ' and oppo_mbti == 'ENFP':
            st.write('1점!')
        elif mbti == 'ENFP' and oppo_mbti == 'ESTJ' or mbti == 'ESTJ' and oppo_mbti == 'ENFP':
            st.write('1점!')
        elif mbti == 'INFJ' and oppo_mbti == 'INFJ':
            st.write('4점!')
        elif mbti == 'INFJ' and oppo_mbti == 'ENFJ' or mbti == 'ENFJ' and oppo_mbti == 'INFJ':
            st.write('4점!')
        elif mbti == 'INFJ' and oppo_mbti == 'INTJ' or mbti == 'INTJ' and oppo_mbti == 'INFJ':
            st.write('4점!')
        elif mbti == 'INFJ' and oppo_mbti == 'ENTJ' or mbti == 'ENTJ' and oppo_mbti == 'INFJ':
            st.write('4점!')
        elif mbti == 'INFJ' and oppo_mbti == 'INTP' or mbti == 'INTP' and oppo_mbti == 'INFJ':
            st.write('1점!')
        elif mbti == 'INFJ' and oppo_mbti == 'ENTP' or mbti == 'ENTP' and oppo_mbti == 'INFJ':
            st.write('5점!')
        elif mbti == 'INFJ' and oppo_mbti == 'ISFP' or mbti == 'ISFP' and oppo_mbti == 'INFJ':
            st.write('1점!')
        elif mbti == 'INFJ' and oppo_mbti == 'ESFP' or mbti == 'ESFP' and oppo_mbti == 'INFJ':
            st.write('1점!')
        elif mbti == 'INFJ' and oppo_mbti == 'ISTP' or mbti == 'ISTP' and oppo_mbti == 'INFJ':
            st.write('1점!')
        elif mbti == 'INFJ' and oppo_mbti == 'ESTP' or mbti == 'ESTP' and oppo_mbti == 'INFJ':
            st.write('1점!')
        elif mbti == 'INFJ' and oppo_mbti == 'ISFJ' or mbti == 'ISFJ' and oppo_mbti == 'INFJ':
            st.write('1점!')
        elif mbti == 'INFJ' and oppo_mbti == 'ESFJ' or mbti == 'ESFJ' and oppo_mbti == 'INFJ':
            st.write('1점!')
        elif mbti == 'INFJ' and oppo_mbti == 'ISTJ' or mbti == 'ISTP' and oppo_mbti == 'INFJ':
            st.write('1점!')
        elif mbti == 'INFJ' and oppo_mbti == 'ESTJ' or mbti == 'ESTJ' and oppo_mbti == 'INFJ':
            st.write('1점!')
        elif mbti == 'ENFJ' and oppo_mbti == 'ENFJ':
            st.write('4점!')
        elif mbti == 'ENFJ' and oppo_mbti == 'INTJ' or mbti == 'INTJ' and oppo_mbti == 'ENFJ':
            st.write('4점!')
        elif mbti == 'ENFJ' and oppo_mbti == 'ENTJ' or mbti == 'ENTJ' and oppo_mbti == 'ENFJ':
            st.write('4점!')
        elif mbti == 'ENFJ' and oppo_mbti == 'INTP' or mbti == 'INTP' and oppo_mbti == 'ENFJ':
            st.write('1점!')
        elif mbti == 'ENFJ' and oppo_mbti == 'ENTP' or mbti == 'ENTP' and oppo_mbti == 'ENFJ':
            st.write('4점!')
        elif mbti == 'ENFJ' and oppo_mbti == 'ISFP' or mbti == 'ISFP' and oppo_mbti == 'ENFJ':
            st.write('5점!')
        elif mbti == 'ENFJ' and oppo_mbti == 'ESFP' or mbti == 'ESFP' and oppo_mbti == 'ENFJ':
            st.write('1점!')
        elif mbti == 'ENFJ' and oppo_mbti == 'ISTP' or mbti == 'ISTP' and oppo_mbti == 'ENFJ':
            st.write('1점!')
        elif mbti == 'ENFJ' and oppo_mbti == 'ESTP' or mbti == 'ESTP' and oppo_mbti == 'ENFJ':
            st.write('1점!')
        elif mbti == 'ENFJ' and oppo_mbti == 'ISFJ' or mbti == 'ISFJ' and oppo_mbti == 'ENFJ':
            st.write('1점!')
        elif mbti == 'ENFJ' and oppo_mbti == 'ESFJ' or mbti == 'ESFJ' and oppo_mbti == 'ENFJ':
            st.write('1점!')
        elif mbti == 'ENFJ' and oppo_mbti == 'ISTJ' or mbti == 'ISTJ' and oppo_mbti == 'ENFJ':
            st.write('1점!')
        elif mbti == 'ENFJ' and oppo_mbti == 'ESTJ' or mbti == 'ESTJ' and oppo_mbti == 'ENFJ':
            st.write('1점!')
        elif mbti == 'INTJ' and oppo_mbti == 'INTJ':
            st.write('4점!')
        elif mbti == 'INTJ' and oppo_mbti == 'ENTJ' or mbti == 'ENTJ' and oppo_mbti == 'INTJ':
            st.write('4점!')
        elif mbti == 'INTJ' and oppo_mbti == 'INTP' or mbti == 'INTP' and oppo_mbti == 'INTJ':
            st.write('1점!')
        elif mbti == 'INTJ' and oppo_mbti == 'ENTP' or mbti == 'ENTP' and oppo_mbti == 'INTJ':
            st.write('5점!')
        elif mbti == 'INTJ' and oppo_mbti == 'ISFP' or mbti == 'ISFP' and oppo_mbti == 'INTJ':
            st.write('3점!')
        elif mbti == 'INTJ' and oppo_mbti == 'ESFP' or mbti == 'ESFP' and oppo_mbti == 'INTJ':
            st.write('3점!')
        elif mbti == 'INTJ' and oppo_mbti == 'ISTP' or mbti == 'ISTP' and oppo_mbti == 'INTJ':
            st.write('3점!')
        elif mbti == 'INTJ' and oppo_mbti == 'ESTP' or mbti == 'ESTP' and oppo_mbti == 'INTJ':
            st.write('3점!')
        elif mbti == 'INTJ' and oppo_mbti == 'ISFJ' or mbti == 'ISFJ' and oppo_mbti == 'INTJ':
            st.write('2점!')
        elif mbti == 'INTJ' and oppo_mbti == 'ESFJ' or mbti == 'ESFJ' and oppo_mbti == 'INTJ':
            st.write('2점!')
        elif mbti == 'INTJ' and oppo_mbti == 'ISTJ' or mbti == 'ISTJ' and oppo_mbti == 'INTJ':
            st.write('2점!')
        elif mbti == 'INTJ' and oppo_mbti == 'ESTJ' or mbti == 'ESTJ' and oppo_mbti == 'INTJ':
            st.write('2점!')
        elif mbti == 'ENTJ' and oppo_mbti == 'ENTJ':
            st.write('4점!')
        elif mbti == 'ENTJ' and oppo_mbti == 'INTP' or mbti == 'INTP' and oppo_mbti == 'ENTJ':
            st.write('1점!')
        elif mbti == 'ENTJ' and oppo_mbti == 'ENTP' or mbti == 'ENTP' and oppo_mbti == 'ENTJ':
            st.write('4점!')
        elif mbti == 'ENTJ' and oppo_mbti == 'ISFP' or mbti == 'ISFP' and oppo_mbti == 'ENTJ':
            st.write('3점!')
        elif mbti == 'ENTJ' and oppo_mbti == 'ESFP' or mbti == 'ESFP' and oppo_mbti == 'ENTJ':
            st.write('3점!')
        elif mbti == 'ENTJ' and oppo_mbti == 'ISTP' or mbti == 'ISTP' and oppo_mbti == 'ENTJ':
            st.write('3점!')
        elif mbti == 'ENTJ' and oppo_mbti == 'ESTP' or mbti == 'ESTP' and oppo_mbti == 'ENTJ':
            st.write('3점!')
        elif mbti == 'ENTJ' and oppo_mbti == 'ISFJ' or mbti == 'ISFJ' and oppo_mbti == 'ENTJ':
            st.write('3점!')
        elif mbti == 'ENTJ' and oppo_mbti == 'ESFJ' or mbti == 'ESFJ' and oppo_mbti == 'ENTJ':
            st.write('3점!')
        elif mbti == 'ENTJ' and oppo_mbti == 'ISTJ' or mbti == 'ISTJ' and oppo_mbti == 'ENTJ':
            st.write('3점!')
        elif mbti == 'ENTJ' and oppo_mbti == 'ESTJ' or mbti == 'ESFTJ' and oppo_mbti == 'ENTJ':
            st.write('3점!')
        elif mbti == 'INTP' and oppo_mbti == 'INTP':
            st.write('1점!')
        elif mbti == 'INTP' and oppo_mbti == 'ENTP' or mbti == 'ENTP' and oppo_mbti == 'INTP':
            st.write('1점!')
        elif mbti == 'INTP' and oppo_mbti == 'ISFP' or mbti == 'ISFP' and oppo_mbti == 'INTP':
            st.write('1점!')
        elif mbti == 'INTP' and oppo_mbti == 'ESFP' or mbti == 'ESFP' and oppo_mbti == 'INTP':
            st.write('1점!')
        elif mbti == 'INTP' and oppo_mbti == 'ISTP' or mbti == 'ISTP' and oppo_mbti == 'INTP':
            st.write('1점!')
        elif mbti == 'INTP' and oppo_mbti == 'ESTP' or mbti == 'ESTP' and oppo_mbti == 'INTP':
            st.write('1점!')
        elif mbti == 'INTP' and oppo_mbti == 'ISFJ' or mbti == 'ISFJ' and oppo_mbti == 'INTP':
            st.write('1점!')
        elif mbti == 'INTP' and oppo_mbti == 'ESFJ' or mbti == 'ESFJ' and oppo_mbti == 'INTP':
            st.write('1점!')
        elif mbti == 'INTP' and oppo_mbti == 'ISTJ' or mbti == 'ISTH' and oppo_mbti == 'INTP':
            st.write('1점!')
        elif mbti == 'INTP' and oppo_mbti == 'ESTJ' or mbti == 'ESTJ' and oppo_mbti == 'INTP':
            st.write('1점!')
        elif mbti == 'ENTP' and oppo_mbti == 'ENTP':
            st.write('4점!')
        elif mbti == 'ENTP' and oppo_mbti == 'ISFP' or mbti == 'ISFP' and oppo_mbti == 'ENTP':
            st.write('3점!')
        elif mbti == 'ENTP' and oppo_mbti == 'ESFP' or mbti == 'ESFP' and oppo_mbti == 'ENTP':
            st.write('3점!')
        elif mbti == 'ENTP' and oppo_mbti == 'ISTP' or mbti == 'ISTP' and oppo_mbti == 'ENTP':
            st.write('3점!')
        elif mbti == 'ENTP' and oppo_mbti == 'ESTP' or mbti == 'ESTP' and oppo_mbti == 'ENTP':
            st.write('3점!')
        elif mbti == 'ENTP' and oppo_mbti == 'ISFJ' or mbti == 'ISFJ' and oppo_mbti == 'ENTP':
            st.write('2점!')
        elif mbti == 'ENTP' and oppo_mbti == 'ESFJ' or mbti == 'ESFJ' and oppo_mbti == 'ENTP':
            st.write('2점!')
        elif mbti == 'ENTP' and oppo_mbti == 'ISTJ' or mbti == 'ISTJ' and oppo_mbti == 'ENTP':
            st.write('2점!')
        elif mbti == 'ENTP' and oppo_mbti == 'ESTJ' or mbti == 'ESTJ' and oppo_mbti == 'ENTP':
            st.write('2점!')
        elif mbti == 'ISFP' and oppo_mbti == 'ISFP':
            st.write('2점!')
        elif mbti == 'ISFP' and oppo_mbti == 'ESFP' or mbti == 'ESFP' and oppo_mbti == 'ISFP':
            st.write('2점!')
        elif mbti == 'ISFP' and oppo_mbti == 'ISTP' or mbti == 'ISTP' and oppo_mbti == 'ISFP':
            st.write('2점!')
        elif mbti == 'ISFP' and oppo_mbti == 'ESTP' or mbti == 'ESTP' and oppo_mbti == 'ISFP':
            st.write('2점!')
        elif mbti == 'ISFP' and oppo_mbti == 'ISFJ' or mbti == 'ISFJ' and oppo_mbti == 'ISFP':
            st.write('3점!')
        elif mbti == 'ISFP' and oppo_mbti == 'ESFJ' or mbti == 'ESFJ' and oppo_mbti == 'ISFP':
            st.write('5점!')
        elif mbti == 'ISFP' and oppo_mbti == 'ISTJ' or mbti == 'ISTJ' and oppo_mbti == 'ISFP':
            st.write('3점!')
        elif mbti == 'ISFP' and oppo_mbti == 'ESTJ' or mbti == 'ESTJ' and oppo_mbti == 'ISFP':
            st.write('5점!')
        elif mbti == 'ESFP' and oppo_mbti == 'ESFP':
            st.write('2점!')
        elif mbti == 'ESFP' and oppo_mbti == 'ISTP' or mbti == 'ISTP' and oppo_mbti == 'ESFP':
            st.write('2점!')
        elif mbti == 'ESFP' and oppo_mbti == 'ESTP' or mbti == 'ESTP' and oppo_mbti == 'ESFP':
            st.write('2점!')
        elif mbti == 'ESFP' and oppo_mbti == 'ISFJ' or mbti == 'ISFJ' and oppo_mbti == 'ESFP':
            st.write('5점!')
        elif mbti == 'ESFP' and oppo_mbti == 'ESFJ' or mbti == 'ESFJ' and oppo_mbti == 'ESFP':
            st.write('3점!')
        elif mbti == 'ESFP' and oppo_mbti == 'ISTJ' or mbti == 'ISTJ' and oppo_mbti == 'ESFP':
            st.write('5점!')
        elif mbti == 'ESFP' and oppo_mbti == 'ESTJ' or mbti == 'ESTJ' and oppo_mbti == 'ESFP':
            st.write('3점!')
        elif mbti == 'ISTP' and oppo_mbti == 'ISTP':
            st.write('2점!')
        elif mbti == 'ISTP' and oppo_mbti == 'ESTP' or mbti == 'ESTP' and oppo_mbti == 'ISTP':
            st.write('2점!')
        elif mbti == 'ISTP' and oppo_mbti == 'ISFJ' or mbti == 'ISFJ' and oppo_mbti == 'ISTP':
            st.write('3점!')
        elif mbti == 'ISTP' and oppo_mbti == 'ESFJ' or mbti == 'ESFJ' and oppo_mbti == 'ISTP':
            st.write('5점!')
        elif mbti == 'ISTP' and oppo_mbti == 'ISTJ' or mbti == 'ISTJ' and oppo_mbti == 'ISTP':
            st.write('3점!')
        elif mbti == 'ISTP' and oppo_mbti == 'ESTJ' or mbti == 'ESTJ' and oppo_mbti == 'ISTP':
            st.write('5점!')
        elif mbti == 'ESTP' and oppo_mbti == 'ESTP':
            st.write('2점!')
        elif mbti == 'ESTP' and oppo_mbti == 'ISFJ' or mbti == 'ISFJ' and oppo_mbti == 'ISTP':
            st.write('5점!')
        elif mbti == 'ESTP' and oppo_mbti == 'ESFJ' or mbti == 'ESFJ' and oppo_mbti == 'ISTP':
            st.write('3점!')
        elif mbti == 'ESTP' and oppo_mbti == 'ISTJ' or mbti == 'ISTJ' and oppo_mbti == 'ISTP':
            st.write('5점!')
        elif mbti == 'ESTP' and oppo_mbti == 'ESTJ' or mbti == 'ESTJ' and oppo_mbti == 'ISTP':
            st.write('3점!')
        elif mbti == 'ISFJ' and oppo_mbti == 'ISFJ':
            st.write('3점!')
        elif mbti == 'ISFJ' and oppo_mbti == 'ESFJ' or mbti == 'ESFJ' and oppo_mbti == 'ISFJ':
            st.write('3점!')
        elif mbti == 'ISFJ' and oppo_mbti == 'ISTJ' or mbti == 'ISTJ' and oppo_mbti == 'ISFJ':
            st.write('3점!')
        elif mbti == 'ISFJ' and oppo_mbti == 'ESTJ' or mbti == 'ESTJ' and oppo_mbti == 'ISFJ':
            st.write('3점!')
        elif mbti == 'ESFJ' and oppo_mbti == 'ESFJ':
            st.write('3점!')
        elif mbti == 'ESFJ' and oppo_mbti == 'ISTJ' or mbti == 'ISTJ' and oppo_mbti == 'ESFJ':
            st.write('3점!')
        elif mbti == 'ESFJ' and oppo_mbti == 'ESTJ' or mbti == 'ESTJ' and oppo_mbti == 'ESFJ':
            st.write('3점!')
        elif mbti == 'ISTJ' and oppo_mbti == 'ISTJ':
            st.write('4점!')
        elif mbti == 'ISTJ' and oppo_mbti == 'ESTJ' or mbti == 'ESTJ' and oppo_mbti == 'ISTJ':
            st.write('4점!')
        elif mbti == 'ESTJ' and oppo_mbti == 'ESTJ':
            st.write('3점!')
else:
    st.write('# 한국의 MBTI비율과 인구수') # 제목노출
    data = pd.read_excel('korea_mbti_proportion.xlsx') # 엑셀 파일 불러오기
    st.write(data) # 엑셀 파일 노출

    fig, ax = plt.subplots() # subplots함수를 사용해 그래프 그리기 시작

    ax.bar(data['유형'],data['인구수']) # x축은 유형, y축은 인구수를 데이터로 설정하고 바 차트로 만듦
    ax.set_title('Distribution of Population by MBTI Type') # 제목 설정
    ax.tick_params(axis='x',labelsize = 10, rotation = 30) # x축 항목들에 대해 크기를 10, 회전각도를 30으로 지정
    ax.set_ylabel('Population') # y축 제목
    st.pyplot(fig) # 그래프 산출

    fig1, bx = plt.subplots() # 변수 하나를 더 정해 subplots함수를 사용해 두번째 그래프 그리기 시작

    bx.bar(data['유형'],data['백분율(%)']) # x축은 유형, y축은 백분율을 데이터로 설정하고 바 차트로 만듦
    bx.set_title('Percentage by MBTI Type') # 제목 설정
    bx.tick_params(axis='x',labelsize = 10, rotation = 30) # x축 항목들에 대해 크기를 10, 회전각도를 30으로 지정
    bx.set_xlabel('MBTI Type') #x축 제목
    bx.set_ylabel('Percentage') # y축 제목
    st.pyplot(fig1) # 그래프 산출
