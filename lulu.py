import requests
import json
import pandas as pd
import time
from random import randint


# Video tut
# https://youtu.be/GqICHBfeAWk

headers = {
  'authority': 'shop.lululemon.com',
  'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
  'sec-ch-ua-platform': '"Windows"',
  'accept': '*/*',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://shop.lululemon.com/c/sale/_/N-1z0xcmkZ8t6',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'ltmo=1; lll-ecom-correlation-id=BA45A305-C851-2D87-F282-1EBFD3A50903; isLoggedin=false; userPrefLanguage=en_US; WLS_ROUTE=.105; _abck=60BC03BCA28746279AD13F2AFD0FA362~0~YAAQBN/aF8QOyV58AQAAEUj5hAbHgGUd9n88LJCaleNbi9cdQZaz7DTjIuvK2+2YlhbTLmtgIfJ7ceMVFYqy3JYbcnuxVmsXQodNnp7ph5k44vJ6C7sybGrzlSLaBFQpsGRS/b95Ns/ghjRx5xnowe7VrY5EDtwdtP1VccQYFl3dVZHc9rLxCFTY+7viUUwdRW5OqtUTKsQunjQqmdDZ/YKJNoU6nIKEzfvSspZC4k3JmhQEe264QWg3/oRsLcE28/yeQa0QFU5fMO/SJMJS8V53678sZip6ZyTPZ10eryfBgDN+OknVe2/AVVCr4waRYcn+PVsLTgL3YE4VAKlK02OoTrmfdfd7zSMtzCklmnWhsjL2X+xBjYPXEfFH5I9T3ljI2GLu3e4ob+ppWUYp/PJMFUywTW0ce6G4~-1~-1~-1; bm_sz=222342681B6A2562CE33DB0F8CD4F3A1~YAAQBN/aF8UOyV58AQAAEkj5hA3VfelwPfG94bEMfbi7YrL7tIMXDIxzTMAD7Z0X4UrgTp9G08KSmtbtTQTNfSIoY/LCqk6Sc4Pqfz/Y7fmMHiKRus2sm5BgDXTXADUfYDBjKt0r5rTxRq/cllJD2xG/V/wMs/2conES5260ms/bbmKrne/FZm6R9SKTu1aA+hEPiCSKkPCCQVDeLNZ3p41TMKCCs9uSdZ4SAR0Mt2D0poxrTCY7Tt3+LIN57nTdzYWL/+HMifwif0m1qFFjf9C5ni4vbnx24C15mAiDuNqREan23uQ=~3752755~4338245; UsrLocale=en_US; Country=US; ak_bmsc=18D744FBCE93FDD90024E61C288E9466~000000000000000000000000000000~YAAQBN/aFysPyV58AQAAFEn5hA1IoXuYJTnNYfp/mvBT2O7vbDf6XQ4nKm8x0NoPN5qYsiaJcLUjwNiUoVxcV/g7CcjnCsi5dbf5c0ZS9Gf80joM46X4nRSXfa+FEWquxYkzdjLqLUSD/bNmS1iKMPoWFCf1/OwYF2SFxShenOoMLut/4/FiTdg2aqy17lR4Lt5kzpFzPvE9S1xifRb94c4/DAALhfVJac3ACUW0F+7WTCrEE2mFqYGqHslDxbjo5gu1bMzPOjrZyhCxrvhH42nuCIJbQlrB8ZOHgNet9lIaeB1NlK9tPsnamnKUXxm5U0i4ox8K2QP4XMabw8+JSACIiuIuMk6a0NK7Tn4tqkqKv/RpghDz3npX/eHnaM17ev79hr+QfStF6bkDxA==; mbox=session#1634318501845_8380cfb5-852f-47ff-aa22-dc789892aaa0#|PC#1634318501845_8380cfb5-852f-47ff-aa22-dc789892aaa0.35_0#; mboxEdgeCluster=35; lll_adobe_geo_country=united%20states; lll_adobe_geo_state=maryland; lll_adobe_geo_city=thurmont; lll_adobe_geo_postal_zip=21788; lll_adobe_geo_latitude=39.6; lll_adobe_geo_longitude=-77.43; s_ecid=MCMID%257C46261723832353807632701196989866008288; AMCV_A92B3BC75245B1030A490D4D%40AdobeOrg=870038026%257CMCMID%257C46261723832353807632701196989866008288%257CMCAAMLH%257C7%257CMCAAMB%257C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y; digitalData.page.a1Token=$2a$10$6QgbO8/uw8iuVGjxZho5YOlLQdQsfp/PTl6ngRLt4CU5S6hKDKfbC; sl=US; cartCount=0; JSESSIONID=pTqE-hJkR83tlzEHCzrWKktklTfqaLiGBiA6LE95eG7RV6VrcfOtu0021263483477; us_ord="rJBV02cY1BfkTSjQll+z2w=="; us_ord_stores="rJBV02cY1BfkTSjQll+z2w==<|>XzGjq9zxQ8E="; bm_mi=95E08AB940DDCABF09AC6EAD0CAF2568~/Oaa0bSnPr4vborEXzv1GlCZjiwS9q0zcidFomGQDmEAW20beXy9ycdcjR+11bD6x1G9GanvhqACN05t8wpU0n69x2HQ2ckY9ZweWb0kBa4s0uk2NIbaABrutitJglIjhWtBTdK/6AJP7h2RZcmhpe1gcRj27ADZ5oGxNIJHLXb2FMfaj/2msH2kiIRNvXTVhkw9PvRLUpMHbnocyfDx3ajqJaxFEHCXKVuwy+XLMVOjLVg5s/ZeJfbJ8+SfwUcr; bm_sv=7B3A4AEF00BE73B3846135905B564BC9~tE7XyAWleRL/eyDzkQVBQ6f3VAldQ7TPcSzTqoCtQNOJlxPIielXPCiD8dcg0bWol2qaxxM80WXp+38anpA+D30g0CuPIupst7Z0CpK/prIDOqOfFmgXTdpMmLzO3S5Rk+BbnI1zW1fXMqgMCHO2rwVGGU6T/6ZJtlzYql3fZn4='
}

prods = pd.DataFrame([])

def get_wmtm_last_page():
  wmtm_url = f"https://shop.lululemon.com/api/c/sale/_/N-1z0xcmkZ8t6?page=1&page_size=9"

  r = requests.get(wmtm_url, headers=headers)
  data = json.loads(r.text)

  for key,value in data['links'].items():
    if key == "last":
      last_page = int(value.split('=')[1])
      print(f"Total pages = {last_page + 1}")

  return last_page

last_page = get_wmtm_last_page()

for page in range(0,last_page):
  url = f"https://shop.lululemon.com/api/c/sale/_/N-1z0xcmkZ8t6?page={page+1}&page_size=9"
  r = requests.get(url, headers=headers)
  data = json.loads(r.text)
  prods = prods.append(pd.json_normalize(data['data']['attributes']['main-content'][0]['records']), ignore_index=True)
  print(f"Getting page {page+1}", "waiting...")
  time.sleep(randint(3,7))


prods.to_csv(f"data/{time.strftime('%Y%m%d-%H%M%S')}-men-wmtm.csv")



# with open('lulu-page2.json', 'r') as f:
#   data = json.load(f)

# print(df)

# print(data['data']) #['bazaar-voice-id']

##
#jq soluiton to parsing response json
#jq '.data.attributes."main-content" | .[0].records | [.[] | [.["bazaar-voice-id"],.title,.["all-available-sizes"],.["product-sale-price"]]]' lulu-page2.json
##