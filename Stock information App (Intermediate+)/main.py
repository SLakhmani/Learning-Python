import requests
import smtplib

# Email details
SENDER = "youremail@yahoo.com"
SENDER_PASSWORD = "yourpassword12345"
RECEIVER = "receiveremail@yahoo.com"

# NOTE: for security, it is important to store api keys as environment variables
#       and call them using os.environ() when needed
# Use https://www.alphavantage.co to get Stock data
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

alpha_vantage_API_KEY = "your_alpha_vantage_api_key"
alpha_vantage_API_ENDPOINT = "https://www.alphavantage.co/query"

news_API_KEY = "your_news_api_key"
news_API_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "apikey": alpha_vantage_API_KEY,
    "symbol": STOCK,
    "function": "TIME_SERIES_DAILY",
}

stock_response = requests.get(alpha_vantage_API_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

yesterday_closing = float(stock_data_list[0]["4. close"])
day_before_closing = float(stock_data_list[1]["4. close"])
closing_difference = yesterday_closing - day_before_closing

up_down = None
if closing_difference > 0:
    up_down = "⬆"
else:
    up_down = "⬇"

diff_percent = round((closing_difference / yesterday_closing) * 100)

# Use https://newsapi.org to get news articles
if abs(diff_percent) > 5:
    news_params = {
        "apiKey": news_API_KEY,
        "qInTitle": COMPANY_NAME,

    }

    news_response = requests.get(news_API_ENDPOINT, params=news_params)
    news_articles = news_response.json()["articles"]
    first_three_articles = news_articles[:3]

    formatted_articles = [f"Headline: {article['title']}\nBrief: {article['description']}\n"
                          for article in first_three_articles]

    email_subject = f"Subject:{STOCK}: {up_down} {diff_percent}%\n\n"
    email_body = ""
    for articles in formatted_articles:
        email_body = email_body + articles

    message_final = email_subject + email_body

    try:
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(SENDER, SENDER_PASSWORD)
            connection.sendmail(SENDER, RECEIVER, message_final)
    except:
        print("Unable to send email...")
    else:
        print("Email sent successfully!")



