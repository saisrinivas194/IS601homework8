FROM python:3.12-bullseye
WORKDIR /myapp
COPY . /myapp/
RUN pip install -r requirements.txt
RUN pip install pytest
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]