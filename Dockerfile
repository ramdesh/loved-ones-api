from python:3.8

copy . /app
WORKDIR /app
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
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

# Datasets
RUN mkdir dataset_cache && \
curl https://s3.amazonaws.com/datasets.huggingface.co/personachat/personachat_self_original.json > dataset_cache/personachat_self_original.json && \
curl https://s3.amazonaws.com/models.huggingface.co/transfer-learning-chatbot/gpt_personachat_cache.tar.gz > dataset_cache/gpt_personachat_cache.tar.gz


CMD gunicorn --bind 0.0.0.0:5001 --timeout=1200 wsgi:loved_ones

EXPOSE 5001