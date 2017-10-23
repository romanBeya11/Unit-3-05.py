'''
Created by: Roman Beya
Created on: 18-oct-2017
Created for: ICS3U
This program finds the factorial for any given number input by the user
'''
import ui

def calculate_factorial_touch_up_inside(sender):
	# calculates the factorial of a number inputted by a user
	counter = 1
	answer = 1
	user_input = int(view['integer_textfield'].text)
	while(counter <= user_input):
		if (counter <= user_input):
			answer = answer * counter
			counter = counter + 1
			view['output_label'].text = "{}".format(answer)
		
view = ui.load_view()
view.present('sheet')
