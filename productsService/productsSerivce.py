import json

class ProductsService:
    def __init__(self):
        pass

    def readJson(self, filename, data, popError, popNoExist, popValueError):
        try:
            # Reading data from JSON file
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            if data is None:
                popError
                print(f"File {filename} not found.")
                return None
            else:
                popNoExist
                print(f"New file created and data written to {filename}")
        except json.JSONDecodeError:
            popValueError
            print(f"Error reading JSON data from {filename}. It may be corrupted.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")


    def writeJson(filename, data, popMethod, popValueError):
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            popMethod
            print(f"Data successfully written to {filename}")
        except Exception as e:
            popValueError
            print(f"An error occurred while writing to {filename}: {e}")


    def update_json(filename, update, popMethod, popValueError):
        try:
            # Read existing data from JSON file
            with open(filename, 'r') as file:
                data = json.load(file)

            # Apply the update function to the data
            updated_data = update(data)

            # Write the updated data back to the JSON file
            with open(filename, 'w') as file:
                json.dump(updated_data, file, indent=4)
            popMethod
            print(f"Data successfully updated in {filename}")
        
        except FileNotFoundError:
            popValueError
            print(f"Error: The file '{filename}' does not exist.")
        except json.JSONDecodeError:
            popValueError
            print(f"Error: The file '{filename}' is not valid JSON or is corrupted.")
        except Exception as e:
            popValueError
            print(f"An error occurred while updating the file: {e}")