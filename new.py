class Type_of_request:
    def __init__(self,process_name = "Accounting", tool = "SAP", access_type = "Business Access"):
        self.process_name = process_name
        self.tool = tool
        self.access_type =access_type

        print(process_name,tool,access_type)

#request = Type_of_reques("Booking", "SAS", "Base access")

request = Type_of_request("Booking", "AT", "Country Access")
request.access_type


