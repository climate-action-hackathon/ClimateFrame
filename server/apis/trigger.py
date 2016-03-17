import pulse
from actions import send_sms
import sys 
import importlib

def take_action(action):
	print ('Taking action for ' + str(action))
	if action['type'] == 'sms':
		send_sms('', [])
	return None

def check_trigger(trigger):
    module_name = 'apis.' + trigger['api_id']
    function_name = trigger['trigger_id']
    parameter = trigger['parameter']
    f = getattr(sys.modules[module_name], function_name)
    return f(parameter)

def control_all_recipes(recipes):
    for recipe in recipes:
    	print('Controlling recipe with id ' + recipe['_id'])
        trigger = recipe['trigger']
        action = recipe['action']
        if check_trigger(trigger):
            print('Action is' + str(action))
            take_action(action)
