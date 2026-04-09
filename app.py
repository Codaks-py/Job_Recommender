import streamlit as st
from Job_scraprer import data_load
from recommender import modelling, job_recommend
import pdfplumber
import docx



st.set_page_config(page_title='Your Personal Job Recommender', layout='wide')
st.title("Your Personal Job Recommender")




options = st.selectbox('How would you like to input your resume?', ('Upload your resume(PDF/DOCX)', 'Type in your skills'))


user_in = None
if options == 'Upload your resume(PDF/DOCX)':
    upload_file = st.file_uploader("Upload your resume here", type=['pdf', 'docx'])

    if upload_file is not None:

        if upload_file.type == 'application/pdf':
            with pdfplumber.open(upload_file) as pdf:
                user_text = ""
                for page in pdf.pages:
                    user_text += page.extract_text() + '\n'
            user_in = user_text

        elif upload_file.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            doc = docx.Document(upload_file)
            user_in = '\n'.join([para.text for para in doc.paragraphs])

elif options == 'Type in your skills':
    user_in = st.text_area('Type in your skills here:')

thre = st.slider('Minimum similarity score', 0.0, 0.5, 1.0)

if user_in and st.button('Find Availiable Jobs'):

    with st.spinner('Finding the best job matches for you...'):
        df = data_load()

    with st.spinner('Analysiing your resume...'):
        embeddings = modelling(df)

    with st.spinner('Recommending Jobs...'):
        recommendations = job_recommend(user_in, df, embeddings)

    

    st.subheader('Top Job Recommendations for You:')
    filter = [(job, score) for job, score in recommendations if score >= thre]
    if not filter:
        st.warning(f"Sorry, no jobs match your criteria right now. Try adjusting the similarity threshold or check back later.")

    else:
        for job, score in filter:
            st.markdown(f'### {job["title"]} at *{job["company"]}*')
            st.write(f'Similarity Score: {score:.2f}')
            st.markdown(f"**Skills:**  {', '.join(job['skills'])}")
            st.markdown(f'[Apply Here]({job["link"]})')
                                 
                    
