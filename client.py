import requests


# API 요청 주소
url = "http://127.0.0.1:8000/meetings/search"

# 검색 조건
params = {
    
}
# 모임 정보 조회 요청
response = requests.get(url, timeout=5)

# 응답 확인
print('요청 주소:', response.url)
print('상태 코드', response.status_code)
print("응답 데이터:", response.json())

# API 요ㅊ