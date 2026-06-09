# Today task- Enter your pincode number and get the dict. and print all the values of these dict.


address={"Message":"Number of Post office(s) found: 12","Status":"Success","PostOffice":[{"Name":"Belan Bazar","Description":"","BranchType":"Sub Post Office","DeliveryStatus":"Non-Delivery","Taluk":"Munger","Circle":"Munger","District":"Munger","Division":"Monghyr","Region":"Patna HQ","State":"Bihar","Country":"India"}]}


for i in address["PostOffice"]:
    print(i["Name"])
    print(i["Taluk"])
    print(i["Circle"])
    print(i["District"])
    print(i["Division"])
    print(i["Region"])
    print(i["State"])
    print(i["Country"])
    print("\n")
    
    

    
    
