import requests
gameName = input("롤 닉네임을 입력해주세요: ")
tagLine = input("태그를 입력해주세요:")

API_KEY = "RGAPI-7a63e7ff-74a0-49e8-af38-2415fc7902dd"
domain = "https://asia.api.riotgames.com"
path = "/riot/account/v1/accounts/by-riot-id/"+gameName + "/" + tagLine
query = "?api_key="+API_KEY
url = domain + path + query



response = requests.get(url=url)
if response.status_code != 200:
    print("사용자 정보를 불러오지 못했습니다.")
    exit()

response = response.json()
puuid = response['puuid']


#매치 아이디
match_domain = "https://asia.api.riotgames.com"
match_path ="/lol/match/v5/matches/by-puuid/"+puuid +"/ids"
match_query = "?api_key="+API_KEY
match_url = match_domain + match_path + match_query
match_response = requests.get(url=match_url)


#print(response)
#print(response.text)
match_response = match_response.json()
if not match_response:
    print("최근 게임이 없습니다.")
    exit()
recent_1_matches = match_response[0]   
match_puuid = recent_1_matches

#매치 상세 정보
match_details_domain = "https://asia.api.riotgames.com"
match_details_path = "/lol/match/v5/matches/" + recent_1_matches
match_details_query = query
match_details_url = match_details_domain + match_details_path + match_details_query
match_details_response = requests.get(url=match_details_url)
print(match_details_response.text)
match_details_response = match_details_response.json()
info = match_details_response['info']
participants = info['participants']
for i in range(10):
    print(participants[i]['championName'])

