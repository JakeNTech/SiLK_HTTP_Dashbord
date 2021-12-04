# py_api.py
The API has a number of functions:
```
Check Status
Display the details of records from today
```
## Check Status - NOT IMPLIMENTED PROPERLY
This functions runs the commands to display if SiLK is running on or not.\
Two commands are used to discover the status:
```
YAF: service yaf status
rwflowpack: service rwflowpack status
```
***NOTE: At the moment the result will always be stopped, I haven't tested this on a Pi with SILK yet and only have it configured to read data that I have copied from the Pi into WSL for testing!***
## Details from Today - NOT IMPLIMENTED PROPERLY
The idea of this is to display some infomation about the traffic seen by the sensor today:
```
Total number of records
Total packets seen
Total Kilobytes seen
```
This infomation is calculated form splitting the data from the current day down into 1 hour chunks, we don't need the full data for this infomation. All infomaiton is rounded to 2 decimal places and Bytes are converted into Kilobytes to make it look a bit less scary...although megabytes would also be fine for this application...could be a setting later down the line.
***NOTE: At the moment this is takeing a result from a CSV file generated ages ago...I don't have Data in the SiLK install on this machine; will test it later down the line.***\
Now also inclueds details of grahphs that are generated about this data, not sure how to impliment this...Download them or make them show on the Interface. Download sounds eaiser!