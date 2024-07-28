allowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
menu = f"""********************************
AutoCountry Vehicle Finder v0.3
********************************
Please Enter the following number below from the following menu:\n
1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. ADD Authorized Vehicle
4. Exit
********************************"""


def mainMenu(menu):
  print(menu)
  return menu


def selectChoice():
  choice = input("\nEnter Selection: ")
  return choice


def printCars(allowedVehiclesList):
  returnString = "\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
  print(returnString)
  returnString += "\n"
  for vehicle in allowedVehiclesList:
    print(vehicle)
    returnString += vehicle + "\n"
  return returnString


def searchVehicle(allowedVehiclesList):
  search = input("Please Enter the full Vehicle name: ")
  if search in allowedVehiclesList:
    print(f"{search} is an authorized vehicle")
  else:
    print(f"{search} is not an authorized vehicle, if you received this in error please check the spelling and try again")


def addCar(allowedVehiclesList):
  car = input("Please Enter the full Vehicle name you would like to add: ")
  if car not in allowedVehiclesList:
    allowedVehiclesList.append(car)
    print(f'You have added "{car}" as an authorized vehicle')
  else:
    print("Authorized Vehicle already in system.")



def main(allowedVehiclesList, menu):
  while True:
    mainMenu(menu)
    choice = selectChoice()
    if choice == "1":
      printCars(allowedVehiclesList)
    elif choice == "2":
      searchVehicle(allowedVehiclesList)
    elif choice == "3":
      addCar(allowedVehiclesList)
    elif choice == "4":
      exitString = "\nThank you for using the AutoCountry Vehicle Finder, good-bye!"
      print(exitString)
      return exitString   
    else:
      print("\nPlease enter 1 or 2.\n")


if __name__ == "__main__":
  main(allowedVehiclesList, menu)