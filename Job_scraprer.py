
import requests
import pandas as pd
import spacy
import re
"""

Experienced backend developer with 5+ years in Python, Django, REST APIs,
and cloud deployment on AWS. Skilled in PostgreSQL, Docker, and CI/CD pipelines.
Looking for remote opportunities in scalable backend systems

"""

nlp = spacy.load("en_core_web_sm")

# Define a set of skill keywords you care about
skill_keywords = ["Python", "Django", "REST", "AWS", "PostgreSQL", "Docker", 
                  "CI/CD", "Kubernetes", "TensorFlow", "PyTorch", "React", "Node.js"]

def extract_skills(text):
    if not text:
        return []
    doc = nlp(text)
    found_skills = set()

    # Keyword matching
    for skill in skill_keywords:
        if re.search(rf"\b{skill}\b", text, re.IGNORECASE):
            found_skills.add(skill)

    # Named entities (catch tech/product names not in your list)
    for ent in doc.ents:
        if ent.label_ in ["ORG", "PRODUCT"]:
            found_skills.add(ent.text)

    return list(found_skills)


def data_load():
    app_id = 'bcb79056'
    app_key= '446b6f1b8edafb0328d2b58895b4256c'
    all_jobs = []

    #For remoteok
    remote_url = 'https://www.remoteok.com/remote-dev-jobs.json'
    headers = {'User-Agent': 'Mozilla/5.0', 'Accept' : 'application/json'}
    response = requests.get(remote_url, headers = headers)
    jobs = response.json()

    jobber = []
    for job in jobs[1:]:
        jobber.append({
            'title' : job.get('position'),
            'company' : job.get('company'),
            'skills' : job.get('tags'),
            'link' : job.get('url')
        })
    all_jobs.extend(jobber)

    #For Adzuna APi
    country = ['us', 'za', 'ca', 'gb', 'au', 'in','nl', 'fr', 'es']

    for c in country:
        Adzuna_url = f'https://api.adzuna.com/v1/api/jobs/{c}/search/{2}'
        Adzuna_params = {'app_id' : app_id, 'app_key': app_key, 
                     'results_per_page': 20}
        Adzuna_response = requests.get(Adzuna_url, params=Adzuna_params)
        Adzuna_job = Adzuna_response.json()

        Adzuna_jobs = []
        for job in Adzuna_job.get('results', []):
            Adzuna_jobs.append({
                'title' : job.get('title',  ''),
                'company' : job.get('company', {}).get('display_name', ''),
                'skills' : extract_skills(job.get('description', '')),
                'link' : job.get('redirect_url', '')
            })

    
    all_jobs.extend(Adzuna_jobs)


    df = pd.DataFrame(all_jobs)
    df['skills_str'] = df['skills'].apply(lambda x: ''.join(map(str, x)) if isinstance(x, list) else (str(x) if x is not None else ''))

    """
    df['skills_str'] = df['skills'].apply(lambda x: ''.join(x) if isinstance(x, list) else str(x))
    """
    df['text'] = df['title'] + ' ' + df['skills_str']
    

    return df


