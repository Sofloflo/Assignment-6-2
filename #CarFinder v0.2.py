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
print("\n")

if (response == 1):
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

if(response == 2):
    search = input("Please Enter the full Vehicle name: ")
    if (search == "Ford F-150"):
         print("Ford F-150 is an authorized Vehicle")
         print("\n")
         print("**********************************")
         print("AutoCountry Vehicle Finder v0.1")
         print("**********************************\n")
         print("Please Enter the following number below from the following menu:\n")
         print("1. PRINT all Authorized Vehicles")
         print("2. SEARCH for Authorized Vehicle")
         print("3. Exit\n")
    if (search == "Tesla"):
         print("Tesla is not an authorized vehicle, if you received this in error please check the spelling and try again")
         print("\n")
         print("**********************************")
         print("AutoCountry Vehicle Finder v0.1")
         print("**********************************\n")
         print("Please Enter the following number below from the following menu:\n")
         print("1. PRINT all Authorized Vehicles")
         print("2. SEARCH for Authorized Vehicle")
         print("3. Exit\n")
          

if (response == 3):
    print( "Thank you for using the AutoCountry Vehicle Finder, good-bye!")