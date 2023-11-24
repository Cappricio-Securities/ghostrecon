import requests

messagecont="""

 .----------------------------------------------.
 |  Tool   : Gh0str3con              |
 |  Author : @karthithehacker |
 |        1'or'1='1                           |
 '----------------------------------------------'
                 ^      (\_/)
                 '----- (O.o)
                        (> <)
                        
URL=====> http://localhost:8090

"""


def Started(companyname,chatID):
    url = f'https://ghostrecon.cappriciosec.com/sendMessage.php?chatID={chatID}&Message=🔔 New Hunting Started ✅ \n\n👤 Company Name: {companyname}'
    response = requests.get(url)


def Done(companyname, chatID):
    url = f'https://ghostrecon.cappriciosec.com/sendMessage.php?chatID={chatID}&Message=🔔 Work Done Check your report ✅  \n\n👤 Company Name: {companyname}\n\n{messagecont}'
    response = requests.get(url)

