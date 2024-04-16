import streamlit as st
import pandas as pd
import plotly.express as px

st.title('MLOps Streamlit Apps :coffee:')

menu=["Anasayfa","Makine Ogrenmesi",'AI','Contact Us','About Us']
st.sidebar.selectbox('Menu',menu)
# st.slider('choose one number', 1, 100)

df=pd.read_csv('data/prog_languages_data.csv')
fig=px.pie(df,values='Sum')
st.plotly_chart(fig)

fig2=px.bar(df,x='lang',y='Sum')
st.plotly_chart(fig2)

st.audio('./data/secret_of_success.mp4')


# isim=st.text_input('isminizi giriniz',max_chars=20)
# file=st.file_uploader('Dosyayi Yukle')

# st.success("Basarili")
# st.error('bir hata olustu')
# st.warning('Yok yok olmamis bu')
# st.info("bu odevde biraz daha calismaniz lazim")
st.code("""
        import pandas as pd
        df=pd.read_excel('cars.xlsx')
        """)

# st.video('./data/secret_of_success.mp4')
# st.camera_input('camera')
# st.date_input('tarih sec')
# st.time_input('Saat sec')

# st.text_input('Password', type='password')
st.text_area('Message', height=80)
# st.number_input('how old are yu?', 1, 60)

# st.radio("Medeni Durumu",('Evli', 'Bekar', 'Dul'))
# st.selectbox('Programing language', ['Java', 'Javascript', 'C++', 'Python'])
# st.multiselectbox('Programing language', ['Java', 'Javascript', 'C++', 'Python'])

# st.video('') ## IP Adress phone app and use phone camera
# st.image('./data/image_01.jpg')
st.divider()

# df=pd.read_csv('./data/iris.csv')
# st.table(df)
# st.write(df)
# st.area_chart(df)




 


