class Customer:
    def __init__(self, customer_id, dietary_preferences = None, dietary_restrictions = None):
        self.customer_id = customer_id
        self.dietary_preferences = dietary_preferences if dietary_preferences is not None else None
        self.dietary_restrictions = dietary_restrictions if dietary_restrictions is not None else None
    #This would save the dietary restrictions, like Halal, Kosher, etc. to the user's profile 
    def add_dietary_restrictions(self, dietary_restrictions, customer_id):
        return NotImplemented

    #This would save the dietary preferences, like Paleo, Keto, etc. to the user's profile 
    def add_dietary_preferences(self, dietary_restrictions, customer_id):
        return NotImplemented

    #We only allow at most 1 dietary restriction per customer, in order to manage the menu without much complexity
    def get_number_of_dietary_restrictions(self, customer_id):
        return NotImplemented

    #We only allow at most 1 dietary preference per customer, in order to manage the menu without much complexity
    def get_number_of_dietary_preferences(self, customer_id):
        return NotImplemented

    
    def get_dietary_restrictions(self, customer_id):
        return NotImplemented

   
    def get_dietary_preferences(self, customer_id):
        return NotImplemented

    #this method should take the menu items and generate a list suited for the customer
    #then it will save that to the database
    #it will return a response message indicating success if everything goes well 
    def generate_custom_menu(self, dietary_restriction, dietary_preference, customer_id, menu_items):
        return NotImplemented

    #this method should check if the customer is eligible for deal of the day offer 
    def check_eligibility_for_deal_of_day(self, customer_id, number_of_orders_placed):
        if number_of_orders_placed >= 20: #this data would come from a database in a real life application
            return True
        else:
            return False
    #this method should return the deal of the day for the customer based on the most ordered menu item 
    def view_deals_of_the_day(self, customer_id):
        return NotImplemented

    #this method should save order history of the customer to the database and return a message indicating so
    def save_order_history(self, customer_id, menu_items, order_date):
        return NotImplemented

    #this method would retrieve the order history from the database 
    def view_order_history(self, customer_id, order_date):
        return NotImplemented

    #this method would add the selected item to user favorites, if not already present
    #if the item already exists it would return a message indicating so
    #if the item gets added it would return a message indicating so 
    def add_item_to_favorites(self, customer_id, menu_item):
        return NotImplemented

    #checks if the button text matched the expected button text 
    def check_repeat_order_button_text(self, customer_id):
        return NotImplemented
