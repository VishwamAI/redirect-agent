import pytest
from unittest.mock import patch
from src.agent import RedirectAgent
import subprocess


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


@patch('subprocess.check_output')
def test_execute_command(mock_check_output, agent):
    mock_check_output.return_value = b'command output'
    assert agent.parse_command("execute ls") is None
    mock_check_output.assert_called_with('ls', shell=True, stderr=subprocess.STDOUT)


@patch('subprocess.call')
def test_open_application(mock_subprocess, agent):
    assert agent.parse_command("open application gnome-calculator") is None
    mock_subprocess.assert_called_with(['gnome-calculator'])


def test_fetch_data(agent):
    assert agent.parse_command("fetch data") is None
