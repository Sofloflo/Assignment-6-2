#CarFinder v0.2

allowedVehiclesList = ["Ford F-150", "Chevrolet Silverado", "Telsa CyberTruck", "Toyota Tundra", "Nissan Titan"]

print("**********************************")
print("AutoCountry Vehicle Finder v0.1")
print("**********************************\n")

print("Please Enter the following number below from the following menu:\n")
print("1. PRINT all Authorized Vehicles")
print("2. SEARCH for Authorized Vehicle")
print("3. Exit\n")

response = int(input("Enter here: "))

while(True):

     if (response == 1):
        print("\n")
        print(f'The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
        print("\n")
        for answer in allowedVehiclesList:
             print(answer)
        print("\n")
        print("**********************************")
        print("AutoCountry Vehicle Finder v0.1")
        print("**********************************\n")
        print("Please Enter the following number below from the following menu:\n")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. Exit\n")
        response = int(input("Enter here: "))
        print("\n")
        continue;

     if(response == 2):
          print("\n")
          search = input("Please Enter the full Vehicle name: ")
          if search in allowedVehiclesList:
               print("\n")
               print(f'{search} is an authorized vehicle')
               print("\n")
               print("**********************************")
               print("AutoCountry Vehicle Finder v0.1")
               print("**********************************\n")
               print("Please Enter the following number below from the following menu:\n")
               print("1. PRINT all Authorized Vehicles")
               print("2. SEARCH for Authorized Vehicle")
               print("3. Exit\n")
               response = int(input("Enter here: "))
               print("\n")
               continue;
          else: 
               print(f'{search} is not an authorized vehicle, if you received this in error please check the spelling and try again')
               print("\n")
               print("**********************************")
               print("AutoCountry Vehicle Finder v0.1")
               print("**********************************\n")
               print("Please Enter the following number below from the following menu:\n")
               print("1. PRINT all Authorized Vehicles")
               print("2. SEARCH for Authorized Vehicle")
               print("3. Exit\n")
               response = int(input("Enter here: "))
               print("\n")
               continue;
     if (response == 3):
          print("\n")
          print( "Thank you for using the AutoCountry Vehicle Finder, good-bye!")
          break;

     