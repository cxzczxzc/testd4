class CommentsAndFeedback:
    def __init__(self, comment_id = None, customer_id = None, comment_text =  None):
        self.comment_id = comment_id if comment_id is not None else None 
        self.customer_id = customer_id if customer_id is not None else None 
        self.comment_text = comment_text if comment_text is not None else None
    #this method should take the given parameters and save the comment to the database
    #upon succesful submission of a comment, it should return a message indicating so
    def add_comment(self, comment_id, customer_id, comment_text, rating):
        return NotImplemented
    #this method would add a comment to the chosen menu item 
    #the argument comment contains all the fields defined in the CommentsAndFeeback class
    #upon succesful submission of a comment, it should return a message indicating so
    def add_comment_to_menu_item(self, menu_item_id, comment):
        return NotImplemented
    #this method would delete a comment from the chosen menu item 
    #the argument comment contains all the fields defined in the CommentsAndFeeback class
    #upon succesful deletion of a comment, it should return a message indicating so
    def delete_comment_from_menu_item(self, menu_item_id, comment):
        return NotImplemented
    #this method would verify the text that is displayed in the Add comment button
    def verify_add_comment_button_text(self, add_comment_button_text):
        valid_comment_button_text = "Add comments or feedback"
        if valid_comment_button_text==add_comment_button_text:
            return True
        else:
            return False