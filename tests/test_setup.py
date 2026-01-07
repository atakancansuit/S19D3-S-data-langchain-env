# pylint: disable-all

from nbresult import ChallengeResultTestCase

class TestSetup(ChallengeResultTestCase):
    def test_setup(self):
        self.assertTrue(self.result.all_good)
