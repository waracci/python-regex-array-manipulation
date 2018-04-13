import re
import json
#create an array with ten items
items = [
    'BizTech Limited, Nairobi0792009522info@kenyaplex.com',
    'Cable Options Limited, Nairobi0722 308 793info@cableoptions.co.ke',
    'Likin Electrical Services, Mombasa+254736254230info@likinelectricalservices.co.ke'
]
# print(len(items))
businesses = []#?

for item in items:
    input = item
    # x = re.match('(^[A-Za-z ,]+)'+'([\+ 0-9]+)'+'([a-z@\.]+)', a)

    regExpStr = re.match('(^[A-Za-z ,]+)'+'([\+ 0-9]+)'+'([a-z@\.]+)', input)

    # print (regExpStr)
    # separate return value
    businessNameLocation = regExpStr.group(1)
    businessName = businessNameLocation.split(",")[0]
    location = businessNameLocation.split(",")[1]
    # print(businessName)
    #returns businessname plus location
    mobile = regExpStr.group(2)
    #return mobile number
    email = regExpStr.group(3)
    #return email
    # print(businessName, location, mobile, email)
    businessDataList = {
                        'name': businessName,
                        'location': location,
                        'mobile': mobile, 
                        'email': email
                        }
    # businessesJsonData = json.dumps(businessDataList)
    businesses.append(businessDataList)
print(businesses)
# allbusinesess =json.dumps(businesses)
# print(allbusinesess)
# for index in businesses:
    # print(index["mobile"])
    # print(index["location"])