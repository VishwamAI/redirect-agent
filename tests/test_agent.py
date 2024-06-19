import pytest
from src.agent import RedirectAgent

@pytest.fixture
def agent():
    return RedirectAgent()

def test_parse_command_terminal(agent):
    assert agent.parse_command("open terminal") is None

def test_parse_command_browser(agent):
    assert agent.parse_command("browse https://www.example.com") is None

def test_parse_command_unrecognized(agent):
    assert agent.parse_command("unrecognized command") is None
