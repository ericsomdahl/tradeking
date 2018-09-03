import unittest

from fixml import FixMLRequests
from tradeking import TradeKingAPI


class TestTradeking(unittest.TestCase):
    template = FixMLRequests()

    def __init__(self, methodName='runTest'):
        super(TestTradeking, self).__init__(methodName)
        self.sut = TradeKingAPI()

    def test_getAccounts(self):
        actual = self.sut.accounts()

        self.assertEqual(actual.status_code, 200)
        self.assertIn('accountsummary', actual.json()['response']['accounts'])

    def test_placePreviewOrder(self):
        accounts = self.sut.accounts()

        # get account Ids we can use
        accountIds = [a['account'] for a in accounts.json()['response']['accounts']['accountsummary']]
        self.assertTrue(len(accountIds) > 0)

        # Market Buy 1 MSFT
        fixml = self.template.get_new_single_leg_order(account=accountIds[0], symbol="GOOG", quantity=1,
                                                       security_type=FixMLRequests.SECURITY_TYPE_COMMON_STOCK,
                                                       side=FixMLRequests.SIDE_BUY,
                                                       price_type=FixMLRequests.PRICE_TYPE_MARKET)

        actual = self.sut.accounts_id_orders_preview(accountIds[0], fixml=fixml)
        self.assertEqual(actual.status_code, 200)
