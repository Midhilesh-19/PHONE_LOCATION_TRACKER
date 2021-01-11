import phonenumbers  #pip install phonenumbers and import

number = "+..1111111111" #here give the number with country code

from phonenumbers import geocoder #geocoder is a inbuilt in phonenumbers pacakage

call_number = phonenumbers.parse(number,"CH") #"CH","RO","GB" is required codes for libraries
print(geocoder.description_for_number(call_number,"en"))

from phonenumbers import carrier #carrier is a inbuilt in phonenumbers pacakage
service_number = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))

from phonenumbers import timezone #timezone is a inbuilt in phonenumbers pacakage
tz_number = phonenumbers.parse(number,"GB")
print(timezone.time_zones_for_number(tz_number))