from testd4.restaurantstaff import RestaurantStaff


#Requirement 7.6 - Add deals of the day functionality for the restaurant owner
def test_view_most_popular_menu_items():
    expected_popular_items = ["Chips", "Coke", "Pot Brownies"]
    rs = RestaurantStaff()
    assert rs.view_most_popular_menu_items() == fake_popular_items, "Restaurant owner unable to view the most popular menu items!"

def test_create_deal_of_the_day_for_all_customers():
    expected_deal_of_the_day = "Pot Brownies"
    expected_discounted_price = "@$10 per kilo"
    rs = RestaurantStaff()
    assert rs.create_deal_of_the_for_all_customers(expected_deal_of_the_day, expected_discounted_price) == expected_deal_of_the_day, "Restaurant staff unable to create deal of the day!"
def test_deal_of_the_day_validity():
    special_deal_id = "007"
    created_date = "10/10/20"
    rs = RestaurantStaff()
    assert rs.check_deal_of_the_day_validity(special_deal_id, created_date) == True, "The deal is no longer valid!"