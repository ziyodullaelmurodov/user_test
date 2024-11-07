from user import User

user = User("Elmurodov", "Ziyodullo", 19, "programmer", False)
# Create tests check book attributes
def test_book_attributes():
    assert user.first_name == "Elmurodov"
    assert user.author == "Ziyodullo"
    assert user.age == 19
    assert user.job == "programmer"
   
    assert user.availability == False