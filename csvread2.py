import csv
from influxdb import InfluxDBClient
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'deneme1')
client.create_database('deneme1')
time1 = 0
with open('line_example3.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        liste = row[0].split(",")
        time = int(str(liste[1:2])[2:-2])
        time1 = time1 + 1
        print(time1)
        json_body = [
            {
                "measurement": "veri5",
                    "tags": {
                        "Event": str(liste[2:3])[2:-2],
                        "prodUnit": str(liste[4:5])[2:-2]
                },
                "time": time,
                "fields": {
                    "name": str(liste[0:1])[2:-2],
                    "status": str(liste[6:7])[2:-2],        
                }
            }   
        ]
        client.write_points(json_body)