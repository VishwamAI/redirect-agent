# Usage Instructions for Redirect Agent

## Overview
The Redirect Agent is designed to handle user requests related to terminal operations, browsing, and redirecting to desktop-related applications or more. The agent is enhanced with advanced features akin to Jarvis, including internet access, auto-learning capabilities, and multi-language support.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/VishwamAI/redirect-agent.git
   cd redirect-agent
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Running the Agent
To run the Redirect Agent, execute the following command:
```bash
python src/agent.py
```

## Available Commands
The Redirect Agent can handle the following commands:

### 1. Terminal Operations
- **Open Terminal**: Opens a terminal window on the user's operating system.
  ```plaintext
  open terminal
  ```

- **Execute Commands**: Executes shell commands provided by the user.
  ```plaintext
  execute <command>
  ```

### 2. Browsing
- **Open Browser**: Opens a web browser with a specified URL.
  ```plaintext
  browse <url>
  ```

### 3. Desktop Applications
- **Open Applications**: Opens desktop applications based on user requests (e.g., text editor, file explorer).
  ```plaintext
  open application <application_name>
  ```

### 4. Internet Access
- **Fetch Data**: Fetches data from the internet (e.g., weather information, news updates).
  ```plaintext
  fetch data
  ```

## Example Usage
1. To open a terminal window:
   ```plaintext
   open terminal
   ```

2. To browse a website:
   ```plaintext
   browse https://www.example.com
   ```

3. To execute a shell command:
   ```plaintext
   execute ls
   ```

4. To open a desktop application:
   ```plaintext
   open application gnome-calculator
   ```

5. To fetch data from the internet:
   ```plaintext
   fetch data
   ```

## Contributing
Please refer to the `CONTRIBUTING.md` file for guidelines on how to contribute to this project.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
