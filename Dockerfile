# Use the Python Docker Image to speed up the process
FROM python

RUN apt-get update

# Set the working directory 
WORKDIR /code_challenge

# Copy required files and information into their appropriate locations
COPY datasets/ /code_challenge/datasets
COPY requirements.txt /code_challenge/
ADD . /code_challenge 

RUN pip install --upgrade pip

# Install dependencies
RUN pip3 install -r requirements.txt

# Run the application:
COPY main.py main.py
CMD ["python3", "main.py"]