## Synopsis
`deleteIndicies.py` is a python script that delete old Elastic Search indexes. It list all indexes in Elastic Search. Keep only these that apply in a regex pattern and which is older than the date that obtains it delete it.

## Requirments 
Python's Elastic Search client.
```
elasticsearch
```
In order to install it run:
```
pip install elasticsearch
````

## Execution
If required packages are installed,to execute that script run
```
./deleteIndicies.py -e <elasticSearch host> -f "<regex pattern>" -i <the number of the last days that you want to keep>
./deleteIndicies.py -e localhost:9200 -f "^topbeat\-hhps\-\d{4}\.\d{2}\.\d{2}$" -i 10

