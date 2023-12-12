from python:3.7

copy . /app
WORKDIR /app
RUN pip install numpy
RUN pip install -r requirements.txt
RUN pip install gunicorn
ENV FLASK_APP /app/server.py

# model zoo
RUN mkdir models && \
    curl https://s3.amazonaws.com/models.huggingface.co/transfer-learning-chatbot/finetuned_chatbot_gpt.tar.gz > models/finetuned_chatbot_gpt.tar.gz && \
    cd models/ && \
    tar -xvzf finetuned_chatbot_gpt.tar.gz && \
    rm finetuned_chatbot_gpt.tar.gz

CMD gunicorn --bind 0.0.0.0:5000 --timeout=600 wsgi:basilar

EXPOSE 5000