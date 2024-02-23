# Github activity log files to parquet

### Description:
 This is a simple demo project that converts json data and write in Parquet format

### File Specifications

app.py -  Is the main() file which needs to be executed

util.py - Creates SparkSession in order to handle the files based on DEV or PROD

read.py - reads the json file as DataFrame

process.py - creates new Dataframe from json DataFrame with 3 new columns 'year', 'month', 'day'

write.py - writes the new DataFrame data as Parquet in raw folder

### Environmental

Following are the environmental variables used

ENVIRON - DEV/PROD to use local/yarn resources for files</br>
SRC_DIR - Source location of the json log files</br>
SRC_FILE_FORMAT - Json as source file format</br>
SRC_FILE_PATTERN -  file name pattern </br>
TGT_DIR - Target directory to write down the files</br>
TGT_FILE_FORMAT - Parquet as target file format</br>

```
[saravanan@LAPTOP]$ export ENVIRON=PROD
[saravanan@LAPTOP]$ export SRC_DIR=/user/`whoami`/github/landing/ghactivity
[saravanan@LAPTOP]$ export SRC_FILE_FORMAT=json
[saravanan@LAPTOP]$ export TGT_DIR=/user/`whoami`/github/raw/ghactivity
[saravanan@LAPTOP]$ export TGT_FILE_FORMAT=parquet
[saravanan@LAPTOP]$ export SRC_FILE_PATTERN=2021-01-13
[saravanan@LAPTOP]$ export SRC_FILE_PATTERN=2021-01-15
```
### Execution
```
spark3-submit --master yarn --py-files itv-ghactivity.zip --conf spark.ui.port=0 app.py
```
### Data source

You can download the activity data from Github archive 

```
https://www.gharchive.org/
```
