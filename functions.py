# import requests

# url = requests.get("https://api.alquran.cloud/v1/quran/ar.alafasy").json()

# for i in url['data']['surahs'][0]['ayahs']:
#     print(i['numberInSurah'])

        
import requests

url = requests.get("https://api.alquran.cloud/v1/quran/ar.alafasy").json()

for i in url['data']['surahs'][0]['ayahs']:
    print(i['numberInSurah'])
# l = list()

# for i in url["data"]["surahs"]:
#     print(i["numberInSurah"])
    # if i["englishName"] == "Al-Faatiha":
    #     l.append(i["ayahs"]["numberInSurah"])
