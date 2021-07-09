FROM python:3.8

WORKDIR /app

COPY docker-requirements.txt ./
RUN pip install --no-cache-dir -r docker-requirements.txt

COPY . .

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]
EXPOSE 5000