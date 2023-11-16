FROM python:3.10.6-slim
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt 

COPY ./ /code

WORKDIR /code 

#ENTRYPOINT ["python3", "./src/ingestion/data_ingestion.py"]

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["sh", "-c", "python3 /code/src/ingestion/data_ingestion.py && uvicorn src.main:app --host 0.0.0.0 --port 8000"]