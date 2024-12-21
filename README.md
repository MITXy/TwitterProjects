# Twitter (X) Projects Repository

This repository contains a collection of data-driven projects based on data obtained from **Twitter (now X)**. These projects leverage cutting-edge Natural Language Processing (NLP) techniques, machine learning models, and data analytics to analyze and derive insights from Twitter data. Additionally, the repository includes applications like **stock price prediction**, **anomaly detection**, and more.

---

## Projects Overview

### 1. **NLP for Sentiment Analysis**
   - **Description**: Analyzes Twitter sentiment to extract public opinion on various topics, including specific stocks or companies.
   - **Key Features**:
     - Sentiment classification (positive, neutral, negative)
     - Topic modeling and keyword extraction
     - Visualization of sentiment trends over time
   - **Tech Stack**: Python, NLTK, spaCy, Transformers (HuggingFace)

### 2. **Stock Price Prediction Using Twitter Sentiment**
   - **Description**: Uses sentiment scores derived from Twitter posts to predict stock price movement.
   - **Key Features**:
     - Correlation analysis between sentiment and stock prices
     - Predictive models integrating sentiment with historical stock data
     - Backtesting and performance evaluation
   - **Tech Stack**: Python, scikit-learn, XGBoost, Yahoo Finance API

### 3. **Anomaly Detection in Tweet Activity**
   - **Description**: Identifies unusual patterns in tweet activity, such as sudden spikes in mentions or trending topics.
   - **Key Features**:
     - Detection of outliers in time series data
     - Alerts for potentially significant events
     - Integration with streaming Twitter data for real-time analysis
   - **Tech Stack**: Python, Pandas, Matplotlib, Prophet

### 4. **Topic Modeling and Clustering**
   - **Description**: Groups tweets into clusters to identify major themes or topics.
   - **Key Features**:
     - Latent Dirichlet Allocation (LDA) for topic extraction
     - Visualization of clusters using t-SNE or UMAP
     - Applications in market research and public opinion tracking
   - **Tech Stack**: Python, Gensim, scikit-learn, Plotly

### 5. **Hashtag and Network Analysis**
   - **Description**: Explores the relationships between hashtags and the social network of Twitter users.
   - **Key Features**:
     - Graph-based analysis of hashtag co-occurrence
     - Centrality and influence metrics for users
     - Applications in identifying influencers and trending topics
   - **Tech Stack**: Python, NetworkX, Gephi

---

## Installation

### Prerequisites
- Python >= 3.8
- API Access to Twitter (X) via [Twitter Developer Platform](https://developer.twitter.com/)
- Required libraries: TensorFlow, scikit-learn, Pandas, Matplotlib, Plotly, and Tweepy

### Steps to Set Up

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/twitter-projects.git
   cd twitter-projects
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Twitter API Keys**:
   - Obtain API keys from the [Twitter Developer Platform](https://developer.twitter.com/).
   - Save the keys in a `.env` file in the root directory:
     ```env
     TWITTER_API_KEY=your_api_key
     TWITTER_API_SECRET_KEY=your_api_secret_key
     TWITTER_ACCESS_TOKEN=your_access_token
     TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
     ```

---

## Directory Structure

```
twitter-projects/
├── data/                     # Directory for raw and processed data
├── models/                   # Trained models for predictions
├── notebooks/                # Jupyter notebooks for exploration
├── src/                      # Source code for all projects
│   ├── sentiment_analysis.py
│   ├── stock_prediction.py
│   ├── anomaly_detection.py
│   ├── topic_modeling.py
│   └── network_analysis.py
├── requirements.txt          # List of dependencies
├── README.md                 # Project documentation
└── .env                      # Twitter API credentials
```

---

## Usage

1. **Sentiment Analysis**:
   - Run `sentiment_analysis.py` to classify tweets and analyze sentiment trends.

   ```bash
   python src/sentiment_analysis.py
   ```

2. **Stock Price Prediction**:
   - Execute `stock_prediction.py` to correlate sentiment with stock price changes.

   ```bash
   python src/stock_prediction.py
   ```

3. **Anomaly Detection**:
   - Use `anomaly_detection.py` to identify irregular patterns in tweet activity.

   ```bash
   python src/anomaly_detection.py
   ```

4. **Topic Modeling**:
   - Run `topic_modeling.py` to group tweets into clusters.

   ```bash
   python src/topic_modeling.py
   ```

5. **Hashtag and Network Analysis**:
   - Execute `network_analysis.py` to analyze hashtag relationships and user networks.

   ```bash
   python src/network_analysis.py
   ```

---

## Future Plans

1. **Real-Time Dashboard**:
   - Develop a real-time dashboard for sentiment and anomaly tracking.

2. **Multilingual Support**:
   - Expand NLP capabilities to analyze tweets in multiple languages.

3. **Enhanced Prediction Models**:
   - Integrate deep learning models for better prediction accuracy.

4. **User Engagement Metrics**:
   - Add features to measure user influence and engagement.

---

## Contributions

Contributions are welcome! If you have ideas or improvements, feel free to submit a pull request or open an issue.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- **Twitter Developer Platform** for providing access to data.
- **HuggingFace** for their NLP models.
- **Open Source Community** for the tools and frameworks that made this possible.

