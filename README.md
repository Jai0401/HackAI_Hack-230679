```markdown
# Temperature Alert Agent

## Description
The Temperature Alert Agent is a Python script that uses the uAgents library to fetch real-time temperatures from a free weather API for a specified location. It allows users to set their preferred temperature range (minimum and maximum temperature) and sends an alert/notification when the current temperature in the chosen location goes below the minimum or above the maximum threshold.

## Instructions to Run
To run the Temperature Alert Agent, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/temperature-alert-agent.git
   ```

2. Navigate to the project directory:

   ```bash
   cd temperature-alert-agent
   ```

3. Install the required dependencies using Poetry:

   ```bash
   poetry install
   ```

4. Set your OpenWeatherMap API key and preferred location in the `hackathon.py` script:

   ```python
   api_key = "Your_OpenWeatherMap_API_Key"
   location = "Your_Location"  # e.g., "London, UK"
   min_temperature = 20  # Minimum preferred temperature in °C
   max_temperature = 30  # Maximum preferred temperature in °C
   ```

5. Run the Temperature Alert Agent:

   ```bash
   python hackathon.py
   ```

The agent will start fetching the current temperature for the specified location and send alerts if the temperature goes outside the preferred range.

## Special Considerations
- Make sure you have a valid OpenWeatherMap API key. You can obtain one by signing up on the [OpenWeatherMap website](https://openweathermap.org/).
- The agent fetches temperature data every 30 minutes by default. You can adjust the update interval by changing the `period` parameter in the `check_temperature` method in the `hackathon.py` script.
- Ensure that your environment allows outbound internet connections for API requests.

Feel free to reach out for any questions or assistance with running the Temperature Alert Agent.
```

You can copy and paste this code into a `README.md` file in your project repository, and replace `"Your_OpenWeatherMap_API_Key"` and `"Your_Location"` with your actual API key and location.
