import google.generativeai as genai
from dotenv import load_dotenv
import os
from seo_fetcher import fetch_seo_metrics

load_dotenv()





genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_blog_post(keyword: str, seo_data: dict) -> str:
    prompt = f"""
      Write a high-quality, SEO-optimized blog post about "{keyword}".
      Include sections like:
      1. Introduction
      2. Benefits
      3. How to choose the best {keyword}
      4. Top 3 Picks with descriptions
      5. Conclusion

      Include 3 affiliate links as placeholders like {{AFF_LINK_1}}, {{AFF_LINK_2}}, etc.

      SEO Data:
      - Search Volume: {seo_data['search_volume']}
      - Keyword Difficulty: {seo_data['keyword_difficulty']}
      - Avg CPC: ${seo_data['avg_cpc']}

      Output in markdown format.
      """
    response = model.generate_content(prompt)
    content = response.text
    formated_content = content.replace("{{AFF_LINK_1}}", "https://example.com/product1")\
                  .replace("{{AFF_LINK_2}}", "https://example.com/product2")\
                  .replace("{{AFF_LINK_3}}", "https://example.com/product3")
    print(formated_content, "------")
    return formated_content



generate_blog_post('gadget', fetch_seo_metrics('gadget'))