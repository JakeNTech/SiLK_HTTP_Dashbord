# SiLK_HTTP_Dashbord
> JakeNTech, 2021; A simple, Python based, HTTP webserver for interacting with SiLK.

It's not very good...but it's giving me something to mess around with for the moment...so that's got to be a good thing right?
## TO DO
1- Show a grid on the back of the graphs
2- Line of best fit on the graphs that will work with it
3- Think of other things that could be done with SiLK
4- Add ability to control sensor
## Instillation
If SiLK is already installed on the box:
```bash
$ git clone https://github.com/JakeNTech/SiLK_HTTP_Dashbord.git
$ cd SiLK_HTTP_Dashbord
$ pip3 install -r requierments.txt
$ python3 main.py
```
If SiLK isn't installed then two additional steps are required:
```bash
$ git clone https://github.com/JakeNTech/SiLK_HTTP_Dashbord.git
$ cd SiLK_HTTP_Dashbord/docs
$ chmod +x install_silk.sh
$ ./install_silk.sh
```
Configuration of SiLK then needs to be done, see <https://tools.netsa.cert.org/silk/silk-on-box-deb.html#Configuring> on how to do this.

## Configuration
Details about how to use the configuration file see <https://github.com/JakeNTech/SiLK_HTTP_Dashbord/blob/main/docs/config.md>. The config file must be present, although the values are pre-set if they aren't valid. Below is the default JSON file:
```JSON
{
	"data_unit":"megabytes",
	"decimal_places":2
}
```
## Documentaion
To view all the documentaion for this project please see <https://github.com/JakeNTech/SiLK_HTTP_Dashbord/blob/main/docs/> the pages are broken down into the names of the different scripts and files that are used in this project.