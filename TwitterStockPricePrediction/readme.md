# TWITTER STOCK ANALYSIS PREDICTION APP

This repository contains the necessary files for deploying a sentiment analysis-based stock price prediction application. The application uses a trained machine learning model to analyze sentiment from text data and predict stock prices.

## Files

- `app.py`: This is the main Flask application file that handles the web server and API endpoints for the stock price prediction.
- `Stock_price_model.joblib`: This file contains the pre-trained machine learning model that predicts stock prices based on sentiment analysis.
- `prediction.html`: An HTML file that provides a user-friendly interface for inputting text data and displaying the predicted stock prices.
- `Twitter Stock Price from Sentiment Analysis.ipynb`: An IPython Notebook file that contains the code and documentation for training the machine learning model and performing sentiment analysis.

## Implementation

The stock price prediction application was implemented using the following steps:

1. **Data Collection**: Historical stock price data and corresponding tweets were collected. The tweets were used as text input for sentiment analysis.
2. **Sentiment Analysis**: The tweets were processed using the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool. This tool assigned sentiment scores (positive, negative, or neutral) to each tweet based on the presence of sentiment-related words.
3. **Model Training**: The sentiment scores and corresponding stock prices were used to train a machine learning model. In this case, a Linear Regression model was used to establish a correlation between sentiment scores and stock prices.
4. **Model Deployment**: The trained machine learning model was saved as `model.joblib` for later use in the application.
5. **Web Application**: The Flask web framework was used to develop a user interface for the stock price prediction. The `app.py` file defines the routes and API endpoints for handling user requests and generating predictions.
6. **HTML Interface**: The `index.html` file provides an intuitive user interface for inputting text data (tweets) and displaying the predicted stock prices.
7. **Deployment**: The application can be deployed locally or on a cloud platform such as Azure. Detailed instructions for deployment can be found in the previous sections of this README.

## Getting Started

To deploy the application and run it locally, follow the steps mentioned in the previous section.

## Additional Notes

- The `notebook.ipynb` file provides detailed documentation and code for training the machine learning model and performing sentiment analysis. It can be useful for understanding the model's architecture and making modifications if needed.
- If deploying the application on a cloud platform or server, make sure to configure the appropriate settings, such as environment variables, port numbers, and security considerations.
- Feel free to explore and modify the HTML file (`index.html`) to customize the user interface according to your requirements.

## License

This project is licensed under the MIT License. Feel free to use, modify
