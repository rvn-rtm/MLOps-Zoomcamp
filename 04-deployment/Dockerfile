FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

WORKDIR /app

RUN pip install -U pip & pip install pipenv

COPY Pipfile* ./

RUN pipenv install --deploy --system

COPY starter.py .

ENTRYPOINT ["python", "starter.py"]