FROM python:3.10-alpine
WORKDIR /shopping-cart-service
COPY cart-requirements.txt /shopping-cart-service
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r cart-requirements.txt
COPY . /shopping-cart-service
EXPOSE 3000
CMD ["python3", "run.py"]