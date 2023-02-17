FROM python

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./src /code/src

RUN mkdir -p ./static
#
WORKDIR /code/src
CMD ["python3", "main.py"]