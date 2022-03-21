FROM PYTHON:3.9.7

ADD language_translator.py .


RUN pip install translate

CMD [ "python", "./language_translator.py" ]