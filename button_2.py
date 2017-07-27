import paho.mqtt.client as mqtt
from gpiozero import Button
from signal import pause

button = Button(4)

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)

def button_press():
	print("button_clicked")
	client.publish("test/project", "Table 2")

button.when_pressed = button_press
print"connected"
pause()
