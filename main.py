import sys
from command import CommandProcessor

DEFAULT_FILENAME = 'input/Input1.txt'

def read_commands_from_file(filename):
    """Read input from text file and return into  a list of strings."""
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main(filename=DEFAULT_FILENAME):
    processor = CommandProcessor()
    output = []

    commands = read_commands_from_file(filename)
    if not commands:
        print("input not found in the file.")
        return

    for command in commands:
        command = command.strip()
        if command:
            result = processor.process(command)
            if result:
                output.append(result)

    if output:
        print("Simulation Output:")
        for line in output:
            print(line)
    else:
        print("No REPORT input found or no valid output generated.")

if __name__ == "__main__":
    filename = DEFAULT_FILENAME if len(sys.argv) == 1 else sys.argv[1]
    main(filename)
