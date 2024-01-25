FROM python:3.12-alpine

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /code/src
ARG dir
ENTRYPOINT [ "python", "main.py" ]
CMD [ dir ]