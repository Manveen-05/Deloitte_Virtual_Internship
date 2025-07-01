import json, unittest, datetime

with open("./data-1.json","r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json","r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json","r") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1 (jsonObject):
    # split the location field using the / as the delimiter
    locationParts = jsonObject['location'].split('/')
    # create a new dictionary for the unified format
    result = {
        "deviceID": jsonObject['deviceID'], #Extract deviceID
        "deviceType": jsonObject['deviceType'], #Extract deviceType
        "timestamp": jsonObject['timestamp'], #Extract timestamp
        "location": {
            'country': locationParts[0], #Extract the country from the location 
            'city': locationParts[1],  #Extract the city from the location 
            'area': locationParts[2],  #Extract the area from the location 
            'factory': locationParts[3],  #Extract the factory from the location 
            'section': locationParts[4],  #Extract the section from the location 
        },
        'data':{
            'status': jsonObject['operationStatus'], # copy the operationStatus as status
            'temperature': jsonObject['temp'], # copy the temp as temperature
        }
    }

    # IMPLEMENT: Conversion From Type 1

    return result

# convert json format 2 to the unified format
def convertFromFormat2 (jsonObject):
    #convert the ISO timestamp to milliseconds since epoch
    date = datetime.datetime.strptime(jsonObject['timestamp'], #Extract the ISO timestamp
                                      '%Y-%m-%dT%H:%M:%S.%fZ') #ISO timestamp format
    timestamp = round((data-datetime.datetime(1970,1,1)).total_seconds()*1000) # convert to milliseconds
    # create a new dictionary for the unified format
    result = {
        "deviceID": jsonObject['deviceID']['id'], #Extract device ID
        "deviceType": jsonObject['deviceType']['type'], #Extract device Type
        "timestamp": timestamp, #copy the timestamp
        "location": {
            'country': jsonObject['country'], #Extract country 
            'city': jsonObject['city'],  #Extract city 
            'area': jsonObject['area'],  #Extract area 
            'factory': jsonObject['factory'],  #Extract factory 
            'section': jsonObject['section'],  #Extract section 
            },
            'data': jsonObject['data'] # copy the data
    }

    return result


def main (jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


class TestSolution(unittest.TestCase):

    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):

        result = main (jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):

        result = main (jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )

if __name__ == '__main__':
    unittest.main()
