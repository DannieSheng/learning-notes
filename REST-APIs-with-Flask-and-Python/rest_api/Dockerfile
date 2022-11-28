FROM python:3.10
EXPOSE 5000
WORKDIR /app
RUN pip install flask
# copy everything from current folder to current folder
# or COPY . /app
COPY . .
# command should run when this image starts up as a container
CMD ["flask", "run", "--host", "0.0.0.0"]