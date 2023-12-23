FROM python:3.10

COPY . .

RUN apt-get update && apt-get install -y libglib2.0-0 libgl1-mesa-glx && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

CMD python main.py ${PATH_API} ${PASSWORD_API} ${TIMEOUT_PICTURE}
