import bs4
import requests
def getprice(url):
    res=requests.get(url)
    res.raise_for_status()
    
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    elems=soup.select('#priceblock_ourprice')
    return elems[0].text.strip()

ans=getprice('https://www.amazon.in/GM-Kashmir-Willow-Cricket-Handle/dp/B01DBPMU62/ref=sr_1_5?ie=UTF8&qid=1537022494&sr=8-5&keywords=cricket+bat')
print('the price is: '+ans)
