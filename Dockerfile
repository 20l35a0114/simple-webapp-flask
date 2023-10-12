FROM python
COPY . /opt/app-code
# Dockerfile


RUN pip install flask
RUN pip install flask-mysql
ENV BACKGROUND_COLOR=blue
ENV TEXT_COLOR=red
ENTRYPOINT FLASK_APP=/opt/app-code/app.py flask run --host=0.0.0.0