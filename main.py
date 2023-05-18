from base_model import FamiliesDatabase

def main():
    query = FamiliesDatabase()  # Create an instance of FamiliesDatabase
    family_data = {
        "Mail": "Tova@example.com",
        "FirstName": "Tova",
        "LastName": "Smith",
        "city": 1,  # Assuming city ID is 1
        "Neighborhood": 2,  # Assuming neighborhood ID is 2
        "Cell": "123-456-7890",
        "NumOfChildren": 2,
        "OldestChild": 5,
        "YoungestChildren": 2,
    }
    query.create(family_data)  # Pass the instance and the data dictionary to create

if __name__ == "__main__":
    main()

