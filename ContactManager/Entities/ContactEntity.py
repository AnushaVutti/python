class ContactEntity:
    first_name = ""
    last_name = ""
    country_code = ""
    phonenumber = 1111111111
    email_address = ""
    facebook_id = ""
    twitter_id = ""
    website = ""

    #will be address class objects not strings (to be created by Anusha)
    home_address = ""
    office_address = ""

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return "This is contact for {}, with contact number {}".format(self.first_name + " " + self.last_name, self.phonenumber)

    #create parameterized methods
    #overloaded methods
    #child classes
    #method overriding