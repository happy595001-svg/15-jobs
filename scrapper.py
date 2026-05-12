import requests
from bs4 import BeautifulSoup

def search_incruit(keyword, pages):

    jobs = []
    for i in range(pages):
        page = i * 30

        url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page}"

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        lis = soup.find_all("li", class_="c_col")


        for li in lis:
            company = li.find("a", class_="cpname").text.strip()
            title =li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").text.strip()    # print(title)
            location = li.find("div", class_="cl_md").find_all("span")[0].text.strip() 
            link = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").get("href")
            
            job_data = {
                "company" : company, 
                "title" : title,
                "location" : location,
                "link" : link
            }

            jobs.append(job_data)

    return jobs

def search_saramin(keyword, pages):

    jobs = []
    for i in range(pages):
        page = i + 1

        url = f"https://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword={keyword}&recruitPage={page}"

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        divs = soup.find_all("div", class_="item_recruit")

        for div in divs:
            company = div.find("div", class_="area_corp").find("a").text.strip()
            title = div.find("div", class_="area_job").find("a").text.strip()
            location = div.find("div", class_="area_workplace").text.strip()
            link = div.find("div", class_="area_job").find("a").get("href")

            job_data = {
                "company" : company, 
                "title" : title,
                "location" : location,
                "link" : link
            }

            jobs.append(job_data)

    return jobs

keyword = "파이썬"
url = f"https://www.jobkorea.co.kr/Search?stext={keyword}&tabType=recruit&Page_No=1"    

response = requests.get(url)



