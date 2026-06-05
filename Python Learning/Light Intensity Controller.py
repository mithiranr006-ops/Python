# Basic Light Intensity Controller
# This code turns on a light when it gets dark

# Set the threshold for when to turn on the light
light_threshold = 300

# Simulate reading light intensity (in real code, this would come from a sensor)
def read_light_intensity():
    # This is just a sample value - in real life, you'd read from a sensor
    light_intensity = 250  # Try changing this to 350 to see different behavior
    return light_intensity

# Function to turn on the light
def turn_on_light():
    print("Light is ON")

# Function to turn off the light
def turn_off_light():
    print("Light is OFF")

# Main code
light_intensity = read_light_intensity()

print(f"Current light intensity: {light_intensity}")

if light_intensity < light_threshold:
    # It's dark, turn on the light
    turn_on_light()
else:
    # It's bright enough, keep light off
    turn_off_light()