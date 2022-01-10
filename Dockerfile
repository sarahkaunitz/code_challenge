# Use the Python Docker Image to speed up the process
FROM python:3


RUN apt-get update
# RUN apt-get -y install git 
# RUN apt-get install -y vim 

# Copy Python-specific library information into their appropriate locations
COPY ./utils.py /AI_Engineer/code_challenge/
COPY ./requirements.txt /AI_Engineer/code_challenge/
COPY ./functions.py /AI_Engineer/code_challenge/


# Install necessary Python libraries to build the Virtual Environment
RUN pip install --upgrade pip
# RUN pip install virtualenv
# RUN python3 -m venv /opt/venv

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
# RUN /opt/venv/bin/pip install -r requirements.txt

# Future work: Option to ADD environment variables that the user passes into the Container 
# ENV FRAUD_FPATH ""
# ENV TRANSACTIONS_FPATH ""
WORKDIR /Users/sarahkaunitz/Documents/deloitte/AI_Engineer/code_challenge

# Run the application:
COPY main.py ./
CMD ["python", "./main.py"]

# Command that is run at the Container runtime