import os
import subprocess
import webbrowser

class RedirectAgent:
    def __init__(self):
        pass

    def parse_command(self, command):
        if "open terminal" in command:
            self.open_terminal()
        elif "browse" in command:
            self.open_browser(command)
        elif "execute" in command:
            self.execute_command(command)
        elif "open application" in command:
            self.open_application(command)
        elif "fetch data" in command:
            self.fetch_data(command)
        else:
            print("Command not recognized. Please try again.")

    def open_terminal(self):
        if os.name == 'posix':
            subprocess.call(['gnome-terminal'])
        elif os.name == 'nt':
            subprocess.call(['start', 'cmd'], shell=True)
        else:
            print("Unsupported OS for terminal operations.")

    def open_browser(self, command):
        url = self.extract_url(command)
        if url:
            webbrowser.open(url)
        else:
            print("No URL found in the command.")

    def extract_url(self, command):
        words = command.split()
        for word in words:
            if word.startswith("http://") or word.startswith("https://"):
                return word
        return None

    def execute_command(self, command):
        cmd = command.replace("execute ", "")
        try:
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
            print(output.decode())
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {e.output.decode()}")

    def open_application(self, command):
        app_name = command.replace("open application ", "")
        if os.name == 'posix':
            subprocess.call([app_name])
        elif os.name == 'nt':
            subprocess.call(['start', app_name], shell=True)
        else:
            print("Unsupported OS for opening applications.")

    def fetch_data(self, command):
        # Placeholder for fetching data from the internet
        print("Fetching data...")

if __name__ == "__main__":
    agent = RedirectAgent()
    while True:
        user_command = input("Enter your command: ")
        agent.parse_command(user_command)
