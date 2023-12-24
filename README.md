# Raspberry Pi fan control

This code is to enable the turning on and off of any fan in the Raspberry Pi. The fan will turn on when the temperature of the CPU is above 65 degrees Celsius, and will turn off when the temperature is below 55 degrees Celsius.

## Environment tested on
- Raspberry Pi 4 Model B (4gb)
- Raspberry Pi OS (64-bit) with Desktop
- Python 3.11.2

## Default configuration
- Fan GPIO pin: 17
- Temperature threshold to turn on fan: 65 degrees Celsius
- Temperature threshold to turn off fan: 55 degrees Celsius