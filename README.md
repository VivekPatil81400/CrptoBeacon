# Cryptobeacon

Cryptobeacon is a Django-based web application that allows users to set alerts for cryptocurrencies. Users can define custom thresholds based on price changes or percentage fluctuations for their preferred cryptocurrencies. When the actual cryptocurrency prices cross these predefined thresholds, the system sends alerts to notify users.

## Features

- **User Registration and Authentication:**
  - Users can create accounts and log in securely to the application.
  - User authentication is managed using Django's built-in authentication system.

- **Cryptocurrency Alert Creation:**
  - Users can set alerts for specific cryptocurrencies.
  - Alerts can be based on either absolute price changes or percentage fluctuations.

- **Real-time Price Data:**
  - Cryptocurrency price data is obtained from reliable sources, providing accurate and up-to-date information.
  - Real-time data ensures that users receive timely alerts based on the latest market conditions.

- **Email Notifications:**
  - Users receive email notifications when cryptocurrency prices cross the defined thresholds.
  - Email notifications are sent using Django's email sending functionality.
