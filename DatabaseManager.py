import os
import json

class Database:

    def __init__(self, db_directory = 'Databases'):

        self.db_dir = db_directory # Default Database directory
        os.makedirs(self.db_dir, exist_ok=True)
        self.curr_db = None
    # End

    # Create new database 
    def create_database(self, db_name):

        # Path of the new db file
        db_path = os.path.join(self.db_dir, f"{db_name}.json")
        if os.path.exists(db_path):
            print(f"Database '{db_name}' already exists.")
        else:
            with open(db_path, 'w') as file:
                json.dump({}, file)
                print(f"Database '{db_name}' created successfully.")
    # End

    def delete_database(self, db_name):
        pass

    # List available db files
    def list_databases(self):

        databases = [file for file in os.listdir(self.db_dir) if file.endswith(".json")]
        if databases:
            print("Available Databases:")
            for db in databases:
                print(f"- {db}")
        else:
            print("No databases found.")
    # End

    # Open a particular db file
    def open_database(self, name_or_path):

        # Here 'name_or_path' can be just a file name in db_dir or a path to a other db file
        
        db_path = name_or_path # Assume to be an absolute path
        if not os.path.isabs(name_or_path):
            db_path = os.path.join(self.db_dir, f"{name_or_path}.json")
        
        if os.path.exists(db_path):
            self.curr_db = db_path
            print(f"Switched to database '{name_or_path}'.")
        else:
            print(f"Database '{name_or_path}' does not exist.")
    # End

    # Create a table in db file
    def create_table(self, table_name):

        if not self.curr_db:
            print("No database selected. Use 'open_db' to select one.")
            return

        with open(self.curr_db, 'r+') as file:
            
            data = json.load(file)
            if table_name not in data:
                data[table_name] = {}
                file.seek(0) 
                json.dump(data, file, indent=4)
                file.truncate() # Erase unnecessary data
                print(f"Table '{table_name}' created successfully.")
            else:
                print(f"Table '{table_name}' already exists.")
    # End

    def delete_table(self, table_name):
        pass

    # List available tables
    def list_tables(self):

        if not self.curr_db:
            print("No database selected. Use 'open_db' to select one.")
            return

        with open(self.curr_db, 'r+') as file:
            
            data = json.load(file)
            if data:
                print("Tables:")
                for table in data.keys():
                    print(f"- {table}")
            else:
                print("No tables in database.")
    # End

    # Insert data to a particular table
    def insert_data(self, table_name, key, value):

        if not self.curr_db:
            print("No database selected. Use 'open_db' to select one.")
            return
        
        with open(self.curr_db, 'r+') as file:
            
            data = json.load(file)
            if table_name in data:

                if key not in data[table_name]:
                    data[table_name][key] = value
                    file.seek(0)
                    json.dump(data, file, indent=4)
                    file.truncate()
                    print(f"Inserted key '{key}' with value '{value}' into table '{table_name}'.")
                else:
                    print(f"Key '{key}' already exists in table '{table_name}'.")
                     
            else:
                print(f"Table '{table_name}' does not exist.")
    # End

    def delete_data(self, table_name, key):
        pass

    # List all the tuples from a table
    def list_tuples(self, table_name):
        
        if not self.curr_db:
            print("No database selected. Use 'open_db' to select one.")
            return

        with open(self.curr_db, "r") as file:

            data = json.load(file)
            if table_name in data:
                print(f"Tuples in table '{table_name}':")
                for key, value in data[table_name].items():
                    print(f"{key}: {value}")
            else:
                print(f"Table '{table_name}' does not exist.")
    # Exit