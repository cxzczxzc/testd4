class DeliveryProvider:

    def get_delivery_provider(self, dp_name):
        currently_configured_dp =  "UberEats" #this should be a call to the database to get the currently configured delivery provider
        if dp_name == currently_configured_dp:
            return True
        else:
            return False
    
    def set_deliver_provider(self, dp_name):
        currently_configured_dp = dp_name #this would set the delivery provider as chosen by the user
        return NotImplemented
    
    #not implemented because this would require API interaction with the delivery provider
    #it should return a message that tells the restaurant staff about the status of the delivery provider's location
    #before the delivery person picks up the food
    def track_delivery_provider_for_restaurant(self, orderid):
        return NotImplemented
    
    #not implemented because this would require API interaction with the delivery provider
    #it should return an IFRAME that enables the customer to view status of the delivery provider's location
    #after the delivery provider picks up the food 
    def track_delivery_provider_for_customer(self, orderid):
        return NotImplemented


    #not implemented because this would require API interaction with the delivery provider
    #it should return a message that tells the user about the delivery status
    def track_order(self, orderid):
        return NotImplemented
   
    #not implemented because this would require API interaction with the delivery provider
    #it should return a message that confirms that the order was cancelled
    def cancel_order(self, orderid):
        return NotImplemented

    #not implemented because this would require API interaction with the delivery provider
    #this would help in selection of the best delivery provider for the customer
    #based on cost and delivery time 
    def get_best_delivery_option(self, orderid, dp_name):
        return NotImplemented

    #not implemented because this would require API interaction with the delivery provider
    #this method should generate a link to the delivery provider's service
    #the button text will be passed as an argument and should represent the delivery provider's name
    def generate_button_for_delivery(self, dp_name):
        button_text = "Order with " + dp_name
        return NotImplemented
    
    #not implemented because this would require API interaction with the delivery provider
    #this method should take the cart items and send them via an API call to the delivery provider
    def add_cart_items_to_delivery_provider(self, cart_items):
        return NotImplemented
    #not implemented because this would require API interaction with the delivery provider
    #this method should return a list of cart items added to the delivery provider's list
    def get_delivery_provider_cart_items(self):
        return NotImplemented

    

