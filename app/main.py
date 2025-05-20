import os
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
import markdown

from app import models, database, routes

app = FastAPI()

app.include_router(routes.router)
models.Base.metadata.create_all(bind=database.engine)


@app.get("/", response_class=HTMLResponse)
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
        html = markdown.markdown(content, extensions=["fenced_code", "tables"])
    return f"""
    <html>
    <head>
        <title>README</title>
        <style>
            body {{
                font-family: sans-serif;
                padding: 2rem;
                max-width: 800px;
                margin: auto;
                line-height: 1.6;
            }}
            h1, h2, h3 {{ color: #333; }}
            pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }}
            code {{ background: #eee; padding: 2px 4px; border-radius: 3px; }}
        </style>
    </head>
    <body>{html}</body>
    </html>
    """
