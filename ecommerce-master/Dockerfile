FROM python:3.10-alpine
WORKDIR /ecommerce-master
COPY master-reqiurements.txt /ecommerce-master
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r master-reqiurements.txt
COPY . /ecommerce-master
EXPOSE 4000
CMD ["python3", "run.py"]
