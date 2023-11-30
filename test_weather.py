import pytest
from main import weather  # Replace 'your_script_name' with the actual name of your script


def weather():
    
    city = "London"  
    result = weather(city)
    assert result == 200


