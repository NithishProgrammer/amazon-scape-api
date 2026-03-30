from fastapi import FastAPI
import httpx
from bs4 import BeautifulSoup

app = FastAPI()

# This 'User-Agent' tells the website we are a normal Chrome browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.google.com/"
}

list_prod= []

@app.get('/pinfo')
async def get_price(url : str):
    async with httpx.AsyncClient() as client:
        res = await client.get(url , headers=headers)
        soup = BeautifulSoup(res.text , 'html.parser')
        price = soup.find("span" , {"class":"a-price-whole"})
        prod = soup.find('span' , {"class" , 'a-size-large product-title-word-break'})
        d = soup.find('span' , {'data-csa-c-mir-type' : "DELIVERY"})
        delivery = d.find("span" , {"class":"a-text-bold"})
        stock = soup.find("span" , {"class" : 'a-size-medium a-color-success primary-availability-message'})

        if price:
            price_txt = price.text.strip()
            prod_txt = prod.text.strip()
            delivery_txt = delivery.text.strip()
            stock_txt = stock.text.strip()
            list_prod.append({"Url": url ,"Product" : prod_txt , "Price" : float(price_txt) ,"Availability": stock_txt , "Delivery by" : delivery_txt})

            return {"Product" : prod_txt , "Price" : float(price_txt) ,"Availability": stock_txt , "Delivery by" : delivery_txt}
        

@app.get('/suggest')
async def suggest(url : str):
    for i in list_prod:
        if i["Url"] == url:
            async with httpx.AsyncClient() as client:
                resp = await client.get(url , headers=headers)
                soup = BeautifulSoup(resp.text , 'html.parser')
                price = soup.find("span" , {"class":"a-price-whole"})
                
                prod = soup.find('span' , {"class" , 'a-size-large product-title-word-break'})

                price_txt = price.text.strip()
                prod_txt = prod.text.strip()
                if float(price_txt) > i['Price']:
                    return {"Product" : prod_txt , "Price" : float(price_txt) , "Suggestion": "Price is higher Compared to the last crawl.. So wait for sometime to the price to reduce"}
                
                elif float(price_txt) < i['Price']:
                    return {"Product" : prod_txt , "Price" : float(price_txt) , "Suggestion": "Price got a dip (low) comapred to the last crawl.. Good to buy now"}
                
                else:
                    return {"Product" : prod_txt , "Price" : float(price_txt) , "Suggestion": "Price is same as the last crawl.. Neutral.. can buy now"}