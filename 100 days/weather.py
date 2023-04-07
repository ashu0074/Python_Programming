""" 16.Write a program that will determine weather when the value of temperature and humidity is provided by the user.
TEMPERATURE(C)      HUMIDITY(%)      WEATHER

      >= 30                             >=90                Hot and Humid
      >= 30                             < 90                 Hot
      <30                                >= 90               Cool and Humid
      <30                                 <90                 Cool                      """


def weather(temp, humid):
    if (temp >=30) and (humid >=90):
        print("Hot and Humid")
    elif (temp>=30) and (humid < 90):
        print("Hot")
    elif (temp<30) and (humid>=90):
        print("Cool and Humid")
    elif (temp <30) and (humid <90):
        print("Cool")
    else:
        print("you enter the wrong input ")

temperature = int(input("Enter the temperature : "))
humidity = int(input("Enter the humidity : "))
weather(temperature,humidity)