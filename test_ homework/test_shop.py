"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(5) is True
        assert product.check_quantity(1000) is True
        assert not product.check_quantity(1999)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(50)
        assert product.quantity == 950
        product.buy(860)
        assert product.quantity != 910

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)
        print('Ошибка. В наличии имеется только 1000 товаров')


@pytest.fixture
def cart():
    return Cart()


@pytest.fixture
def goods():
    return Product("chocolate", 99, "delicious", 500)



class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_products_to_cart(self, goods, cart):
        cart.add_product(goods, 10)
        assert 10 == cart.products.get(goods)
        print('Товары успешно добавлены в корзину')

    def test_clear_goods(self, cart, goods):
        cart.clear()
        print('Корзина очищена')

    def test_remove_goods(self, cart, goods):
        cart.add_product(goods, 10)
        cart.remove_product(goods, 5)
        assert 5 == cart.products.get(goods)
        cart.remove_product(goods, 1)
        assert 4 == cart.products.get(goods)


    def test_buy_goods(self, cart, goods):
        cart.add_product(goods, 10)
        cart.add_product = goods
        cart.buy()
        assert len(cart.products) == 0
        assert goods.quantity == 490

    def test_total_price(self, cart, goods):
        cart.add_product(goods, 60)
        assert cart.get_total_price() == 5940

    def test_bad_purchase(self, cart, goods):
        cart.add_product(goods, buy_count=1500)
        with pytest.raises(ValueError):
            assert cart.buy()
