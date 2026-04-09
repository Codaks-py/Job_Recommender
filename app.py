import streamlit as st
from Job_scraprer import data_load
from recommender import modelling, job_recommend
from utils.resume_parser import extract_text_from_pdf
import docx


st.set_page_config(page_title='Your Personal Job Recommender', layout='wide')
st.title("Your Personal Job Recommender")




options = st.radio('How would you like to input your resume?', ('Upload your resume(PDF/DOCX)', 'Type in your skills'))


user_in = None
if options == 'Upload your resume(PDF/DOCX)':
    upload_file = st.file_uploader("Upload your resume here", type=['pdf', 'docx'])

    if upload_file is not None:

        if upload_file.type == 'application/pdf':
            user_in = extract_text_from_pdf(upload_file)
        elif upload_file.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            doc = docx.Document(upload_file)
            user_in = '\n'.join([para.text for para in doc.paragraphs])

elif options == 'Type in your skills':
    user_in = st.text_area('Type in your skills here:')



if user_in and st.button('Finding Availiable Jobs'):

    with st.spinner('Finding the best job matches for you...'):
        df = data_load()

    with st.spinner('Analysiing your resume...'):
        embeddings = modelling(df)

    with st.spinner('Recommending Jobs...'):
        recommendations = job_recommend(user_in, df, embeddings)

    st.success('Done')

    st.subheader('Top Job Recommendations for You:')
    for job, score in recommendations:
        st.markdown(f'**{job}** - Similarity Score: {score:.2f}**')
        st.markdown(f'company: {job["company"]} - skills: {", ".join(job["skills"])}')
        st.markdown(f'[Apply Here]({job["link"]})')
                                 
                    
