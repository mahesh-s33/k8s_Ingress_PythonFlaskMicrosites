FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt
EXPOSE 5003
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
