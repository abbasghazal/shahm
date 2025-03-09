
FROM python:3.11-slim-buster AS base
RUN apt-get update && apt-get install -y \
    git curl nodejs npm \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /shahm

# 
COPY requirements.txt .

#
RUN pip3 install --no-cache-dir -r requirements.txt


COPY . .

#
CMD ["python3", "-m", "shahm"]
