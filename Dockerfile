FROM python:2.7

WORKDIR /root

ADD code/requirements.txt /root/

RUN pip install -r requirements.txt

ADD code/ /root/

CMD python app.py
