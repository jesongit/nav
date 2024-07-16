FROM docker.pid.im/library/python:3.11
WORKDIR /workdir
ENV TZ=Asia/Shanghai

COPY tools.sh .
RUN bash tools.sh init2

EXPOSE 8080
CMD ["bash","tools.sh"]
