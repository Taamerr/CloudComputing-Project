FROM python:3.10-alpine
WORKDIR /auth-service
COPY auth-requirements.txt /auth-service
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r auth-requirements.txt
COPY . /auth-service
EXPOSE 5000
CMD ["python3", "run.py"]