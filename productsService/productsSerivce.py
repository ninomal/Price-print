import json
import os

class ProductsService:
    def __init__(self):
        pass


    def readJson(self, filename):
        try:
            # Reading data from JSON file
            with open(filename, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Error reading JSON data from {filename}. It may be corrupted.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")

    def writeJson(self, filename, data):
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Data successfully written to {filename}")
        except Exception as e:
            print(f"An error occurred while writing to {filename}: {e}")

    def updateJson(self, filename, update):
        try:
            # Read existing data from JSON file
            with open(filename, 'r') as file:
                data = json.load(file)

            # Apply the update function to the data
            updated_data = update(data)

            # Write the updated data back to the JSON file
            with open(filename, 'w') as file:
                json.dump(updated_data, file, indent=4)
            print(f"Data successfully updated in {filename}")
        
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist.")
        except json.JSONDecodeError:
            print(f"Error: The file '{filename}' is not valid JSON or is corrupted.")
        except Exception as e:
            print(f"An error occurred while updating the file: {e}")

    def checkFileExist(file_path):
        # Check if the file exists
        if os.path.exists(file_path):
            # If the file exists, return a JSON response (True or some info)
            return json.dumps({"file_exists": True, "message": "File exists."})
        else:
            # If the file does not exist, return a JSON response (False)
            return json.dumps({"file_exists": False, "message": "File does not exist."})