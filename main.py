import requests

print("Welcome to the Open Weather API program, I hope you have a great experience using this program!")
print()

base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = "d08cbb911c7274645def2112cb3f5975"
no_spaces = ""
#I created an empty string for this variable to be used in input validation later on, as without creating this, it won't work in the main() function.

def main():
  location = input("Please enter your city or ZIP: ")
  no_spaces == location.replace(" ", "")
# I created a variable "no_spaces" to take what was assigned to the variable "location" and remove spaces from it so if the user were to input a city with a space in the name, for example "Sioux City" since ".isalpha" only checks for letters in the alphabet and will reject if there is a space, so any city the user inputs with a space will not be true for ".isalpha." This way it can check the user input without any spaces and then use what was input for "location" for the url if it passes. Connection issues were also occurring if "siouxcity" was passed through to the url, as opposed to Sioux City with a space.
  
  if location.isnumeric() and len(location) == 5:
    print()
#This is to check if a ZIP is entered, that it is numeric and the right length.
  
  elif no_spaces.isalpha and len(location) >= 4: 
   print()
#This uses the no_spaces variable to make sure that if a city name is the input, it is part of the alphabet without the space(s) and that the length is at least 4 characters long.
  
  else:
    print("Invalid input, please try again.")
    print()
    main()
#This returns a message to the user if neither parameter is met, and returns to the beginning of the function for the user to try entering a different location.

  while True:
    try:
     url = f"{base_url}?q={location},us&units=imperial&APPID={appid}"
    #this takes everything that is being held in the base_url, location, and appid variables and plugs those in to the url.
     print(url)
     print()
     response = requests.get(url)
     unformated_data = response.json()
     
     city = unformated_data["name"]
     weather = unformated_data["main"]["feels_like"]
     temp = unformated_data["main"]["temp"]
     temp_min = unformated_data["main"]["temp_min"]
     temp_max = unformated_data["main"]["temp_max"]
     wind_speed = unformated_data["wind"]["speed"]
     humidity = unformated_data["main"]["humidity"]
    
#This goes and gets the all of these items from the Open Weather url and assigns these to each variable, which is then displayed to the user for that particular city or ZIP code below with the print() functions.
      
     print("Connection was successful!")
     print()
     print(f"You requested information for {city}:")
     print()
     print(f"The current temp is: {temp}°") 
     print(f"It currently feels like: {weather}°")
     print(f"The min temp is: {temp_min}°")
     print(f"The max temp is: {temp_max}°")
     print(f"The current wind speed is: {wind_speed} mph")
     print(f"The humidity is: {humidity}%")
     print()
     break
     
    except:
     print(f"Error status code: {response.status_code}. Connection was unsuccessful.")
     print()
     main()

  #This will return the status code if the connection was not successful, tell the user the connection was not successful, and then returns to the beginning of the function so the user can try again.
  
  more_requests()
  #This function gets called if the main() function successfully passes all parameters. This previously was in the while loop, but that created an issue when a user what try to quit the program.

def more_requests():
    additional_request = input("Would you like to enter another location? (Y or N): ")
    if additional_request.lower() == "n":
      print()
      print("Thank you for using the Open Weather API Program, I hope you return soon for all your weather related needs!")
      quit()
    elif additional_request.lower() == "y":
      print()
      main()
   
# The ".lower" will accept user input of either lower case "y" or upper case "Y", and then will call the connection_test() function. Same with a lower case "n" or upper case "N". Also, if "N" or "n" is entered, it will end the program.
  
    else:   
      print()
      print("Please enter a correct value and try again:")
      print()
      more_requests()
      
  #This will catch if a user inputs something other than Y, y, N, or n and then prompt the user to try again because they did not enter one of those values.
 
main()