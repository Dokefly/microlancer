
# Microlancer Notification

Microlancer Notification is a telegram bot that notifies each new task added to the platform.

## Installing dependencies

```bash
sudo su && apt-get update
apt-get upgrade && apt-get install python3
apt-get install python3-pip && apt-get install git
git clone https://github.com/Dokefly/microlancer/
cd microlancer/ && pip3 install requirements.txt
```

## Configuring the bot

```
python3 app.py --token 'Your access token' --user 'user of the group where the bot was added'
```

## Starting the bot

```
python3 app.py
```
