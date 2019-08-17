# SmartHome

It's a fork from [mammuth](https://github.com/mammuth/home-assistant-configuration). Thanks!

## Sensors
- 1x Aqara Temperature, Humidity, Air Pressure
- 1x Aqara Water sensor
- 2x Tradfri Remote
- GMaps Sensors
- Raspberry Pi CPU temperature sensor
- Raspberry Pi systemmonitor
- pihole sensor
- Daytime

## Actuators
- 1x Tradfri Light bulb E27 WS opal 980lm
- 1x Tradfri Light bulb E27 W opal 1000lm
- 2x Sonoff Switches (MQTT)
- telegram
- xmpp (jabber)

## Hardware

Running on a Raspberry Pi 3. \
RaspBee premium from dresden elektronik is used for all ZigBee Components.

## Software

Hass.io running in a docker container. \
Deconz (for RaspBee) running in a docker container. \
See [docker-compose.yml](docker-compose.yml) for details.

## Automations

- Notification if driving time is longer than usual (telegram, GMaps), also for carpool
- Turn on / off of Guest Wifi
- Heating blanket automations
- No-one-at-Home and Coming-Home functionality
- Light automations
- Notification if new device in network
- Dark Mode and Main Theme
- Tradfri Remotes for lights
- Notification if aquarium would loose water
- Notification if the humidity of humidor is too high
- Notification if newer version of hass.io is available
