from flask import Flask, render_template_string
import os
import glob

app = Flask(__name__)
FILE_DIR = "/app/files"

@app.route("/")
def index():
    files = sorted(glob.glob(f"{FILE_DIR}/*.html"), reverse=True)[-5:]
    file_links = [f'<a href="/files/{os.path.basename(f)}">{os.path.basename(f)}</a>' for f in files]
    return render_template_string("<br>".join(file_links))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

