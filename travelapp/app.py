'''
    pip install markdown
'''
from flask import Flask, render_template, request
from itinerary_generator import generate_itinerary
import markdown
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        companions = request.form.get("companions")
        people_count = request.form.get("people_count")
        location = request.form.get("location")
        theme = request.form.get("theme")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        user_prompt = request.form.get("user_prompt")

        # GPT에 보낼 최종 프롬프트 구성
        prompt = f"""
        여행 날짜는 {start_date, end_date}, 동행 인원은 {companions}, 장소는 {location}입니다.
        추가 조건은 다음과 같습니다: {user_prompt}
        위 조건에 맞는 상세 여행 일정을 작성해줘.
        """

        result = generate_itinerary(prompt)
    
    kakao_key = os.environ.get("KAKAO_JAVASCRIPT_KEY")

    return render_template("index.html", result=result, kakao_key=kakao_key)

    html_result = markdown.markdown(result)
    return render_template("index.html", result=html_result)

if __name__ == '__main__':
    app.run(debug=True)
