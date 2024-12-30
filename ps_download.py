import requests, zipfile

# URL of the zip file
url = 'https://storage.yandexcloud.net/pioneer-doc.geoscan.ru-static/dwnlds/software/PioneerStation/PioneerStationLinux.zip'

# Download the file
response = requests.get(url)

# Save the file
with open('PioneerStationLinux.zip', 'wb') as file:
    file.write(response.content)

# Extract the zip file
with zipfile.ZipFile('PioneerStationLinux.zip', 'r') as zip_ref:
    zip_ref.extractall()