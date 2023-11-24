import requests

def weather():
    headers = {
        'X-RapidAPI-Key': "36d9867717msh152a633d26299dep192786jsnf80ec7e2e717",
        'X-RapidAPI-Host': "weatherapi-com.p.rapidapi.com"
    }
    URL = "https://weatherapi-com.p.rapidapi.com/current.json?q="
    user_input = input("Enter city: ")

    data = requests.get(URL + user_input, headers=headers).json()

    celsius_temp = data.get('current', {}).get('temp_c')
    if celsius_temp is not None:
        print(f"Temperature in {user_input.capitalize()}: {celsius_temp}°C")
        return(200)
    else:
        print("Temperature data not available.")
        return(404)



Joshuaa = weather()
print(Joshuaa)    


