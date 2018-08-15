from jinja2 import Environment, PackageLoader, select_autoescape


class FixMLRequests(object):
    TIME_IN_FORCE_DAY = 0
    TIME_IN_FORCE_GTC = 1
    TIME_IN_FORCE_MARKET_ON_CLOSE = 7

    PRICE_TYPE_MARKET = 1
    PRICE_TYPE_LIMIT = 2
    PRICE_TYPE_STOP = 3
    PRICE_TYPE_STOP_LIMIT = 4
    PRICE_TYPE_TRAILING_STOP = "P"

    SIDE_BUY = 1
    SIDE_SELL = 2
    SIDE_SELL_SHORT = 5
    SIDE_BUY_TO_COVER = 1

    SECURITY_TYPE_COMMON_STOCK = "CS"
    SECURITY_TYPE_OPTION = "OPT"

    def __init__(self):
        super(FixMLRequests, self).__init__()

        self.env = Environment(
            loader=PackageLoader('fixml', 'templates'),
            autoescape=select_autoescape(['xml'])
        )

    def get_new_single_leg_order(self, account=None, symbol=None, quantity=0, security_type=None, side=0,
                                 time_in_force=0,
                                 price_type=PRICE_TYPE_MARKET):
        if account is None:
            raise Exception('Account value is required')

        template = self.env.get_template('single-leg-new-order.xml')
        return template.render(account=account, symbol=symbol, quantity=quantity, security_type=security_type,
                               order_side=side, time_in_force=time_in_force, price_type=price_type)
