# SiLK_HTTP_Dashbord
> JakeNTech, 2021; A simple, Python based, HTTP webserver for interacting with SiLK.

It's not very good...but it's giving me something to mess arround with for the moment...so that's got to be a good thing right?
## Instillation
If SiLK is already installed on the box:
```
$ git clone https://github.com/JakeNTech/SiLK_HTTP_Dashbord.git
$ cd SiLK_HTTP_Dashbord
$ pip3 install -r requierments.txt
$ python3 main.py
```
If SiLK isn't installed then two additional steps are required:
```
$ git clone https://github.com/JakeNTech/SiLK_HTTP_Dashbord.git
$ cd SiLK_HTTP_Dashbord/docs
$ chmod +x install_silk.sh
$ ./install_silk.sh
```
Configuration of SiLK then needs to be done, see <https://tools.netsa.cert.org/silk/silk-on-box-deb.html#Configuring> on how to do this.

## Configuration
Details about how to use the configuration file see <https://github.com/JakeNTech/SiLK_HTTP_Dashbord/blob/main/docs/config.md>. The config file must be present, although the values are pre-set if they aren't valid. Below is the defalt JSON file:
```JSON
{
	"data_unit":"megabytes",
	"decimal_places":2
}
```