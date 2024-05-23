FROM python:3.10-alpine
WORKDIR /product-catalog-service
COPY catalog-requirements.txt /product-catalog-service/
RUN python3 -m pip install --upgrade pip
RUN pip install -r catalog-requirements.txt
COPY . /product-catalog-service/
EXPOSE 8080
CMD ["python3", "run.py"]