# Code-Challenge

## This directory contains all of the files and information required for the AI Engineer Code Challenge 

### Includes:
Files:
- `Dockerfile` to create a docker image and run a container 
- `requirements.txt` file to denote which packages are required 
- `main.py` file that is used to execute all of the required functionality and produce the appropriate results and reports 
	- `functions.py` contains all the functions the `main.py` file uses
	- `utils.py` contains all the credit card vendor information initially provided and used in the functions file 
- `fraud_detection_modeling_nb.ipynb` is a notebook that creates an ML model that is useful using the datasets provided with accuracy metrics 

Directories:
- `/datasets` contains all the provided datasets needed to perform analysis 
- `/output_data` dataset created and used specifically for the ML Modeling portion of the analysis in `fraud_detection_modeling_nb.ipynb`
- `/results` contains the output .json and binary file format data after all analysis has been completed 
- `/test_datasets` contains small datasets that are used in the Unit Testing portion of the analysis... follows same format as the `/datasets` data provided 
- `/tests` contains the pytest script to perform Unit Testing on the functions 


## Options 

### - Can run the `main.py` script that executes all of the designated functions and produces three important outputs:
	1. A report of the number of fraudulent transactions per state
	2. A report of the number of fraudulent transactions per vendor
	3. A dataframe in the /results directory of all the valid transactions with the last nine digits of their credit card number masked with '*'
Example: `python3 main.py` 

### - Perform Unit Testing 
Example: `pytest tests/pytest_script.py`

## Docker
### Building the docker image 
> Terminal Command `docker build -t choice_of_name_for_image .`
### Running the container 
> Terminal Command `docker run choice_of_name_for_image:tag_name` 


Link to Github: https://github.com/sarahkaunitz/code_challenge