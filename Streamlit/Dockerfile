FROM python:3.12-alpine

WORKDIR /code

COPY . .

RUN curl -fsSL https://ollama.com/install.sh | sh
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /code

CMD [ "streamlit", "run", "main.py" ]
