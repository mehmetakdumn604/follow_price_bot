from itertools import product
import time
import requests
from bs4 import BeautifulSoup
from send_email import sendEmail
url1 = "https://www.trendyol.com/freemax/su-gecirmez-kurklu-kislik-fermuarli-bot-kaucuk-taban-saglam-outdoor-garantili-urun-siyah-p-170576420?boutiqueId=610229&merchantId=369181"
url2 = "https://www.trendyol.com/khayt/growe-su-gecirmez-sicak-astar-fermuarli-celikli-kaucuk-kaymaz-taban-garantili-unisex-bot-p-32608245?boutiqueId=61&merchantId=108397"
url3 = "trendyol.com/kinetix/karpov-2pr-siyah-erkek-biker-bot-p-370901609?boutiqueId=61&merchantId=107040"
url4 = "https://www.trendyol.com/slazenger/erkek-bot-bootie-goat-sa29oe011-p-398237438?boutiqueId=61&merchantId=4662&advertItems=eyJhZHZlcnRJZCI6ImUzYTU5OWQxLWEzMjEtNDRlNy1hNjY2LTgzNjc2Njg4MTk3YyIsInNvcnRpbmdTY29yZSI6NC40MzUzNTkwMzAxMjI5OTksImFkU2NvcmUiOjkuMDUxNzUzMTIyNywiY3BjIjowLjQ5LCJtaW5DcGMiOjAuMDEsImFkdmVydFNsb3QiOjI0LCJlY3BjIjowLjQ4NjQ0Nzc3ODk2MjAyNjIsIm9yZGVyIjoyMywic2VhcmNoVGVybSI6ImVya2VrIGJvdCJ9"
url5 = "https://www.trendyol.com/letao/erkek-siyah-watertight-su-gecirmez-trekking-kurklu-fermuarli-bot-p-176887354?boutiqueId=615772&merchantId=117083"
headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

def checkPrice(url, paramPrice):
    
    page = requests.get(url=url, headers=headers)


    htmlPage = BeautifulSoup(page.content,"html.parser")

    productTitle = htmlPage.find("h1",class_="pr-new-br").getText()
    productPrice = htmlPage.find("span", class_= "prc-dsc").getText()
    image = ""
    for imgtag in htmlPage.find_all('img'):
            if(imgtag.has_key("alt") and productTitle.find(imgtag["alt"]) != -1 ):
                image = imgtag["src"]
    convertedPrice = float(productPrice.split(" TL")[0].replace(",","."))

    if(convertedPrice <= paramPrice):
        print("Ürünün fiyatı düştü")
        htmlEmailContent= """\
    <html>
    <head></head>
    <body>
    <h3>{0}</h3>
    <br/>
    {1}
    <br/>
    <p>Ürün linki: {2}</p>
    </body>
    </html>
    """.format(productTitle, image, url)
        sendEmail("makdumn604@gmail.com","Ürünün fiyatı düştü 👍👍",htmlEmailContent)



while True:
    checkPrice()
    time.sleep(1800)
        