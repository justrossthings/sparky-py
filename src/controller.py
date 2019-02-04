from serial import Serial

port = Serial('/dev/ttyACM0')

control_key = {
    'up': 'f',
    'down': 'b',
    'left': 'l',
    'right': 'r',
    'stop': 's'
}

def execute_control(control):
    if control in control_key.keys():
        command = control_key[control]
        port.write(command)
    else:
        print('Command not recognized')