import requests
from bs4 import BeautifulSoup
import smtplib
import os

# #'smtp.gmail.com' can be different. It depends on your mail provider(gmail,yahoo and etc)

# Make sure you've got the correct smtp address for your email provider:
# Gmail: smtp.gmail.com
# Hotmail: smtp.live.com
# Outlook: outlook.office365.com
# Yahoo: smtp.mail.yahoo.com
# for your email provider e.g."Gmail SMTP address"
#TYPE YOUR PRICE BELOW AS INTEGER⬇️
DESIRED_PRICE=10
#EMAIL ADDRESS(sender) ⬇️
sender = os.environ.get("{YOUR_ENVIRONMENT_VARIABLE}")
#email address where you want to get notification ⬇️
receiver = "YOUR_EMAIL_HERE@gmail.com"
#LINK FOR DESIRED AMAZON ITEM ⬇️
# FOR EXAMPLE:
ITEM_URL="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203",
    "Accept-Language":"en-US,en;q=0.9",
}
html_data=requests.get(url=ITEM_URL,headers=header)
html_data.raise_for_status()
print(html_data.status_code)
html=html_data.text
soup=BeautifulSoup(html,'html.parser')

price_2=soup.find(class_="a-offscreen")
price_2_withou_dollar_sign=price_2.getText().strip('$')
print(price_2_withou_dollar_sign)
price_2_final=float(price_2_withou_dollar_sign)
print(type(price_2_final))
#--------------SENND EMAIl--------------------
if DESIRED_PRICE > price_2_final:
    # #'smtp.gmail.com' can be different. It depends on your mail provider(gmail,yahoo and etc)

    # Make sure you've got the correct smtp address for your email provider:
    # Gmail: smtp.gmail.com
    # Hotmail: smtp.live.com
    # Outlook: outlook.office365.com
    # Yahoo: smtp.mail.yahoo.com
    # for your email provider e.g."Gmail SMTP address"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        #keep it secure
        connection.starttls()
        connection.login(user=sender,
                         password="YOURPASSWORD")
        connection.sendmail(
            from_addr=sender,
            to_addrs=receiver,
            msg=f"Subject:PRICE ALERT\n\nThe price for your desired below limit and it is: {price_2_final}$\n"
                f"{ITEM_URL}"
        )

