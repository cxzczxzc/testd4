class SeasonalRecipesWishlist():
    def __init__(self, wishlist_id=None, recipe_description=None, attachments = None, links = None):
        self.wishlist_id = wishlist_id if wishlist_id is not None else None
        self.recipe_description = recipe_description if recipe_description is not None else None 
        self.attachments = attachments if attachments is not None else None
        self.links = links if links is not None else None
    #this method should verify that the button text is what we expect and not something else
    def verify_add_seasonal_recipe_button_text(self, button_text):
        valid_button_text = "Add Seasonal Wishlist"
        if button_text == valid_button_text:
            return True
        else:
            return False
    #This method should add a wishlist submitted by a customer to the database
    # When a wishlist is successfully submitted it should return a message indicating so
    def add_wishlist(self, customer_id):
        return NotImplemented