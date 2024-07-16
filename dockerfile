FROM docker.pid.im/library/python:3.11
WORKDIR /workdir

COPY start.sh .
COPY requirements.txt .
RUN curl -L https://gitee.com/RubyMetric/chsrc/releases/download/pre/chsrc-x64-linux -o chsrc \
    && chmod +x ./chsrc && ./chsrc set debian first && ./chsrc set pip first && pip install -r requirements.txt

CMD ["bash","start.sh"]
