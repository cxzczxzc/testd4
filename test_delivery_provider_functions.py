from testd4.deliveryprovider import DeliveryProvider

#Requirement 7.2.4
def test_currently_configured_delivery_provider():
    invalid_delivery_providers = ["SkipTheDishes", "Foodora", "Instacart"]
    for dp_name in invalid_delivery_providers:
        dp = DeliveryProvider()
        assert dp.get_delivery_provider(dp_name) == True, "Invalid delivery provider configured!"

def test_deliver_with_uber_eats_button():
    button_text = "Order with UberEats"
    dp = DeliveryProvider()
    assert dp.generate_button_for_delivery == button_text, "Invalid button text specified!"

def test_set_delivery_provider():
    delivery_providers = ["UberEats", "SkipTheDishes", "Foodora"]
    for dp_name in delivery_providers:
        dp = DeliveryProvider()
        assert dp.set_deliver_provider(dp_name) == dp_name, "Delivery provider is not selected as specified!"


def test_track_order():
    valid_order_status_messsages =  ["Order received", "Order accepted", "Order being delivered"]
    fake_order_id = 10
    for message in valid_order_status_messsages:
        dp = DeliveryProvider()
        assert dp.track_order(fake_order_id) == message, "Unable to track the order!"

def test_cancel_order():
    valid_order_status_messsages =  ["Order cancelled", "Unable to cancel order"]
    fake_order_id = 10
    for message in valid_order_status_messsages:
        dp = DeliveryProvider()
        assert dp.cancel_order(fake_order_id) == message, "No confirmation of cancellation received!"

def test_add_cart_items_to_delivery_provider():
    cart_items = ["Octopus", "Lobster"]
    dp = DeliveryProvider()
    assert dp.add_cart_items_to_delivery_provider(cart_items) == True, "Unable to add cart items to the delivery provider!"
