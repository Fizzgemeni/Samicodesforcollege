def uppercase_file_contents(source_path, destination_path):
    """Reads a text file, converts all characters to uppercase, 
    and writes them to a destination file.
    """
    try:
        # Open and read the source file
        with open(source_path, 'r', encoding='utf-8') as source_file:
            content = source_file.read()
        
        # Convert all characters to uppercase
        uppercase_content = content.upper()
        
        # Write the converted content to the destination file
        with open(destination_path, 'w', encoding='utf-8') as dest_file:
            dest_file.write(uppercase_content)
            
        print(f"Success! Converted contents of '{source_path}' written to '{destination_path}'.")    
    except FileNotFoundError:
            print(f"Error: The file '{source_path}' could not be found.")
    except IOError as e:
            print(f"An I/O error occurred: {e}")
    
    # Example usage
    if __name__ == "__main__":
        input_file = "input.txt"   # Replace with your source file name
        output_file = "output.txt" # Replace with your desired output file name
        
        uppercase_file_contents(input_file, output_file)
