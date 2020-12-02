class Customer:
    #This would save the dietary restrictions, like Halal, Kosher, etc. to the user's profile 
    def add_dietary_restrictions(self, dietary_restrictions, customer_id):
        return NotImplementedError
    #This would save the dietary preferences, like Paleo, Keto, etc. to the user's profile 
    def add_dietary_preferences(self, dietary_restrictions, customer_id):
        return NotImplementedError
    #We only allow at most 1 dietary restriction per customer, in order to manage the menu without much complexity
    def get_number_of_dietary_restrictions(self, customer_id):
        return NotImplementedError
    #We only allow at most 1 dietary preference per customer, in order to manage the menu without much complexity
    def get_number_of_dietary_preferences(self, customer_id):
        return NotImplementedError
    
    def get_dietary_restrictions(self, customer_id):
        return NotImplementedError
   
    def get_dietary_preferences(self, customer_id):
        return NotImplementedError
    #this method should take the menu items and generate a list suited for the customer
    #then it will save that to the database
    #it will return a response message indicating success if everything goes well 
    def generate_custom_menu(self, dietary_restriction, dietary_preference, customer_id, menu_items):
        return NotImplementedError
    #this method should check if the customer is eligible for deal of the day offer 
    def check_eligibility_for_deal_of_day(self, customer_id, number_of_orders_placed):
        if number_of_deals_placed >= 20: #this data would come from a database in a real life application
            return True
        else:
            return False
    #this method should return the deal of the day for the customer based on the most ordered menu item 
    def view_deals_of_the_day(self, customer_id):
        return NotImplementedError