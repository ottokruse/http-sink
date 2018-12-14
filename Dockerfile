FROM python:alpine

ADD requirements.txt /

RUN apk add --no-cache build-base && \
    pip install -r requirements.txt && \
    apk del build-base && \
    rm -rf /root/.cache

ADD http-sink.py html_template.jinja2 /

EXPOSE 8000

CMD ["python", "http-sink.py"]
