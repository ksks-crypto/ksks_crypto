from machine import Pin
import utime as time
from dht import DHT11

# Pin connected to the DHT11 data line
dataPin = 16

# Set up the DHT11 sensor
myPin = Pin(dataPin)  # Let the DHT11 library handle pin mode
sensor = DHT11(myPin)

while True:
    try:
        # Measure temperature and humidity
        sensor.measure()
        tempC = sensor.temperature()
        hum = sensor.humidity()

        # Print the results
        print(f"Temperature: {tempC}°C, Humidity: {hum}%")
    except Exception as e:
        # Handle any errors in reading the sensor
        print(f"Error reading sensor: {e}. Check wiring, pin setup, and power.")
    
    # Wait for 2 seconds before reading again
    time.sleep(2)
