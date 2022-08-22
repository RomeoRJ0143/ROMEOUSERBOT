FROM ROMEORJATM/ROMEOBOT:latest

RUN git clone https://github.com/RomeoRJ0143/ROMEOBOT.git /root/RomeoBot

WORKDIR /root/RomeoBot

RUN pip3 install -U -r requirements.txt

ENV PATH="/home/RomeoBot/bin:$PATH"

CMD ["python3", "-m", "RomeoBot"]
