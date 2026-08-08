import pandas as pd

def find_full_name(email, csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    # Find the row where the email matches
    result = df[df['email'] == email]
    # Return the full name if found
    if not result.empty:
        return result.iloc[0]['full_name']
    return None

email_to_lookup = "t**7@g.com"
csv_file_path = "contacts.csv"

full_name = find_full_name(email_to_lookup, csv_file_path)

if full_name:
    print(f"The full name associated with {email_to_lookup} is {full_name}.")
else:
    print(f"No full name found for {email_to_lookup}.")
