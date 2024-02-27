# Read the decimal value from the file
import RPi.GPIO as GPIO
from time import sleep  # Import the sleep function

# Code with only 1 button as input for all the responses
# for e.g. if question 1 is being displayed then button press will increment count for response A and so on


GPIO.setmode(GPIO.BOARD)
count = 250

# safeguarding so if the button is pressed when result screen is displayed so extra element
response_value = [0, 0, 0, 0, 0]

"""
# Commenting to try single button response
# pin 29 for responseA, pin 31 for LED blink when the buttonA is pressed
 buttonLEDOutputA = 31
 buttonPinResponseA = 29

# pin 33 for responseB, pin 35 for LED blink when the buttonB is pressed
buttonPinResponseB = 33
buttonLEDOutputB = 35

# pin 16 for responseC, pin 31 for LED blink when the buttonC is pressed
buttonPinResponseC = 16
buttonLEDOutputC = 18

# pin 10 for responseD, pin 12 for LED blink when the buttonD is pressed
buttonPinResponseD = 10
buttonLEDOutputD = 12
"""

# pin 29 for response capture, pin 31 for LED
buttonPinResponse = 29
buttonLEDOutput = 31

# pin 38 for responseUp, pin 40 for ResponseDown
buttonPinUpResponse = 38
buttonPinDownResponse = 40


def check_value(value):
    if value > 4:
        return 0
    elif value < 0:
        return 4
    else:
        return value


"""
# Commenting to try single button response
GPIO.setup(buttonPinResponseA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonLEDOutputA, GPIO.OUT)

GPIO.setup(buttonPinResponseB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonLEDOutputB, GPIO.OUT)

GPIO.setup(buttonPinResponseC, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonLEDOutputC, GPIO.OUT)

GPIO.setup(buttonPinResponseD, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonLEDOutputD, GPIO.OUT)

GPIO.output(buttonLEDOutputA, False)
GPIO.output(buttonLEDOutputB, False)
GPIO.output(buttonLEDOutputC, False)
GPIO.output(buttonLEDOutputD, False)
"""

GPIO.setup(buttonPinResponse, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonLEDOutput, GPIO.OUT)

GPIO.setup(buttonPinUpResponse, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonPinDownResponse, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

with open('/home/snm/server/a.txt', 'r') as file:
    lines = file.readlines()
    # Read line 1 and extract the number as a decimal
    response_to_disp = int(lines[4].strip())  # Convert the string to a int
    # Read line 2 and extract the number as a decimal
    response_value[0] = int(lines[0].strip())  # Convert the string to a int
    # Read line 3 and extract the number as a decimal
    response_value[1] = int(lines[1].strip())  # Convert the string to a int
    # Read line 4 and extract the number as a decimal
    response_value[2] = int(lines[2].strip())  # Convert the string to a int
    # Read line 5 and extract the number as a decimal
    response_value[3] = int(lines[3].strip())  # Convert the string to a int

try:
    while 1:

        # to ensure the cores are not 100% used
        sleep(0.05)

        # code to collect response for if UP button is pressed
        buttonPressUp = GPIO.input(buttonPinUpResponse)
        if not buttonPressUp:
            print("Button pressed for UP")
            response_to_disp += 1
            response_to_disp = check_value(response_to_disp)
            print(response_to_disp)
            sleep(0.25)
            # Write the updated decimal value back to the file
            with open('/home/snm/server/a.txt', 'r') as file:
                # Read and store all lines
                lines = file.readlines()
                # Update the second number in line 1
                lines[4] = str(response_to_disp) + '\n'
            with open('/home/snm/server/a.txt', 'w') as file:
                file.writelines(lines)

        # code to collect response for if DOWN button is pressed
        buttonPressDown = GPIO.input(buttonPinDownResponse)
        if not buttonPressDown:
            print("Button pressed for Down")
            response_to_disp -= 1
            response_to_disp = check_value(response_to_disp)
            print("Moving to screen")
            print(response_to_disp)
            sleep(0.25)
            # Write the updated decimal value back to the file
            with open('/home/snm/server/a.txt', 'r') as file:
                # Read and store all lines
                lines = file.readlines()
                # Update the second number in line 1
                lines[4] = str(response_to_disp) + '\n'
            with open('/home/snm/server/a.txt', 'w') as file:
                file.writelines(lines)

        # code to collect response
        buttonPress = GPIO.input(buttonPinResponse)
        if not buttonPress and response_to_disp < 4:
            print("Button pressed")
            new_response = int(lines[response_to_disp]) + 1
            print("Screen")
            print(response_to_disp)
            print(new_response)
            # Write the updated decimal value back to the file
            with open('/home/snm/server/a.txt', 'r') as file:
                lines = file.readlines()
                lines[response_to_disp] = str(new_response) + '\n'
            with open('/home/snm/server/a.txt', 'w') as file:
                file.writelines(lines)
            GPIO.output(buttonLEDOutput, True)
            print("LED A ON")
            sleep(0.5)
            GPIO.output(buttonLEDOutput, False)
            print("LED A OFF")
            sleep(0.05)

        """        
        # code to collect response for question A
        buttonPressA = GPIO.input(buttonPinResponseA)
        if not buttonPressA:
            print("Button pressed for Question A")
            response_a_value += 1
            # Write the updated decimal value back to the file
            with open('/home/snm/server/a.txt', 'r') as file:
                lines = file.readlines()
                lines[1] = str(response_a_value) + '\n'
            with open('/home/snm/server/a.txt', 'w') as file:
                file.writelines(lines)
            GPIO.output(buttonLEDOutputA, True)
            print("LED A ON")
            # sleep(1)
            GPIO.output(buttonLEDOutputA, False)
            print("LED A OFF")
            sleep(0.05)

        # code to collect response for question B
        buttonPressB = GPIO.input(buttonPinResponseB)
        if not buttonPressB:
            print("Button pressed for Question B")
            response_b_value += 1
            # Write the updated decimal value back to the file
            with open('/home/snm/server/a.txt', 'r') as file:
                # Read and store all lines
                lines = file.readlines()
                # Update the second number in line 2
                lines[2] = str(response_b_value) + '\n'
            with open('/home/snm/server/a.txt', 'w') as file:
                file.writelines(lines)
            GPIO.output(buttonLEDOutputB, True)
            print("LED B ON")
            # sleep(1)
            GPIO.output(buttonLEDOutputB, False)
            print("LED B OFF")
            sleep(0.05)

        # code to collect response for question C
        buttonPressC = GPIO.input(buttonPinResponseC)
        if not buttonPressC:
            print("Button pressed for Question C")
            response_c_value += 1
            # Write the updated decimal value back to the file
            with open('/home/snm/server/a.txt', 'r') as file:
                # Read and store all lines
                lines = file.readlines()
                # Update the second number in line 2
                lines[3] = str(response_c_value) + '\n'
            with open('/home/snm/server/a.txt', 'w') as file:
                file.writelines(lines)
            GPIO.output(buttonLEDOutputC, True)
            print("LED C ON")
            # sleep(1)
            GPIO.output(buttonLEDOutputC, False)
            print("LED C OFF")
            sleep(0.05)

        # code to collect response for question D
        buttonPressD = GPIO.input(buttonPinResponseD)
        if not buttonPressD:
            print("Button pressed for Question D")
            response_d_value += 1
            # Write the updated decimal value back to the file
            with open('/home/snm/server/a.txt', 'r') as file:
                # Read and store all lines
                lines = file.readlines()
                # Update the second number in line 1
                lines[4] = str(response_d_value) + '\n'
            with open('/home/snm/server/a.txt', 'w') as file:
                file.writelines(lines)
            GPIO.output(buttonLEDOutputD, True)
            print("LED D ON")
            # sleep(1)
            GPIO.output(buttonLEDOutputD, False)
            print("LED D OFF")
            sleep(0.05)
            """



finally:
    GPIO.cleanup()
