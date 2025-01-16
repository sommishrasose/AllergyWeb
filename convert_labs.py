import json

# Input file containing the raw lab data
input_file = "labs.txt"

# Output file for the formatted JSON data
output_file = "labs.json"

# Read the input data from the text file
with open(input_file, "r") as file:
    data = file.read()

# Process the lines, ensuring empty lines are skipped correctly
labs_raw = []
current_block = []

# Iterate through each line in the data
for line in data.split("\n"):
    line = line.strip()
    if line:  # If the line is not empty, add it to the current block
        current_block.append(line)
    elif current_block:  # If an empty line is encountered, save the block and reset
        labs_raw.append(current_block)
        current_block = []

# Add the last block if it exists
if current_block:
    labs_raw.append(current_block)

# Debug: Show the grouped lab blocks (optional for debugging)
print("Grouped lab blocks:")
print(labs_raw)
print("=" * 40)

# Helper function to extract city and state from address
def extract_city_state(address):
    parts = address.split(", ")
    if len(parts) >= 2:
        # Assume the second-to-last part is the city
        city = parts[-3].strip() if len(parts) >= 3 else parts[-2].strip()
        # Assume the last part is the state
        state = parts[-2].strip()
        # Validate state as part of India
        if state.lower() not in map(str.lower, indian_states):
            print(f"Invalid state detected: {state}")
            state = None  # Set state to None if invalid
        return city, state
    return None, None

# Define Indian states for validation
indian_states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
    "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
    "Uttarakhand", "West Bengal", "Delhi", "Jammu and Kashmir", "Ladakh"
]

# Extract and format lab data
labs = []
for index, lab_raw in enumerate(labs_raw, start=1):
    if len(lab_raw) < 3:
        print(f"Skipping entry {index} due to incomplete data: {lab_raw}")
        continue

    name = lab_raw[0]  # Lab name
    address = lab_raw[1]  # Lab address
    phone = lab_raw[2]  # Lab phone number

    # Attempt to extract city and state
    city, state = extract_city_state(address)

    # Append the formatted lab data
    labs.append({
        "id": index,
        "name": name,
        "address": address,
        "phone": phone,
        "city": city,
        "state": state
    })

# Save the formatted data to a JSON file
with open(output_file, "w") as json_file:
    json.dump(labs, json_file, indent=4)

# Print the result (optional)
print("Formatted labs data saved to:", output_file)
print(json.dumps(labs, indent=4))
