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


if __name__ == "__main__":
    agent = RedirectAgent()
    while True:
        user_command = input("Enter your command: ")
        agent.parse_command(user_command)
