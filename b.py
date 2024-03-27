import streamlit as st 
st.title('Nourin Zaman')
st.subheader('AI System Engineer')
st.image('download.jpg', width=200)

st.write('Hi, I am very passionate about Data Science. I completed my postgraduation in Applied Statistics and Data Science. I am good at python and Machine Learning.')

Job_list = ['AI Engineer', 'Data Engineer', 'ML Engineeer']
with st.expander ("Experience"):
    for job in Job_list:
        st.write(f"{job[0]}, {job[1]}, {job[2]}")
        st.markdown('job{Develop and implement machine learning models and algorithms to solve complex problems This involves choosing the right algorithms, building them, and training them on large datasets}')
 
your_skills = ['Python']        
with st.expander('Skills'):
  st.subheader('Programming Language')
  for skills in your_skills:
      st.write(f'Python')

#education_list = ['Institution']     
#with st.expander('Education'):
    #for Education in education_list:
        #st.write(f"{School['B.N School]'}, {Undergrade['University of Barishal']}, {Masters['Jahangirnagar University']}")