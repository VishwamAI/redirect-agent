import unittest
from src.agent import RedirectAgent

class TestRedirectAgent(unittest.TestCase):
    def setUp(self):
        self.agent = RedirectAgent()

    def test_parse_command_terminal(self):
        self.assertIsNone(self.agent.parse_command("open terminal"))

    def test_parse_command_browser(self):
        self.assertIsNone(self.agent.parse_command("browse https://www.example.com"))

    def test_parse_command_unrecognized(self):
        self.assertIsNone(self.agent.parse_command("unrecognized command"))

if __name__ == "__main__":
    unittest.main()
