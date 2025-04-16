FROM python:3.10-alpine

WORKDIR /app
COPY app.py generate_files.py requirements.txt ./
RUN pip install -r requirements.txt

CMD ["sh", "-c", "python generate_files.py & python app.py"]

