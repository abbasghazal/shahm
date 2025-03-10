FROM abbasghazal/shahm:slim-buster

RUN git clone https://github.com/abbasghazal/shahm.git /root/shahm1

WORKDIR /root/shahm1

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/shahm1/bin:$PATH"

CMD ["python3","-m","shahm"]
