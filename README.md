# Vertex AI Flask Integration Example

This README was generated with the help of GPT-4, detailing a basic web application that uses Flask to interact with Vertex AI endpoints for making predictions. The application demonstrates how to set up a simple form to collect user inputs, send them to Vertex AI for processing, and display the results. This project serves as an example for those looking to integrate Google Cloud's AI capabilities into their Flask applications.

## Overview

The project is structured around a Flask app (`app.py`) that handles web requests and communicates with Google Cloud's Vertex AI. It includes:

- A form for user input (`form.html`).
- A script to process the form and make API requests (`form.js`).
- A Flask application (`app.py`) that serves the form and handles submissions to Vertex AI.
- A custom logging class (`LoggerClass`) to facilitate debugging and monitoring.

## Key Features

- **Flask Web Server**: Serves a web form and handles interactions.
- **Vertex AI Integration**: Uses Vertex AI endpoints for making predictions based on user input.
- **Environment Configuration**: Leverages `dotenv` for managing environment variables securely.
- **Custom Logging**: Implements a custom logging mechanism for enhanced debugging.

## Data and Model

The model used in this application was trained on a common direct marketing dataset from banking companies, focusing on customer contact during a campaign. The dataset includes various features like customer job, marital status, education, and previous campaign outcomes.

The model was built using AutoML through Vertex AI, automating the selection of the best model architecture and parameters. However, the steps involved in creating and training the model are not included in this repository. This application focuses on demonstrating the integration and usage of the trained model via Vertex AI endpoints.

## Usage

1. Clone the repository to your local machine.
2. Ensure you have Python installed and create a virtual environment.
3. Install dependencies by running `pip install -r requirements.txt`.
4. Set up your Google Cloud credentials and update the `.env` file with your `gcp_project_id`, `vertex_endpoint_id`, and other configurations.
5. Run `app.py` to start the Flask server.
6. Navigate to `localhost` in your web browser to access the form, input your data, and see the predictions.

## Contributing

This project is a simple example, and contributions are welcome. Whether it's extending functionality, improving the UI, or enhancing security, feel free to fork the repo and submit a pull request.

## Acknowledgments

- Much of the code in this repository was built with the assistance of GPT-4, demonstrating its utility in generating code snippets and documentation.
- Google Cloud Platform and Vertex AI for providing the AI and machine learning infrastructure.

## Disclaimer

This project is for demonstration purposes and is not intended for production use without further development, particularly in terms of security and scalability. Use at your own risk.