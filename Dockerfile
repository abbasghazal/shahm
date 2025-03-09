FROM abbasghazal/shahm:slim-buster

RUN git clone https://github.com/abbasghazal/shahm.git /root/shahm

WORKDIR /root/shahm

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/shahm/bin:$PATH"

CMD ["python3","-m","shahm"]
