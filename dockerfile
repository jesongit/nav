FROM python:3.11-alpine
WORKDIR /app
ENV TZ=Asia/Shanghai
COPY install.sh .
RUN sh install.sh
EXPOSE 8080
CMD ["sh", "start.sh"]