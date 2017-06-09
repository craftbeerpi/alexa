# alexa
Amazon Alexa Plugin for CraftBeerPi

# Installation

Please download and install this plugin via the CraftBeerPi user interface.

You need to run the following command on your Raspberry Pi to install the missing python libs

<code>pip install flask-ask</code>

## Flask Ask Video Tutorial

Just follow this tutorial and just use the CBPi IntentSchema and Utterances

https://www.youtube.com/watch?v=cXL8FDUag-s

## Ngrok

Install ngrok to create a secure tunnel to your local network.

https://ngrok.com/

### Intent Schema

```
{
  "intents": [
    {
      "intent": "Goodbye"
    },
    {
      "intent": "Update"
    },
    {
      "intent": "StepIntent"
    },
    {
      "slots": [
        {
          "name": "Sensor",
          "type": "AMAZON.LITERAL"
        }
      ],
      "intent": "SensorIntent"
    },
    {
      "slots": [
        {
          "name": "K",
          "type": "AMAZON.LITERAL"
        }
      ],
      "intent": "KettleIntent"
    },
    {
      "slots": [
        {
          "name": "Actor",
          "type": "AMAZON.LITERAL"
        }
      ],
      "intent": "ActorIntent"
    }
  ]
}
```

### Sample Utterances

```
Goodbye No thanks
Goodbye Stop
Update for the current state
Update give my a the current status
Update current status
Update status update please
StepIntent what step is running
StepIntent what is the current step
StepIntent current step
SensorIntent  value of sensor {Test|Sensor}
SensorIntent  value of sensor {Sensor|Sensor}
SensorIntent  value of sensor {Thermometer|Sensor}
SensorIntent  what is value of sensor {Test|Sensor}
SensorIntent  what is current value of sensor {Test|Sensor}
SensorIntent  what is the current value of sensor {Test|Sensor}
SensorIntent tell me the value of sensor {Test|Sensor}
KettleIntent  temperature of kettle {Mash Tun|K}
KettleIntent  what is temperature of kettle {Mash Tun|K}
KettleIntent  what is current temperature of kettle {Mash Tun|K}
KettleIntent  what is the current temperature of kettle {Mash Tun|K}
KettleIntent  temperature of kettle {Hot Liquor Tank|K}
KettleIntent  what is temperature of kettle {Hot Liquor Tank|K}
KettleIntent  what is current temperature of kettle {Hot Liquor Tank|K}
KettleIntent  what is the current temperature of kettle {Hot Liquor Tank|K}
KettleIntent  temperature of kettle {Boil Kettle|K}
KettleIntent  what is temperature of kettle {Boil Kettle|K}
KettleIntent  what is current temperature of kettle {Boil Kettle|K}
KettleIntent  what is the current temperature of kettle {Boil Kettle|K}
ActorIntent  toggle actor {heater|Actor}
ActorIntent  toggle actor {agiator|Actor}
ActorIntent  toggle actor {pump|Actor}
```
