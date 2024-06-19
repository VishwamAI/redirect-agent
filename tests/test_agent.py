import pytest
from unittest.mock import patch, Mock
from src.agent import RedirectAgent
import subprocess
from langdetect.lang_detect_exception import LangDetectException


@pytest.fixture
def agent():
    return RedirectAgent()


@patch("subprocess.call")
def test_parse_command_terminal(mock_subprocess, agent):
    assert agent.parse_command("open terminal") is None
    mock_subprocess.assert_called_with(["gnome-terminal"])


def test_parse_command_browser(agent):
    assert agent.parse_command("browse https://www.google.com") is None


def test_parse_command_unrecognized(agent):
    assert agent.parse_command("unrecognized command") is None


@patch("subprocess.check_output")
def test_execute_command(mock_check_output, agent):
    mock_check_output.return_value = b"command output"
    assert agent.parse_command("execute ls") is None
    mock_check_output.assert_called_with(
        "ls", shell=True, stderr=subprocess.STDOUT
    )


@patch("subprocess.call")
def test_open_application(mock_subprocess, agent):
    assert agent.parse_command("open application gnome-calculator") is None
    mock_subprocess.assert_called_with(["gnome-calculator"])


@patch("requests.get")
@patch.object(RedirectAgent, "detect_language")
def test_fetch_data(mock_detect_language, mock_get, agent):
    mock_response = Mock()
    mock_response.text = "This is a test response."
    mock_get.return_value = mock_response
    mock_detect_language.return_value = "en"

    assert agent.parse_command("fetch data https://www.example.com") is None

    mock_get.assert_called_with("https://www.example.com")
    mock_detect_language.assert_called_with("This is a test response.")


def test_detect_language(agent):
    assert agent.detect_language("This is a test.") == "en"


def test_detect_language_exception(agent):
    with patch("src.agent.detect",
               side_effect=LangDetectException("error_code", "error_message")):
        assert agent.detect_language("This is a test.") == "unknown"


@patch("subprocess.call")
def test_learn_from_history(mock_subprocess, agent):
    mock_subprocess.return_value = None
    agent.parse_command("open terminal")
    agent.parse_command("browse https://www.google.com")
    agent.parse_command("open terminal")
    agent.parse_command("learn")
    assert agent.command_history == [
        "open terminal",
        "browse https://www.google.com",
        "open terminal",
        "learn",
    ]


def test_parse_html(agent):
    html_content = (
        "<html><head><title>Test</title></head><body><p>Hello, world!</p></body></html>"
    )
    parsed_html = agent.parse_html(html_content)
    assert parsed_html == "Title: Test\nBody: Hello, world!"
