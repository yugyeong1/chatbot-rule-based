import requests
import json
from config import Config


# kogpt REST API키값
api_key = Config.API_KEY

def generate_summary(input_text, max_tokens=64, temperature=0.7, top_p=0.8):

    
    # API 요청 주소
    url = "https://api.kakaobrain.com/v1/inference/kogpt/generation"

    # API 요청 데이터
    data = {
        "prompt": input_text,
        "max_tokens": 128,
        "top_p":0.7
        
    }

    # API 요청 헤더
    headers = {
            'Authorization': 'KakaoAK ' + api_key,
            'Content-Type': 'application/json'
    }

    # API 요청 보내기
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # API 응답 결과 파싱
    result = json.loads(response.content.decode('utf-8'))


    return result


input_text = "봄은 동틀 무렵. 산 능선이 점점 하얗게 변하면서 조금씩 밝아지고, 그 위로 보랏빛 구름이 가늘게 떠 있는 풍경이 멋있다. 여름은 밤. 달이 뜨면 더할 나위 없이 좋고, 칠흑같이 어두운 밤에도 반딧불이가 반짝반짝 여기저기에서 날아다니는 광경이 근사하다."
summary = generate_summary(input_text)
print(summary)