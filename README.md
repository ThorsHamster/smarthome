[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cc131252ac754da387079ab6215f7617)](https://www.codacy.com/manual/ThorsHamster/smarthome?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ThorsHamster/smarthome&amp;utm_campaign=Badge_Grade)
[![CodeFactor](https://www.codefactor.io/repository/github/thorshamster/smarthome/badge)](https://www.codefactor.io/repository/github/thorshamster/smarthome)

# SmartHome

It's a fork from [mammuth](https://github.com/mammuth/home-assistant-configuration). Thanks!

## Sensors

*   Medtronic Sensor for insulin pump data and notifications, see [contour-next-link](https://github.com/ThorsHamster/contour-next-link)
*   1x Aqara Temperature, Humidity, Air Pressure
*   1x Aqara Water sensor
*   2x Tradfri Remote
*   Raspberry Pi CPU temperature sensor
*   Raspberry Pi systemmonitor
*   pihole sensor
*   Daytime

## Actuators

*   1x Sonoff Switches (MQTT)
*   Sonoff Switch
*   2x Shelly plug
*   telegram

## Hardware

Running on a Raspberry Pi 3. \
RaspBee premium from dresden elektronik is used for all ZigBee Components.

## Software

Hass.io running in a docker container. \
Deconz (for RaspBee) running in a docker container. \
See [docker-compose.yml](docker-compose.yml) for details.

## Automations

*   No-one-at-Home and Coming-Home functionality
*   Notification if new device in network
*   Dark Mode and Main Theme
*   Tradfri Remotes for lights
*   Notification if aquarium would loose water
*   Notification if the humidity of humidor is too high or too low
*   Notification if newer version of hass.io is available
*   Notification if insulin pump has an not acknowledge message
*   Notification if blood glucose level is under a specified value (as a warning)
*   Notification if blood glucose level is supposed to get low (as a prediction)

## Screenshots

![Medtronic Dashboard1](https://user-images.githubusercontent.com/48162347/226168182-5571d239-26eb-4016-9219-178bd5f371b5.jpg)
![Medtronic Dashboard1](https://user-images.githubusercontent.com/48162347/226168180-fbff2860-c482-4865-8352-f4da57b23469.jpg)

![main](https://user-images.githubusercontent.com/48162347/63213761-8b2b0280-c110-11e9-969c-2f7ce5544fc2.png)

![graph](https://user-images.githubusercontent.com/48162347/63213769-9ed66900-c110-11e9-8056-cf1a4c4c3f80.png)

![admin](https://user-images.githubusercontent.com/48162347/63213772-a564e080-c110-11e9-8528-ebe9318fc1dc.png)

![pi](https://user-images.githubusercontent.com/48162347/63213777-aac22b00-c110-11e9-9df5-3499f6ab8988.png)

![sensor_overview](https://user-images.githubusercontent.com/48162347/63213778-b01f7580-c110-11e9-8615-d4527fa8f8c9.png)
