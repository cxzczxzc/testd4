from testd4.registeration import Registration
from testd4.menuitem import MenuItem
from testd4.specialdeals import SpecialDeals
from testd4.restaurantstaff import RestaurantStaff
from testd4.orders import Orders
from testd4.customer import Customer
from testd4.deliveryprovider import DeliveryProvider

#The tests on Registration are performed using make believe scenarios of working with HTTP requests

#Requirement #5.1.1 - Account creation requirements 
def test_password_complexity():
    invalid_passwords = ["invalid", "password", "bad", "evil", "good", "lukewarm"]

    for password in invalid_passwords:
        reg = Registration()
        assert reg.verify_password_complexity(password) == True , "Invalid password supplied"

#Requirement #5.1.1 - Account creation requirements 
def test_email_validity():
    invalid_emails = ["not", "a", "valid", "email"]  

    for email in invalid_emails:
        reg = Registration()
        assert reg.verify_email(email) == True , "Invalid password supplied"

#Requirement #5.1.1 - Account creation requirements 
def test_phonenumber_validity():
    invalid_phone_numbers = ["asdsa", "121", "00000"]

    for phonenumber in invalid_phone_numbers:
        reg = Registration()
        assert reg.verify_phone_number(phonenumber) == True , "Invalid phone number supplied"
#Requirement 5.1.2 and 5.1.2.1
def test_oauth_auth_code_flow():
    invalid_http_responses = ["error", "invalid_credentials"]

    for response in invalid_http_responses:
        reg = Registration()
        assert reg.verify_oauth_authorization_code_flow(response) == True, "Invalid HTTP response received"

#Requirement 5.1.2.1
def test_redirect_after_login():
    invalid_redirect_uri = ["google.com", "donaldjtrump.com"]

    for response in invalid_redirect_uri:
        reg = Registration()
        assert reg.verify_oauth_authorization_code_flow(response) == "https://www.dinnerisserverdanddelivered.com", "Invalid redirect detected"
#Requirement 5.1.2.3
def test_oauth_token_received():
    invalid_http_responses = ["invalid_user", "access_denied"]

    for response in invalid_http_responses:
        reg = Registration()
        assert reg.verify_oauth_token_received(response) == True, "Invalid HTTP response received"

#Requirement 5.2.1 - Account Login
def test_login_credentials():
    invalid_credentials = {"invalid_username","invalid_password"}
    reg = Registration()
    assert reg.check_credentials(invalid_credentials) == True, "Invalid credentials, login not successful!"

#Requirement 5.2.1.1
def test_successful_login():
    reg = Registration()
    user = None 
    assert reg.successful_login(user) == True, "login not successful"

#Requirement 5.2.1.2 - can't test send password reset email functionality
def test_relogin_attempts():
    count = 6
    reg = Registration()
    assert reg.lock_account_after_5_login_attempts(count) == True, "Account not locked out after more than 5 attempts"

#Requirement 5.2.1.2 - can't test send password reset email functionality
def test_account_locked_error_message():
    invalid_errors = ["Your account is locked", "Thou art banished from thine account"]
    for message in invalid_errors:
        reg = Registration()
        assert reg.display_locked_account_error_message(message) == True, "Account lockout error message not correct!"

#Requirement 5.2.2 - Forgotten Password
def test_forgotten_password_button():
    button = None #UI element needed here, which isn't possible 
    reg = Registration()
    assert reg.check_forgotten_password_button(button) == True, "Forgotten password button not available!"

#Requirement 5.2.3 - Reset Forgotten Password
def test_valid_email_and_phone_for_password_reset_request():
    invalid_phone_numbers = ["lalalala", "hahahaha", "blablablablabla"]
    invalid_emails = ["a@b.com" ,"d@e.com", "x@y.com"]
    for x in range(len(invalid_emails)):
        reg = Registration()
        assert reg.check_email_and_phonenumber(invalid_emails[x], invalid_phone_numbers[x]) == True, "Invalid information supplied for password reset request!"
#Requirement 5.2.3 - Reset Forgotten Password
def test_reset_password_link():
    user = None
    reg = Registration()
    assert reg.generate_password_reset_link(user) == True, "Password reset link not generated!"
#Requirement 5.2.4 - Link accounts with UberEats and other delivery providers
def test_currently_configured_delivery_provider():
    invalid_delivery_providers = ["SkipTheDishes", "Foodora", "Instacart"]
    for dp_name in invalid_delivery_providers:
        dp = DeliveryProvider()
        assert dp.get_delivery_provider(dp_name) == True, "Invalid delivery provider configured!"


#Requirement 5.2.4 - Link accounts with UberEats and other delivery providers
def test_deliver_with_uber_eats_button():
    expected_button_text = "Order with UberEats"
    dp = DeliveryProvider()
    assert dp.generate_button_for_delivery == expected_button_text, "Invalid button text specified!"

#Requirement 5.2.4 - Link accounts with UberEats and other delivery providers
def test_set_delivery_provider():
    delivery_providers = ["UberEats", "SkipTheDishes", "Foodora"]
    for dp_name in delivery_providers:
        dp = DeliveryProvider()
        assert dp.set_deliver_provider(dp_name) == dp_name, "Delivery provider is not selected as specified!"


#Requirement 5.2.4 - Link accounts with UberEats and other delivery providers
def test_track_order():
    valid_order_status_messsages =  ["Order received", "Order accepted", "Order being delivered"]
    fake_order_id = 10
    for message in valid_order_status_messsages:
        dp = DeliveryProvider()
        assert dp.track_order(fake_order_id) == message, "Unable to track the order!"

#Requirement 5.2.4 - Link accounts with UberEats and other delivery providers
def test_cancel_order():
    valid_order_status_messsages =  ["Order cancelled", "Unable to cancel order"]
    fake_order_id = 10
    for message in valid_order_status_messsages:
        dp = DeliveryProvider()
        assert dp.cancel_order(fake_order_id) == message, "No confirmation of cancellation received!"

#Requirement 5.2.4 - Link accounts with UberEats and other delivery providers
def test_add_cart_items_to_delivery_provider():
    cart_items = ["Octopus", "Lobster"]
    dp = DeliveryProvider()
    assert dp.add_cart_items_to_delivery_provider(cart_items) == True, "Unable to add cart items to the delivery provider!"

#Requirement 5.3 - Saving dietary choices
def test_add_dietary_restrictions():
    dietary_restrictions = ["Halal", "Kosher"]
    cus = Customer(customer_id=12, dietary_restrictions=dietary_restrictions)
    assert cus.add_dietary_restrictions(cus.dietary_restrictions,cus.customer_id) == True, "Dietary restriciton not saved!"
#Requirement 5.3 - Saving dietary choices
def test_add_dietary_preferences():
    dietary_preferences = ["Paleo", "Keto", "Vegan"]
    customer_id = 14
    cus = Customer(customer_id=customer_id, dietary_preferences=dietary_preferences)
    assert cus.add_dietary_preferences(cus.dietary_preferences, cus.customer_id) == True, "Dietary preferences not saved!"
#Requirement 5.3 - Saving dietary choices
def test_number_of_dietary_restrictions():
    customer_id = 12
    cus = Customer(customer_id=customer_id)
    cus.get_number_of_dietary_restrictions(cus.customer_id) <= 1, "Dietary restriction is more than one!"
#Requirement 5.3 - Saving dietary choices
def test_number_of_dietary_rpreferences():
    customer_id = 14
    cus = Customer(customer_id=customer_id)
    cus.get_number_of_dietary_preferences(cus.customer_id) <= 1, "Dietary preference is more than one!"

#Requirement #5.4.1 Generate Customized User Menu

def test_custom_menu():
    customer_id =  12
    fake_menu_items = ["Frog Legs", "Shark Skin", "Chicken"]
    dietary_restriction = ["Kosher"]
    dietary_preference = ["Paleo"]
    cus = Customer(customer_id=customer_id, dietary_preferences=dietary_preference, dietary_restrictions=dietary_restriction)
    assert cus.generate_custom_menu(cus.dietary_restrictions, cus.dietary_preferences, cus.customer_id, fake_menu_items) == "Menu generated successfully!", "Unable to generate custom user menu!"

#Requirement 5.5 - Deals of the day for the user
def test_check_eligibility_for_deal_of_day():
    customer_id = 14
    cus = Customer(customer_id=customer_id)
    number_of_orders_placed = 19
    assert cus.check_eligibility_for_deal_of_day(cus.customer_id, number_of_orders_placed) == True, "Customer is not eligible for deal of the day!"

#Requirement 5.5 - Deals of the day for the user
def test_view_deals_of_the_day():
    customer_id = 12
    expected_deals_of_the_day = ["Chicken Sandwich", "Grilled Salmon"]
    cus = Customer(customer_id=customer_id)
    assert cus.view_deals_of_the_day(cus.customer_id) == expected_deals_of_the_day, "Deals of the day not found for the customer!"

#Requirement 5.6 - Add deals of the day functionality for the restaurant owner
def test_view_most_popular_menu_items():
    expected_popular_items = ["Chips", "Coke", "Pot Brownies"]
    rs = RestaurantStaff()
    assert rs.view_most_popular_menu_items() == expected_popular_items, "Restaurant owner unable to view the most popular menu items!"

#Requirement 5.6 - Add deals of the day functionality for the restaurant owner
def test_create_deal_of_the_day_for_all_customers():
    expected_deal_of_the_day = "Pot Brownies"
    expected_discounted_price = "@$10 per kilo"
    rs = RestaurantStaff()
    assert rs.create_deal_of_the_for_all_customers(expected_deal_of_the_day, expected_discounted_price) == expected_deal_of_the_day, "Restaurant staff unable to create deal of the day!"

#Requirement 5.6 - Add deals of the day functionality for the restaurant owner
def test_deal_of_the_day_validity():
    deal = SpecialDeals(special_deal_id="007")
    created_date = "10/10/20"
    rs = RestaurantStaff()
    assert rs.check_deal_of_the_day_validity(deal.special_deal_id, created_date) == True, "The deal is no longer valid!"
#Requirement 5.7 - Order and cart features 
def test_save_order_history():
    expected_response = "Order history saved successfully!"
    menu_items = ["Coke", "Deep Fried Oreos"]
    order_date = "10/10/20"
    customer_id = 14
    cus = Customer(customer_id=customer_id)
    assert cus.save_order_history(cus.customer_id, menu_items, order_date) == expected_response ,"Customer is not able to save the order history!"
#Requirement 5.5.1 - View user history and repeat order
def test_view_order_history():
    expected_response = "You ordered Coke and Deep Fried Oreos on 10/10/20"
    order_date = "10/10/20"
    customer_id = 14
    cus = Customer(customer_id=customer_id)
    assert cus.view_order_history(cus.customer_id, order_date) == expected_response ,"Customer is not able to view the order history!"

#Requirement 5.5.1 - View user history and repeat order
def test_check_repeat_order_button_text():
    expected_resposne = "Repeat last order"
    customer_id =  12
    cus = Customer(customer_id=customer_id)
    assert cus.check_repeat_order_button_text(cus.customer_id) == expected_resposne, "Repeat order history button does not have the correct text!"


#Requirement 5.5.2 - Users with registered accounts can save their favorite foods and meals.
def test_add_item_to_favorites_success():
    expected_response = "Item added to your favorites successfully"
    customer_id = 14
    menu_item = "Kiwi Juice"
    cus = Customer(customer_id=customer_id)
    assert cus.add_item_to_favorites(customer_id, menu_item) == expected_response, "Unable to add menu item to customer's favorites!"

#Requirement 5.5.2 - Users with registered accounts can save their favorite foods and meals.
def test_add_item_to_favorites_failure():
    expected_response = "Item already exists in your favorites"
    customer_id = 14
    menu_item = "Kiwi Juice"
    cus = Customer(customer_id=customer_id)
    assert cus.add_item_to_favorites(customer_id, menu_item) == expected_response, "Unable to check if menu item is in the customer's favorites!"

#Requirement 5.5.3 -  Delivery provider live tracking and IFRAME - cannot be tested 

#Requirement 5.5.4 - Delivery driver tracking for restaurant 
def test_check_driver_arrival_time_status():
    order = Orders(10)
    staff= RestaurantStaff(12)
    dp = DeliveryProvider()
    expected_time = "12:43 pm"
    assert dp.check_driver_arrival_time_status(order.order_id, staff.employee_id) == expected_time, "Arrival time not available for tracking by restaurant staff!"

def test_calcualate_remaining_time_for_delivery_pickup():
    dp = DeliveryProvider()
    expected_arrival_time = "12:43 pm"
    expected_remaining_time = "32 minutes and 41 seconds"
    assert dp.calcualate_remaining_time_for_delivery_pickup(expected_arrival_time) == expected_remaining_time, "Calculation for the remaining time for delivery driver's arrival failed!"
 
#Requirement 5.5.5 - Ready for pickup alert cannot be tested because alert is a UI function that is out of scope for our testing 

#Requirement 5.8 - Comments section 
def test_add_comment():
    customer =  Customer(customer_id=12)
    com = CommentsAndFeedback(comment_id=1, comment_text="I love the food here!", customer_id= customer.customer_id)
    rating = 5
    expected_response =  "Comment posted succesfully"
    assert com.add_comment(com.comment_id, com.comment_text, com.customer_id, rating) == expected_response, "Unable to post comment!"
#Requirement 5.8.1 - Verified customers can post comments and feedback
def test_add_comment_to_menu_item():
    menu_item = MenuItem(menu_item_id = 1)
    cus = Customer(customer_id=10)
    com = CommentsAndFeedback(comment_id=1, comment_text="I hate this menu item!", customer_id= cus.customer_id)
    expected_response = "Comment to menu item added successfully"
    assert com.add_comment_to_menu_item(menu_item.menu_item_id, com) == expected_response, "Unable to add comment to menu item!"
#Requirement 5.8.1 - Verified customers can post comments and feedback
def test_delete_comment_from_menu_item():
    menu_item = MenuItem(menu_item_id = 1)
    cus = Customer(customer_id=10)
    com = CommentsAndFeedback(comment_id=1, comment_text="I hate this menu item!", customer_id= cus.customer_id)
    expected_response = "Comment from menu item deleted successfully"
    assert com.delete_comment_from_menu_item(menu_item.menu_item_id, com) == expected_response, "Unable to delete comment from menu item!"
#Requirement 5.8.1 - Verified customers can post comments and feedback
def test_verify_add_comment_button_text():
    invalid_add_comment_button_text = ["Add comment", "Whatsupbro", "Waagwaan", "Kiddaan"]
    for comment in invalid_add_comment_button_text:
        com = CommentsAndFeedback()
        assert com.verify_add_comment_button_text(comment) == True, "Invalid add comment button text detected!"

#Requirement 5.8.2 - Share experiences and seasonal recipe Wishlist
def test_verify_add_seasonal_recipe_button_text():
    cus = Customer(customer_id=12)
    srw = SeasonalRecipesWishlist(wishlist_id=10, recipe_description="How to bake good pot brownies", attachments="marijuana.jpg", links="https://www.ganjika-house.com/" )
    expected_message = "Recipe added succesfully"
    assert srw.add_wishlist(cus.customer_id) == expected_message, "Unable to add wishlist!"

def test_verify_add_comment_button_text():
    invalid_button_text = ["Add wishlist", "Keep wishing" ]
    for comment in invalid_button_text:
        srw = SeasonalRecipesWishlist()
        assert srw.verify_add_seasonal_recipe_button_text(comment) == True, "Invalid button text detected!"
