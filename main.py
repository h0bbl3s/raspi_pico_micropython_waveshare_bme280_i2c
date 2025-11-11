# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-bme280-micropython/
# updated by h0bbl3s at https://github.com/h0bbl3s/raspi_pico_micropython_waveshare_bme280_i2c

from machine import Pin, I2C
from time import sleep
import BME280
import utime

# Initialize I2C communication
# pin 5 and  pin 4 match pico i2c0 scl and sda 
i2c = I2C(id=0, scl=Pin(5), sda=Pin(4), freq=10000)

# do a one time scan for i2c devices and print the result
# if this program isn't working, check that this result matches the
# address in BME280.py, if not then edit BME280.py.
devices = i2c.scan()
print('i2c scan result: ', [hex(device) for device in devices], '\n')

# Initialize the RTC - thonny will set it to your system time :)
rtc=machine.RTC()

while True:
    try:
        # set up the timestring
        timestamp = rtc.datetime()
        timestring = "%04d-%02d-%02d %02d:%02d:%02d"%(timestamp[0:3] +
                                                      timestamp[4:7])
        # Initialize BME280 sensor
        bme = BME280.BME280(i2c=i2c)
        
        # Read sensor data
        tempC = bme.temperature
        hum = bme.humidity
        pres = bme.pressure
        
        # Convert temperature to fahrenheit
        tempF = (bme.read_temperature()/100) * (9/5) + 32
        tempF = str(round(tempF, 2)) + 'F'
        
        # Print time
        print(timestring)
        # Print sensor readings
        print('Temperature: ', tempC)
        print('Temperature: ', tempF)
        print('Humidity: ', hum)
        print('Pressure: ', pres, '\n')
        
    except Exception as e:
        # Handle any exceptions during sensor reading
        print('An error occurred:', e)

    sleep(5)
