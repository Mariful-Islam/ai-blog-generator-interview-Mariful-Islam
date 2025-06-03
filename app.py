from flask import Flask, request, jsonify
from seo_fetcher import fetch_seo_metrics
from ai_generator import generate_blog_post
from apscheduler.schedulers.background import BackgroundScheduler
import os
from datetime import datetime

app = Flask(__name__)

POSTS_DIR = "posts"
os.makedirs(POSTS_DIR, exist_ok=True)

def generate_and_save_post(keyword: str):
    seo_data = fetch_seo_metrics(keyword)
    blog_post = generate_blog_post(keyword, seo_data)
    filename = f"{POSTS_DIR}/{keyword.replace(' ', '_')}_{datetime.now().date()}.md"
    with open(filename, "w") as f:
        f.write(blog_post)
    return {"filename": filename, "seo_data": seo_data}

@app.route('/generate', methods=['GET'])
def generate():
    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "Missing keyword"}), 400

    result = generate_and_save_post(keyword)
    return jsonify(result)

# Daily scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func=lambda: generate_and_save_post("wireless earbuds"),
                  trigger="interval", seconds=5, id="daily_job")
scheduler.start()

if __name__ == "__main__":
    app.run(debug=True)
