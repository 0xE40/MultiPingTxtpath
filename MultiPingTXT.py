import os
import socket


def ping_website(host):
    """Attempt to ping a website."""
    try:
        # Check if the host resolves to an IP address to simulate ping
        socket.gethostbyname(host)
        return True
    except socket.error:
        return False


def read_websites(file_path):
    """Read website URLs from a text file."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []


def save_successful_pings(output_file, successful_websites):
    """Save successfully pinged website URLs to a text file."""
    with open(output_file, 'w') as file:
        for website in successful_websites:
            file.write(f"{website}\n")


def main():
    """Main program function."""
    input_file = input("Enter the path to the text file containing website URLs: ").strip()

    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return

    script_dir = os.path.dirname(input_file)
    output_file = os.path.join(script_dir, 'successful_pings.txt')

    websites = read_websites(input_file)
    if not websites:
        print("No websites to ping. Please check the input file.")
        return

    successful_websites = []

    for website in websites:
        print(f"Pinging: {website}")
        if ping_website(website):
            print(f"Success: {website}")
            successful_websites.append(website)
        else:
            print(f"Failed: {website}")

    save_successful_pings(output_file, successful_websites)
    print(f"Successful pings saved to: {output_file}")

if __name__ == "__main__":
    main()