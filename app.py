import time
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import yaml
from typing import Dict
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value

from classes.LoggingManager import LoggerClass

# Create a Flask app
app = Flask(__name__)

relative_config_filepath = r'C:\Users\Admin\OneDrive\Desktop\_work\__repos (unpublished)\_____CONFIG\vertex-ai-marketing-frontend\config\config.yaml'

# get config
with open(relative_config_filepath) as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

dotenv_path = config.get('dotenv_path')
gcp_project_id = config.get('gcp_project_id')
vertex_endpoint_id = config.get('vertex_endpoint_id')

# Load environment variables
load_dotenv(dotenv_path=dotenv_path)

# Create logger
logger = LoggerClass(
    dirname='log',
    logger_name='main',
    debug_level='DEBUG',
    mode='w',
    stream_logs=True
).create_logger()

# Define a root route
@app.route('/')
def form():
    return render_template('form.html')

# Define a route to handle form submissions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    logger.info(f"Received data in /predict: {data}")

    # Convert the form data to the format expected by your model. This might involve some preprocessing.
    # For simplicity, let's assume the form data is already in the correct format.
    model_input = {
        "duration": data['duration'],
        "poutcome": data['poutcome'],
        "pdays": data['pdays'],
        "housing": data['housing'],
        "previous": data['previous'],
        "marital": data['marital'],
        "job": data['job'],
        "campaign": data['campaign'],
        "education": data['education'],
        "age": data['age'],
        "balance": data['balance'],
        "default": data['default'],
        "loan": data['loan']
    }
    logger.debug(f"model_input: {model_input}")

    # capture start time
    start_time = time.time()

    # Call your model prediction function here. You might need to adjust this call to match your function's parameters.
    prediction = predict_tabular_classification_sample(
        project=gcp_project_id,
        endpoint_id=vertex_endpoint_id,
        instance_dict=model_input,
        location="us-central1",
    )

    # capture end time
    end_time = time.time()
    runtime = end_time - start_time
    
    response = {
        "prediction": prediction,
        "runtime": runtime
    }

    logger.debug(f"response: {response}")
    return jsonify(response)  # Return the combined response as JSON


def predict_tabular_classification_sample(
    project: str,
    endpoint_id: str,
    instance_dict: Dict,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}

    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    
    # for more info on the instance schema, please use get_model_sample.py
    # and look at the yaml found in instance_schema_uri
    instance = json_format.ParseDict(instance_dict, Value())
    instances = [instance]
    parameters_dict = {}
    parameters = json_format.ParseDict(parameters_dict, Value())
    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id
    )
    response = client.predict(
        endpoint=endpoint, instances=instances, parameters=parameters
    )
    logger.debug("prediction service endpoint response:")
    logger.debug(f"deployed_model_id: {response.deployed_model_id}")
    
    # See gs://google-cloud-aiplatform/schema/predict/prediction/tabular_classification_1.0.0.yaml for the format of the predictions.
    # Convert the protobuf messages to dictionaries
    predictions = [dict(prediction) for prediction in response.predictions]

    return predictions

if __name__ == '__main__':
    app.run(
        debug=True,
        port=3300
        )