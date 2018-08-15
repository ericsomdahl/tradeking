import unittest

from fixml import FixMLRequests


class TestFixMlRequests(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super(TestFixMlRequests, self).__init__(methodName)
        self.sut = FixMLRequests()

    def test_timeInForce_notPresentForMarketOrder(self):
        actual = self.sut.get_new_single_leg_order(account="123", time_in_force=self.sut.TIME_IN_FORCE_GTC,
                                                   price_type=self.sut.PRICE_TYPE_MARKET)
        self.assertNotRegexpMatches(actual, '.*TmInForce.*')

    def test_timeInForce_presentForOtherOrders(self):
        actual = self.sut.get_new_single_leg_order(account="123", time_in_force=self.sut.TIME_IN_FORCE_GTC,
                                                   price_type=self.sut.PRICE_TYPE_LIMIT)
        self.assertRegexpMatches(actual, '.*TmInForce.*')

        actual = self.sut.get_new_single_leg_order(account="123", time_in_force=self.sut.TIME_IN_FORCE_GTC,
                                                   price_type=self.sut.PRICE_TYPE_STOP)
        self.assertRegexpMatches(actual, '.*TmInForce.*')

        actual = self.sut.get_new_single_leg_order(account="123", time_in_force=self.sut.TIME_IN_FORCE_GTC,
                                                   price_type=self.sut.PRICE_TYPE_STOP_LIMIT)
        self.assertRegexpMatches(actual, '.*TmInForce.*')

        actual = self.sut.get_new_single_leg_order(account="123", time_in_force=self.sut.TIME_IN_FORCE_GTC,
                                                   price_type=self.sut.PRICE_TYPE_TRAILING_STOP)
        self.assertRegexpMatches(actual, '.*TmInForce.*')

    def test_account_valueIsRequired(self):
        self.assertRaisesRegexp(Exception, 'Account value is required', self.sut.get_new_single_leg_order)
