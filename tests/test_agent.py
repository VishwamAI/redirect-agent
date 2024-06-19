import pytest
from unittest.mock import patch
from src.agent import RedirectAgent

@pytest.fixture
def agent():
    return RedirectAgent()

@patch('subprocess.call')
def test_parse_command_terminal(mock_subprocess, agent):
    assert agent.parse_command("open terminal") is None
    mock_subprocess.assert_called_with(['gnome-terminal'])

def test_parse_command_browser(agent):
    assert agent.parse_command("browse https://www.example.com") is None

def test_parse_command_unrecognized(agent):
    assert agent.parse_command("unrecognized command") is None
