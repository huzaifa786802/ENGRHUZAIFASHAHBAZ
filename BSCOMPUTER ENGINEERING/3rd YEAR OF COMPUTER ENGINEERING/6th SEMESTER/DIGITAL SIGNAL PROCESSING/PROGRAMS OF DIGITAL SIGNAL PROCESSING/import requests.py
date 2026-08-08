import requests

# URL of the Brahms audio file (replace with the actual URL)
url = 'http://example.com/path/to/brahms.mp3'

# Send a HTTP request to the URL
response = requests.get(url)

# Ensure the request was successful
if response.status_code == 200:
    # Save the file locally
    with open('brahms.mp3', 'wb') as file:
        file.write(response.content)
    print('Download complete.')
else:
    print('Failed to download the file.')
