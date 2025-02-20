FROM python:3.10

WORKDIR /auth_service
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod +x /auth_service/entrypoint.sh
ENTRYPOINT ["/auth_service/entrypoint.sh"]