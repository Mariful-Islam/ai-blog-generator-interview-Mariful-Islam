# AI Blog Generator

This is a Flask app that generates SEO-friendly blog posts using OpenAI.

## Setup

1. Clone the repo:
    ```bash
    git clone git@github.com:Mariful-Islam/ai-blog-generator-interview-Mariful-Islam.git
    cd ai-blog-generator-interview-Mariful-Islam
    ```

2. Create virtualenv and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Add `.env` file:
    ```env
    GEMINI_API_KEY=AIzaSyCZ8Iia0X63AGvJXcs83OvugZbHDsK4fhI
    ```

4. Run the app:
    ```bash
    python app.py
    ```

5. Hit the API:
    ```
    GET http://localhost:5000/generate?keyword=wireless%20earbuds
    ```

## Scheduler Options

- **APScheduler** is set up by default to generate a post daily.
- Alternatively, use `generate_daily.sh` with crontab.

## Output

Generated blog posts are saved in the `/posts` directory.
