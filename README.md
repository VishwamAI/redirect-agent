# VishwamAI Redirect Agent

## Overview

The VishwamAI Redirect Agent is an advanced redirection agent designed to handle user requests for terminal operations, browsing, and redirecting to desktop-related applications. It features internet access, auto-learning capabilities, and multi-language support, similar to the capabilities of Jarvis.

## Features

- **Command Parsing**: The agent can parse user commands to perform various actions.
- **Terminal Operations**: Open a terminal window.
- **Browsing**: Open a browser with a specified URL.
- **Application Redirection**: Open specified desktop applications.
- **Data Fetching**: Fetch data from the internet and detect its language.
- **Multi-Language Support**: Detect and handle multiple languages, with enhanced exception handling and consistent results.

## Project Structure

```
VishwamAI/
├── data/               # Directory for datasets
├── models/             # Directory for storing trained models
├── scripts/            # Directory for scripts (e.g., training, preprocessing, model conversion, auto-update)
├── notebooks/          # Directory for Jupyter notebooks
├── logs/               # Directory for training logs and metrics
├── docs/               # Directory for documentation
├── config/             # Directory for configuration files
├── utils/              # Directory for utility scripts and functions
├── setup.sh            # Script for setting up the environment
├── requirements.txt    # File for specifying required dependencies
└── README.md           # Project overview and instructions
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/VishwamAI/redirect-agent.git
   cd redirect-agent
   ```

2. Set up the virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Usage

1. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. Run the agent:
   ```bash
   python src/agent.py
   ```

## Testing

Run the tests using `pytest`:
```bash
pytest -v
```

## CI/CD Pipeline

The project includes a CI/CD pipeline configured with GitHub Actions. The pipeline is triggered on updates to the `main` and `feature/*` branches and includes steps for checkout, Python setup, dependency installation, testing, and linting.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact the project maintainers.
