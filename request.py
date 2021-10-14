import requests


parameters = {"imagebase": 268435456.0, "checksum": 848033.0, "sizeofstackcommit": 4096.0, "sizeofstackreserve": 1048576.0, "sizeofuninitializeddata": 0.0,
              "loadconfigurationsize": 104.0, "sizeofinitializeddata": 568320.0, "loaderflags": 0.0, "sizeofheapreserve": 1048576.0, "resourcesmeansize": 1028.0}

url = 'http://localhost:5000/predict_api'
r = requests.post(url, json=parameters)

print(r.json())
