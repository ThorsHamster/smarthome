# My Configuration for Home Assistant

Within this repository I'm sharing my Home Assistant configuration.

### Noteworthy stuff
- 22 automations in total
- FRITZ!Box Guest Wifi Control (custom_component)
- Turn coffee machine on when alarm clock rings (using Sleep As Android and a Wifi switch)
- Turn on bedroom lights 15m before my alarm starts (using Tasker and Sleep As Android)
- Many light automations (Turn on when arriving home, turn off when leaving, dim when TV is turned on, ...)
- Enable shuffle mode on spotify (shell script)
- WIP: Voice control everything via DIY Amazon Echo (using Dialogflow)


Most of the code / configuration is English except friendly names of frontend-facing entities (which are German).

### Main Dashboard (minimalistic)
![screenshot from 2017-12-02 22-29-33](https://user-images.githubusercontent.com/3121306/33519875-58172fa4-d7b0-11e7-91f8-77d4c4defc92.png)

### Admin Dashboard
![screenshot from 2017-12-02 22-30-46](https://user-images.githubusercontent.com/3121306/33519917-d0f4b540-d7b0-11e7-8f3c-ea6485d2235c.png)

### Raspberry PI Monitoring
![screenshot from 2017-12-02 22-33-03](https://user-images.githubusercontent.com/3121306/33519912-c9be9278-d7b0-11e7-8baa-3405679b56d2.png)


### Dependencies:
- nmap: device_tracker
- jq: Used for json parsing used in the spotify shuffle shell command
- python3 python3-venv python3-pip: Let's Encrypt
- libpython-dev libffi-dev libssl-dev: HTML5 push notifications
- libxslt-dev libxml2-dev python3-lxml: FRITZ!Box

Python:
- lxml, fritzconnection: FRITZ!Box (takes long installing)
