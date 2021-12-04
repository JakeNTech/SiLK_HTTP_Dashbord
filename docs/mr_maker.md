# mr_maker.py
This is the script that will generate the graphs, save them and return the paths of them in JSON. It's been seperated out to make it a bit easier on the eyes, there is litterly no other reason for this. I suspect at some point I might mess arround with threading to make it a bit faster but for the moment it's good enough...well I say this but testing on a laptop is very different to testing on the Pi.
## Chunk Data function
```
Summary
    Args:
        df (DataFrame): DataFrame for the Chunk Data
        file_name (String): Desired name of output files
    
    Returns:
        TYPE: JSON, location of each Graph and what it shows

```
Creates the graphs for the chunk data, command used to generate this is in py_api.