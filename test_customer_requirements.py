from testd4.customer import Customer

#Requirement 7.3 - Saving dietary choices
def test_add_dietary_restrictions():
    dietary_restrictions = ["Halal", "Kosher"]
    customer_id = 12
    for item in dietary_restrictions:
        cus = Customer()
        assert cus.add_dietary_restrictions(item, customer_id) == True, "Dietary restriciton not saved!"
#Requirement 7.3 - Saving dietary choices
def test_add_dietary_preferences():
    dietary_preferences = ["Paleo", "Keto", "Vegan"]
    customer_id = 14
    for item in dietary_preferences:
        cus = Customer()
        assert cus.add_dietary_preferences(item, customer_id) == True, "Dietary preferences not saved!"
#Requirement 7.3 - Saving dietary choices
def test_number_of_dietary_restrictions():
    customer_id = 12
    cus = Customer()
    cus.get_number_of_dietary_restrictions(customer_id) <= 1, "Dietary restriction is more than one!"
#Requirement 7.3 - Saving dietary choices
def test_number_of_dietary_rpreferences():
    customer_id = 14
    cus = Customer()
    cus.get_number_of_dietary_preferences(customer_id) <= 1, "Dietary preference is more than one!"

#Requirement #7.4.1

def test_custom_menu():
    customer_id =  12
    fake_menu_items = ["Frog Legs", "Shark Skin", "Chicken"]
    cus = Customer()
    dietary_restriction = ["Kosher"]
    dietary_preference = ["Paleo"]
    assert cus.generate_custom_menu(dietary_restriction, dietary_preference, customer_id, fake_menu_items) == "Menu generated successfully!", "Unable to generate custom user menu!"

#Requirement 7.5 - Deals of the day for the user
def test_check_eligibility_for_deal_of_day():
    customer_id = 14
    number_of_orders_placed = 19
    cus = Customer()
    assert cus.check_eligibility_for_deal_of_day(customer_id, number_of_orders_placed) == True, "Customer is not eligible for deal of the day!"

def test_view_deals_of_the_day():
    customer_id = 12
    expected_deals_of_the_day = ["Chicken Sandwich", "Grilled Salmon"]
    cus = Customer()
    assert cus.view_deals_of_the_day(customer_id) == expected_deals_of_the_day, "Deals of the day not found for the customer!"

#Requirement 7.7 - Order and cart features 
def test_save_order_history():
    expected_response = "Order history saved successfully!"
    menu_items = ["Coke", "Deep Fried Oreos"]
    order_date = "10/10/20"
    customer_id = 14
    cus = Customer()
    assert cus.save_order_history(customer_id, menu_items, order_date) == expected_response ,"Customer is not able to save the order history!"
#Requirement 7.7.1 - View user history and repeat order
def test_view_order_history():
    expected_response = "You ordered Coke and Deep Fried Oreos on 10/10/20"
    order_date = "10/10/20"
    customer_id = 14
    cus = Customer()
    assert cus.view_order_history(customer_id, order_date) == expected_response ,"Customer is not able to view the order history!"

#Requirement 7.7.1 - View user history and repeat order
def test_check_repeat_order_button_text():
    expected_resposne = "Repeat last order"
    customer_id =  12
    cus = Customer()
    assert cus.check_repeat_order_button_text(customer_id) == expected_resposne, "Repeat order history button does not have the correct text!"


#Requirement 7.7.2 - Users with registered accounts can save their favorite foods and meals.
def test_add_item_to_favorites_success():
    expected_response = "Item added to your favorites successfully"
    customer_id = 14
    menu_item = "Kiwi Juice"
    cus = Customer()
    assert cus.add_item_to_favorites(customer_id, menu_item) == expected_response, "Unable to add menu item to customer's favorites!"

#Requirement 7.7.2 - Users with registered accounts can save their favorite foods and meals.
def test_add_item_to_favorites_failure():
    expected_response = "Item already exists in your favorites"
    customer_id = 14
    menu_item = "Kiwi Juice"
    cus = Customer()
    assert cus.add_item_to_favorites(customer_id, menu_item) == expected_response, "Unable to check if menu item is in the customer's favorites!"

