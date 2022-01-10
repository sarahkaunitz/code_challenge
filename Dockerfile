# Use the Python Docker Image to speed up the process
FROM python:3

# Set the working directory 
WORKDIR /code_challenge

RUN apt-get update

# Copy required files and information into their appropriate locations
COPY utils.py utils.py 
COPY requirements.txt requirements.txt 
COPY functions.py functions.py 
COPY requirements.txt requirements.txt
COPY datasets /code_challenge/datasets
ADD . /code_challenge 
RUN pip install --upgrade pip

# Install dependencies
RUN pip3 install -r requirements.txt

# Run the application:
COPY main.py main.py
CMD ["python3", "main.py"]