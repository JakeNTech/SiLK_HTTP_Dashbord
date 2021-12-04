# Config.json
The configuration file allows you to change some key variables, rather than using command line arguments when running the script. These options are:
```
Unit of Data
Number of decimal places
```
This configuration file uses JSON to make it easy to read and understand.
## Unit of Data
The unit of data can be any of the following:
```JSON
"data_unit":"bytes"
"data_unit":"kilobytes"
"data_unit":"megabytes"
"data_unit":"gigabytes"
"data_unit":"terabytes"
```
This changes the divion factor when data is read from SiLK (By defualt it uses Bytes, which isn't to relatable).
## Number of Decimal Places
Some of the data shown in the HTTP site is rounded to make it look nicer, while not removing too much infomaiton. The number of decimal places can be configured by changing the entry in the `config.json` file:
```JSON
"decimal_places":2
"decimal_places":100
```
(I would't recommend using 100 decimal places though!)
## Sensor - NOT YET IMPLEMENTED
Silk allows for multiple sensors to be configured, with whatever name you like. This can be controlled with the below:
```JSON
"sensor_name":"S0"
```
This currently has no use
## Implementation of Config file
The JSON file is loaded in `/api/configure.py` to allow access to the global variables it declares.
## Example of Completed JSON
```JSON
{
	"data_unit":"megabytes",
	"decimal_places":2,
	"sensor_name":"S0"
}
```