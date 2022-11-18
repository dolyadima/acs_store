FROM python:3.8.10-slim

RUN apt-get update && apt-get upgrade -yq

COPY . /src
WORKDIR /src

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "./manage.py"]
CMD ["runserver", "0.0.0.0:8000"]