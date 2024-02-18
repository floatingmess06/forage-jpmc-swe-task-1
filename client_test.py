import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {
                "top_ask": {"price": 121.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            stock, bid_price, ask_price, calculated_price = getDataPoint(quote)
            expected_price = (bid_price + ask_price) / 2
            self.assertEqual(
                calculated_price, expected_price, "Price calculation incorrect."
            )

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {
                "top_ask": {"price": 119.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            stock, bid_price, ask_price, calculated_price = getDataPoint(quote)
            expected_price = (bid_price + ask_price) / 2
            self.assertEqual(
                calculated_price, expected_price, "Price calculation incorrect."
            )

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_calculatePrice(self):
        prices = [
            {"price_a": 10, "price_b": 5, "expected_ratio": 2.0},
            {"price_a": 5, "price_b": 10, "expected_ratio": 0.5},
            {"price_a": 0, "price_b": 5, "expected_ratio": 0},
            {"price_a": 5, "price_b": 0, "expected_ratio": None},
            {"price_a": 0, "price_b": 0, "expected_ratio": None},
        ]
        """ ------------ Add the assertion below ------------ """
        for price_tuple in prices:
            calculated_ratio = getRatio(price_tuple["price_a"], price_tuple["price_b"])
            self.assertEqual(
                calculated_ratio,
                price_tuple["expected_ratio"],
                "Price calculation incorrect.",
            )


if __name__ == "__main__":
    unittest.main()
