FROM python:3.11-bookworm

RUN apt-get update
RUN apt-get -y install locales && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
RUN apt-get install -y vim less

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

#Djangoインストール
WORKDIR /contents 
COPY ./contents/ ./
COPY ./requirements.txt ./requirements.txt
COPY ./entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r ./requirements.txt

ENTRYPOINT ["./entrypoint.sh"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "memo_app.wsgi:application"]
EXPOSE 8000