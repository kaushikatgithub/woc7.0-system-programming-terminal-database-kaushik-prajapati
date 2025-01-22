from DatabaseManager import Database

def main():

    db_manager = Database()

    print("Welcome to the Terminal Database by KP!")
    print("Type 'help' for a list of commands.")
    help_message = """
        Available commands:
        - create_db <db_name>: Create a new database
        - list_dbs: List all databases
        - open_db <db_name>: Switch to a specific database
        - create_table <table_name>: Create a new table in the current database
        - list_tables: List all tables in the current database
        - insert_data <table_name> <key> <value>: Insert data into a table
        - list_tuples <table_name>: List all entries in a table
        - exit: Exit the CLI
        - help: Show this help message      
    """

    while True:
        command = input("<terminal-db> ").strip().lower()

        if command == "exit":
            print("Exiting...")
            break

        elif command == "help":
            print(help_message)
        
        elif command.startswith("create_db "):
            cmd, db_name = command.split(maxsplit=1)
            db_manager.create_database(db_name=db_name)
        
        elif command == "list_dbs":
            db_manager.list_databases()
        
        elif command.startswith("open_db "):
            cmd, db_name = command.split(maxsplit=1)
            db_manager.open_database(db_name)

        elif command.startswith("create_table "):
            cmd, table_name = command.split(maxsplit=1)
            db_manager.create_table(table_name)

        elif command == "list_tables":
            db_manager.list_tables()

        elif command.startswith("insert_data "):
            parts = command.split(maxsplit=3)
            if len(parts) == 4:
                cmd, table_name, key, value = parts
                db_manager.insert_data(table_name, key, value)
            else:
                print("Usage: insert_data <table_name> <key> <value>")

        elif command.startswith("list_tuples "):
            cmd, table_name = command.split(maxsplit=1)
            db_manager.list_tuples(table_name)

        else:
            print("Unknown command. Type 'help' for a list of available commands.")
            
if __name__ == "__main__":
    main()