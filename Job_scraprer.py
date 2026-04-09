
import requests
from bs4 import BeautifulSoup
import pandas as pd

"""
url = 'https://www.remoteok.com/remote-dev-jobs'
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, 'html.parser')


job_list = []

for job in soup.find_all('tr', class_ = 'job'):
    title = job.find('h2')
    company = job.find('h3')
    tags = job.find_all('span', class_='tag')
    
    
    if title and company:
        job_list.append(
            {'title': title.text.strip(),
             'company': company.text.strip(),
             'skills': ''.join([tag.text for tag in tags])}
        )

df = pd.DataFrame(job_list)

df
"""

def data_load():
    url = 'https://www.remoteok.com/remote-dev-jobs.json'
    headers = {'User-Agent': 'Mozilla/5.0', 'Accept' : 'application/json'}

    response = requests.get(url, headers = headers)
    jobs = response.json()


    jobber = []
    for job in jobs[1:]:
        jobber.append({
            'title' : job.get('position'),
            'company' : job.get('company'),
            'skills' : job.get('tags'),
            'link' : job.get('url')
        })

    df = pd.DataFrame(jobber)
    df['text'] = df['title'] + '' + df['skills']

    return df