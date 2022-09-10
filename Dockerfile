FROM python:3.9-slim

RUN apt-get update
RUN export DEBIAN_FRONTEND=noninteractive
    # Language tool needs java
    # Huh? https://github.com/geerlingguy/ansible-role-java/issues/64
RUN mkdir -p /usr/share/man/man1/
RUN apt-get -y install --no-install-recommends default-jre
RUN pip install --no-cache-dir \
        language-tool-python==2.5.1 \
        requests==2.25.1 \
        tweepy==3.10.0 \
        language-tool-python==2.5.1 \
        flask==1.1.2 \
        gunicorn==20.1.0
# RUN rm -rf /var/lib/apt/lists/* && \
    # pip cache purge && \

# We need to do this before installing language tool because it needs to be available to myuser
# See https://github.com/jxmorris12/language_tool_python/blob/master/language_tool_python/utils.py
ENV LTP_PATH /home/ltp

# Need to instantiate it to get it to download for some reason...
RUN mkdir -p /home/ltp && \
    python -c "from language_tool_python import LanguageTool; lt = LanguageTool('en-GB')" && \
    chmod -R 777 ${LTP_PATH}

COPY ascii_words.pickle sentences.pickle ./

COPY *.py ./

RUN adduser myuser
USER myuser

CMD gunicorn --bind 0.0.0.0:$PORT app
