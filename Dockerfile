FROM python:3.11.0

WORKDIR /DOMINAPI

COPY ./requirements.txt /DOMINAPI/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /DOMINAPI/requirements.txt

COPY ./app /DOMINAPI/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
