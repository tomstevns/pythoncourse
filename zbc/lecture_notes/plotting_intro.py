import os
import csv
import json
from downloader import download

url = 'https://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv'
file_name = os.path.basename(url)
download(url, file_name)

""" with open(file_name) as fp:
    content = fp.readlines() """

# printer med newline 
""" for line in content[:200]:
    print(line.split(',')) """

# Sådan kan man læse en csv fil, men det gør man ikke.
# Brug i stedet for standard csv modul.
""" for line in content[1:200]:
    aar, bydel, alder, startkode, person = line.split(',')
    aar, bydel, alder, startkode, person = int(aar), int(bydel), int(alder), int(startkode), int(person) 
    print(aar, bydel, alder, startkode, person) """

# csv modulet. Husk at lave type cast, hvis float
with open(file_name) as fp: # fp = file pointer.
    reader = csv.reader(fp)
    header_row = next(reader) # hoppper over headerlinjen
    for line in reader:
        aar, bydel, alder, startkode, personer = line
        aar, bydel, alder, startkode, personer = int(aar), int(bydel), int(alder), int(startkode), int(personer) 
        print(personer)

# JSON fil
# csv modulet. Husk at lave type cast, hvis float
""" with open(file_name) as fp: # fp = file pointer.
    reader = json.load(fp)
    header_row = next(reader) # hoppper over headerlinjen
    for line in reader:
        aar, bydel, alder, startkode, personer = line
        aar, bydel, alder, startkode, personer = int(aar), int(bydel), int(alder), int(startkode), int(personer) 
        print(personer) """

# Printer det hele
# print(content)

# printer (slicer dataset) fra 50000 til 500012
# print(content[50000:50012])
