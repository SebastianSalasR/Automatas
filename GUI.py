import PySimpleGUI as sg

class GUI:
	def __init__(self):
		# All the stuff inside your window.
		layout = [  [sg.Text("What's your name?")],
					[sg.InputText()],
					[sg.Button('Ok'), sg.Button('Cancel')] ]

		# Create the Window
		self.window = sg.Window('Hello Example', layout)

	def run(self):
		# Event Loop to process "events" and get the "values" of the inputs
		while True:
			event, values = self.window.read()

			# if user closes window or clicks cancel
			if event == sg.WIN_CLOSED or event == 'Cancel':
				break

			print('Hello', values[0], '!')

		self.window.close()
