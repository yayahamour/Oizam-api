FROM python:3.8.13

WORKDIR /code

RUN apt-get update

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code/app

CMD python main.py