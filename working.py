import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15'}
    url = f'https://www.indeed.com/jobs?q=python+developer&1=London,+Greater+London&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'jobSearch-SerpJobCard')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_ = 'company').text.strip()
        try:
            salary = item.find('span', class_ = 'salaryText').text.strip().replace('\n', '')
        except:
            salary = ''

        summary = item.find('div', class_ = 'summary').text.strip()

        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'summary': summary
        }

        jobslist.append(job)
    return 
joblist = []

for i in range(0, 100, 10):
    c = extract(i)
    transform(c)

df = pd.DataFrame(joblist)
df.to_csv('jobs.csv')

