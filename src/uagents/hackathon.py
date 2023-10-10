from flask import ctx
from uagents import Agent, Context, Model
import requests

# Define the API endpoint for fetching real-time temperatures
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

# Define a data model for the TemperatureAlert message
class TemperatureAlert(Model):
    location: str
    current_temperature: float

# Create a Temperature Alert Agent
class TemperatureAlertAgent(Agent):
    def __init__(self, location, api_key, min_temperature, max_temperature):
        super().__init__()
        self.location = location
        self.api_key = api_key
        self.min_temperature = min_temperature
        self.max_temperature = max_temperature

    def fetch_current_temperature(self):
        params = {"q": self.location, "appid": self.api_key, "units": "metric"}
        response = requests.get(API_ENDPOINT, params=params)
        ctx.logger.info(f'API Request URL: {response.url}')  # Log the API request URL

        if response.status_code == 200:
            json_response = response.json()
            current_temperature = json_response["main"]["temp"]
            ctx.logger.info(f'Current temperature in {self.location}: {current_temperature}°C')
            return current_temperature
        else:
            ctx.logger.error(f'API request failed with status code {response.status_code}')
            raise Exception("API request failed")


    async def check_temperature(self, ctx: Context):
        current_temperature = self.fetch_current_temperature()
        ctx.logger.info(f'Current temperature in {self.location}: {current_temperature}°C')

        if current_temperature < self.min_temperature or current_temperature > self.max_temperature:
            # Temperature is outside the preferred range, send an alert
            alert_message = f"Temperature in {self.location} is outside the preferred range: {current_temperature}°C"
            ctx.logger.warning(alert_message)

            # Create and send a TemperatureAlert message
            alert = TemperatureAlert(location=self.location, current_temperature=current_temperature)
            await ctx.send(self.address, alert)

        # Schedule the task to run again after 1800 seconds (30 minutes)
        await ctx.sleep(1800)

if __name__ == "__main__":
    # Replace with your OpenWeatherMap API key, location, and preferred temperature range
    api_key = "5088bdf83d93cc7ad40a1bbb30de4608"
    location = "London, UK"  # Replace with your desired location
    min_temperature = 20  # Minimum preferred temperature in °C
    max_temperature = 30  # Maximum preferred temperature in °C

    temperature_alert_agent = TemperatureAlertAgent(location=location, api_key=api_key, min_temperature=min_temperature, max_temperature=max_temperature)
    temperature_alert_agent.run()
