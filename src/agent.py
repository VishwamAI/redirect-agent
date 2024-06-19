import os
import subprocess
import webbrowser
import requests
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
import json

# Ensure consistent results from langdetect
DetectorFactory.seed = 0

class RedirectAgent:
    def __init__(self):
        self.command_history = []

    def parse_command(self, command):
        self.command_history.append(command)
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
        elif "learn" in command:
            self.learn_from_history()
        else:
            print("Command not recognized. Please try again.")

    def open_terminal(self):
        if os.name == "posix":
            subprocess.call(["gnome-terminal"])
        elif os.name == "nt":
            subprocess.call(["start", "cmd"], shell=True)
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
            output = subprocess.check_output(
                cmd, shell=True, stderr=subprocess.STDOUT
            )
            print(output.decode())
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {e.output.decode()}")

    def open_application(self, command):
        app_name = command.replace("open application ", "")
        if os.name == "posix":
            subprocess.call([app_name])
        elif os.name == "nt":
            subprocess.call(["start", app_name], shell=True)
        else:
            print("Unsupported OS for opening applications.")

    def fetch_data(self, command):
        url = self.extract_url(command)
        if url:
            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.text
                language = self.detect_language(data)
                print(
                    f"Fetched data in {language} language: "
                    f"{data[:200]}..."
                )  # Print first 200 characters
            except requests.RequestException as e:
                print(f"Failed to fetch data: {e}")
        else:
            print("No URL found in the command.")

    def detect_language(self, data):
        try:
            return detect(data)
        except LangDetectException:
            return "unknown"

    def learn_from_history(self):
        print("Learning from command history...")
        # Simple example: count command occurrences
        command_counts = {}
        for command in self.command_history:
            if command in command_counts:
                command_counts[command] += 1
            else:
                command_counts[command] = 1
        print("Command counts:", json.dumps(command_counts, indent=2))

if __name__ == "__main__":
    agent = RedirectAgent()
    while True:
        user_command = input("Enter your command: ")
        agent.parse_command(user_command)
