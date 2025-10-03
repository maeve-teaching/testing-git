# Contents of /git-collaboration-template/git-collaboration-template/src/main.py

def greet(name):
    return f"Hello, {name}!"

def process_data(data):
    return data.upper()

def main():
    # Read sample data from file
    with open('src/data/sample_data.txt', 'r') as file:
        data = file.read()
    
    # Process the data
    processed_data = process_data(data)
    
    # Greet the user
    user_name = "Student"
    greeting = greet(user_name)
    
    # Print the results
    print(greeting)
    print("Processed Data:")
    print(processed_data)

if __name__ == "__main__":
    main()