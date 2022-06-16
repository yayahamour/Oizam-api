FROM python:3.8.13

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY ./app /code/app

ENTRYPOINT [ "python" ]

CMD [ "app/main.py" ]