# Use the official lightweight Python image from
# https://hub.docker.com/_/python
FROM python:3.9-slim 
RUN pip install --upgrade pip

# Copy all the files needed for the app to work
COPY inference.py .
COPY requirements.txt .
COPY models/ ./models

# Install all the necessary libraries
RUN pip3 install -r requirements.txt 

# Run the API!
CMD python inference.py
