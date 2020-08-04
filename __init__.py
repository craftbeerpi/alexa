# -*- coding: utf-8 -*-
from flask_ask import Ask, request, session, question, statement

from modules import app, cbpi
import logging


ask = Ask(app, "/")

@ask.launch
def launch():
    speech_text = 'Welcome to CraftBeerPi Alexa Plugin'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


@ask.intent('Update')
def update():
    s = cbpi.cache.get("active_step")
    text = "Here is your update. "
    if s is not None:
        text = text + 'The current step is %s . ' % (s.name,)

    else:
        text = text + 'There is no brewing process running .'
    text = text + "Now to the brewing kettles. "

    for idx, value in cbpi.cache["kettle"].items():
        current_sensor_value = cbpi.get_sensor_value(value.sensor)
        text = text + "%s has set target temperature to %s and a current temperature of %s. " % (value.name, value.target_temp, current_sensor_value)

    text = text + "Any further question?"

    return question(text).reprompt(text).simple_card('CBP Update', text)

@ask.intent('SensorIntent', mapping={'sensor': 'Sensor'})
def sensor_value(sensor):
    print("SENSOR", sensor)
    for idx, value in cbpi.cache["sensors"].items():
        print(value.__dict__)
        if value.name.lower() == sensor:
            v = cbpi.get_sensor_value(value.id)
            speech_text = 'The sensor temperature is %s %s' % (v, value.instance.get_unit())
            return question(speech_text).reprompt(speech_text).simple_card('Value Name', speech_text)

    speech_text = "I have notf found the sensor %s. Any further question?" % sensor
    return question(speech_text).reprompt(speech_text).simple_card('Sensor Value', speech_text)

@ask.intent('KettleIntent', mapping={'kettle': 'K'})
def kettle_value(kettle):
    print("KETTLE", kettle)
    for idx, value in cbpi.cache["kettle"].items():
        if value.name.lower() == kettle:
            v = cbpi.get_sensor_value(value.sensor)
            s = cbpi.cache["sensors"].get(int(value.sensor))
            speech_text = 'The Kettle Temperature of %s is %s %s' % (str(kettle), v, s.instance.get_unit())

            return question(speech_text).reprompt(speech_text).simple_card('Kettle Value', speech_text)
            #return statement(speech_text).simple_card('Kettle Value', speech_text)

        speech_text = "I have not found the kettle %s. Any further question?" % kettle
    return question(speech_text).reprompt(speech_text).simple_card('Kettle Value', speech_text)


@ask.intent('ActorIntent', mapping={'actor': 'Actor'})
def toggle_actor(actor):

    for idx, value in cbpi.cache["actors"].items():
        if value.name.lower() == actor:

            if value.state == 1:
                cbpi.switch_actor_off(value.id)
                speech_text = 'Ok, I switched %s off ' % actor
            else:
                cbpi.switch_actor_on(value.id)
                speech_text = 'Ok, I switched %s on ' % actor

            return question(speech_text).reprompt(speech_text).simple_card('Actor Toggle', speech_text)

        speech_text = "I have not found the actor %s. Any further question?" % actor
    return question(speech_text).reprompt(speech_text).simple_card('Kettle Value', speech_text)


@ask.intent('StepIntent')
def step_intent(kettle):
    s = cbpi.cache.get("active_step")
    if s is not None:
        speech_text = 'The current step is %s' % (s.name, )
        return question(speech_text).reprompt(speech_text).simple_card('Step Name', speech_text)

    else:
        speech_text = 'There is no brewing process running'
        return question(speech_text).reprompt(speech_text).simple_card('Step Name', speech_text)

@ask.intent('Goodbye')
def goodbye(kettle):
    speech_text = "OK don't for get to donate some beer to Manuel! Goodbye"
    return statement(speech_text).simple_card("Goodbye", speech_text)


@ask.session_ended
def session_ended():
    return "{}", 200
