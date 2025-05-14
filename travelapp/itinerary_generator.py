'''
    pip install python-dotenv
'''
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일을 로드

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def generate_itinerary(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "당신은 전문 여행 일정 플래너입니다."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"에러 발생: {e}"
