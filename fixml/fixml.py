from jinja2 import Environment, PackageLoader, select_autoescape


class FixMLRequests(object):

    def __init__(self):
        super(FixMLRequests, self).__init__()

        self.env = Environment(
            loader=PackageLoader('fixml', 'templates'),
            autoescape=select_autoescape(['xml'])
        )

    def get_buy_order(self, symbol=None, quantity=0, security_type=None, side=0, time_in_force=0):
        """"""
        template = self.env.get_template('single-leg-new-order.xml')
        return template.render(symbol=symbol, quantity=quantity, security_type=security_type, order_side=side)
