class AddressEntity:
    flat_no=""
    street=""
    city=""
    state=""
    country=""
    zipcode=""

    def __init__(self)->None:
        pass
    def __str__(self)->str:
        return "Address is : "+self.flat_no+" "+self.street+" "+self.city+" "+self.state+" "+self.country+" "+self.zipcode
        