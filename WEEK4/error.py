def process_file():
    while True:
        
        input_filename = input("text.txt: ")
        
        try:
            
            with open(input_filename, 'r') as input_file:
                content = input_file.read()
                
            
            output_filename = input_filename.rsplit('.', 1)
            output_filename = f"{output_filename[0]}_modified.{output_filename[1]}"
            
           
            modified_content = content.upper()
            
          
            with open(output_filename, 'w') as output_file:
                output_file.write(modified_content)
                
            print(f"\nSuccess! Modified content has been written to {output_filename}")
            print(f"Original file: {input_filename}")
            print(f"Number of characters processed: {len(content)}")
            break
            
        except FileNotFoundError:
            print(f"\nError: The file '{input_filename}' was not found.")
            print("Please check the filename and try again.")
            
        except PermissionError:
            print(f"\nError: Permission denied to access '{input_filename}'.")
            print("Please check file permissions and try again.")
            
        except IOError as e:
            print(f"\nError: An I/O error occurred: {str(e)}")
            print("Please try again.")
            
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
            print("Please try again.")
        
        retry = input("\nWould you like to try again? (yes/no): ").lower()
        if retry != 'yes':
            print("Program terminated.")
            break

if __name__ == "__main__":
    print("File Processing Program")
    print("----------------------")
    print("This program will read a file and create a modified version.")
    process_file()