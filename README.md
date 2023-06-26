# Weather Mosaic Command Line Tool

<p align="center">
  <img alt="logo" src="gshraddha17/Github_Copilot_Hackathon_Weather_Mosaic/Weather_Mosaic_logo.jpeg">
</p>


Weather Mosaic is a command line tool that allows users to access weather information for different cities, change the language of weather reports, retrieve weather data through GPS functionality, view historical weather data, receive weather notifications, and use Telegram for weather queries.

## Table of contents

- [Installation](#installation)
- [Microsoft Azure Integration](#microsoft-azure-integration)
- [Telegram Integration](#telegram-integration)
- [Usage](#usage)
- [Chrome Extension](#chrome-extension)

## Installation

To use Weather Mosaic, please follow these steps:

1. Clone the repository or download the code files.

2. Install the required dependencies by running the following command:

```shell
pip install -r requirements.txt
```
3. Obtain API Keys:
   -> OpenWeatherMap API Key: Sign up on OpenWeatherMap and get an API key.

4. Set environment variables:
   * Create a .env file in the project directory.
   * Add the following environment variables and replace the values with your API keys and preferences:
   * Replace the placeholders with your own values.
   
```plaintext
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
```

5. You can use Microsoft Visual Studio Code to open the directory and terminal.

<p align="center">
  <img alt="VS Code in action" src="https://user-images.githubusercontent.com/35271042/118224532-3842c400-b438-11eb-923d-a5f66fa6785a.png">
</p>



### Set up your environment

-   **Step 1.** [Install a supported version of Python on your system](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites) 
-   **Step 2.** [Install the Python extension for Visual Studio Code](https://code.visualstudio.com/docs/editor/extension-gallery).

-   Select your Python interpreter by clicking on the status bar

     <img src=https://raw.githubusercontent.com/microsoft/vscode-python/main/images/InterpreterSelectionZoom.gif width=280 height=100>


## Microsoft Azure Integration 
* Weather Mosaic provides integration with Microsoft Azure services for weather notifications, GPS Location Retrieval, daily and hourly weather forecast .

<p align="center">
  <img alt="Azure" src="https://logos-world.net/wp-content/uploads/2021/02/Microsoft-Azure-Symbol.png">
</p>

Add the following environment variables also to the `.env` file you created earlier:

```plaintext
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
RECIPIENT_PHONE_NUMBER=your_recipient_phone_number
```
* Weather notifications will now be sent to the specified recipient phone number at the specified interval.

## Telegram Integration

Weather Mosaic provides integration with Telegram for weather queries. To set up Telegram integration:

* Create a new Telegram bot by following the instructions in the Telegram Bot documentation.

* Obtain the bot token for your newly created Telegram bot.

* Set the following environment variable in your .env file:

  ```plaintext
  TELEGRAM_BOT_TOKEN: Your Telegram bot token.
  ```
* Replace the placeholder with your own bot token.

## Usage

* To use Weather Mosaic, open a terminal or command prompt and navigate to the project directory.

### Run Your Code using the following command

```shell
python main.py
```

## Dashboard

* The dashboard provides various commands and functionalities. Type command followed by any required parameters to execute the corresponding action.
* To view the dashboard with all available commands, type `help`.

## Commands

* To view weather details of a specific city, type or say `weather {city_name}`.
Example:

```shell
  weather Lucknow
```

* To change the language of weather reports, type `change language`. Follow the prompts to select the desired language.

```shell
change language
```

* To retrieve weather data through GPS functionality, type `enable GPS`.

```shell
enable GPS
```

* To view historical weather data of a place, type `historical data`. Follow the prompts to enter the city name and date.

Example:

```shell
historical data
Enter city name: London
Enter date (YYYY-MM-DD): 2023-06-01
```

* To receive weather notifications, type `notifications`

```shell
notifications
```

* To save weather data for future use, type `save data`. Follow the prompts to enter the city name and date.

Example:

```shell
save data
Enter city name: London
Enter date (YYYY-MM-DD): 2023-06-01
```

* View weather details of any city through graphs and visuals, type `vizualization`
```shell
visualization
```

* To use Telegram for weather queries, type `telegram`.

```shell
telegram
```

  
## Chrome Extension

* Open Google Chrome and go to the Extensions page by entering the following URL in the address bar: chrome://extensions/

* Enable `Developer mode` by toggling the switch in the top-right corner of the Extensions page.

* Click on the `Load unpacked` button that appears.

* Select the folder where you cloned or downloaded the Chrome extension.

* The Chrome extension should now be loaded and visible in the Extensions page.




