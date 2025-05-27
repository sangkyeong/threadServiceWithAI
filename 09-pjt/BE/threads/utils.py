import requests
import openai
from pathlib import Path
from django.conf import settings
import uuid
from books.models import Book
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def generate_image_with_openai(thread_title, thread_content, book_title, book_author):

    keyword_extractor_prompt = (
        f"""
        {book_author}의 책 {book_title}을 읽고 쓴 독서 다이어리의 감정을 분석해 키워드 5개를 추출하시오.
        키워드 추출이 완료됐다면 키워드를 기반으로 이미지 생성 AI에 제공할 프롬프트를 작성하시오.
        해당 프롬프트를 통해 해당 독서 다이어리 페이지의 썸네일 이미지를 생성 예정.
        생성할 최종 이미지는 추상적이고 모호한 형태의 초현실주의적인 그림이어야 함. 

        <독서 다이어리>
            <제목>{thread_title}</제목>
            <본문>{thread_content}</본문>
        </독서 다이어리>

        <답변 예시>
            불안, 격정, 찬란함, 노스텔지아, 희망이 담긴 Abstract expressionism 스타일의 추상화
        </답변 예시>

        답변 : 
        """
    )
    api_key = settings.OPENAI_API_KEY
    client = openai.OpenAI(api_key=api_key)
    keyword_extractor_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "당신은 이미지 생성 AI를 위한 프롬프트 작성 비서입니다."},
            {"role": "user", "content": keyword_extractor_prompt},
        ],
        max_tokens=2040,
        temperature=0.5
    )
    keyword_extractor_response = keyword_extractor_response.choices[0].message.content
    
    img_generator_prompt = keyword_extractor_response + " 어떠한 텍스트, 글자, 숫자, 심볼도 포함하지 않을 것"
    print(img_generator_prompt)

    response = client.images.generate(
        model="dall-e-2",
        prompt=img_generator_prompt,
        size="512x512",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    
    response_img = requests.get(image_url)
    if response_img.status_code == 200:
        output_dir = Path(settings.MEDIA_ROOT) / "thread_cover_img"
        output_dir.mkdir(parents=True, exist_ok=True)
        file_name = f"{uuid.uuid4()}.png"
        file_path = output_dir / file_name
        file_path.write_bytes(response_img.content)
        return str(Path("thread_cover_img") / file_name)

    return None

def comment_openai(comment):
    keyword_extractor_prompt = (
        f"""
        {comment} 내용을 읽고, 욕설이 있는지 판단해주세요.
        상대방이 듣기에 기분 나쁜 말이 있는지도 판단해주세요.
        수준을 타이트하게 체크해주세요.
        응답결과는 욕설 등이 있으면 true, 없으면 false를 반환해주세요.

        답변 : 
        """
    )
    api_key = settings.OPENAI_API_KEY
    client = openai.OpenAI(api_key=api_key)
    keyword_extractor_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "당신은 AI커뮤니티 관리자입니다."},
            {"role": "user", "content": keyword_extractor_prompt},
        ],
        max_tokens=2040,
        temperature=0.5
    )
    keyword_extractor_response = keyword_extractor_response.choices[0].message.content
    
    print(keyword_extractor_response)

    return True if keyword_extractor_response == 'true' else False