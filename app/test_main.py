import datetime
import pytest
from unittest.mock import patch
from app.main import outdated_products


class TestProductsDate:
    @pytest.mark.parametrize(
        "products, expected",
        [
            pytest.param(
                [
                    {
                        "name": "salmon",
                        "expiration_date": datetime.date(2022, 2, 10),
                        "price": 600
                    },
                    {
                        "name": "chicken",
                        "expiration_date": datetime.date(2022, 2, 5),
                        "price": 120
                    },
                    {
                        "name": "duck",
                        "expiration_date": datetime.date(2022, 2, 1),
                        "price": 160
                    },
                ],
                ["salmon", "chicken", "duck"],
                id="Single outdated product"
            ),
            pytest.param(
                [
                    {
                        "name": "milk",
                        "expiration_date": datetime.date(2022, 2, 5),
                        "price": 30
                    },
                    {
                        "name": "bread",
                        "expiration_date": datetime.date(2022, 2, 2),
                        "price": 20
                    },
                ],
                ["milk", "bread"],
                id="Multiple products, some outdated"
            ),
            pytest.param(
                [
                    {
                        "name": "egg",
                        "expiration_date": datetime.date(2024, 8, 8),
                        "price": 10
                    },
                    {
                        "name": "cheese",
                        "expiration_date": datetime.date(2024, 8, 8),
                        "price": 50
                    },
                ],
                [],
                id="No outdated products"
            ),
            pytest.param(
                [
                    {
                        "name": "apple",
                        "expiration_date": datetime.date(2022, 8, 8),
                        "price": 15
                    },
                    {
                        "name": "banana",
                        "expiration_date": datetime.date(2022, 8, 7),
                        "price": 10
                    },
                    {
                        "name": "orange",
                        "expiration_date": datetime.date(2022, 8, 9),
                        "price": 12
                    },
                ],
                ["banana"],
                id="Products with varying expiration dates"
            ),
        ]
    )
    @patch("app.main.datetime")
    def test_outdated_products(self,
                               mock_datetime,
                               products: list,
                               expected: list) -> None:
        mock_datetime.date.today.return_value = datetime.date(2022, 8, 8)
        result = outdated_products(products)
        assert result == expected
