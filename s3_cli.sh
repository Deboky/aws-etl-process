# Data from the local file is uploaded to the s3 bucket
# Upload JSON Reference data to same location
# Download AWS CLI
# then install 
# then type aws in the command line

aws configure

aws s3 cp . s3://de-aws-raw-data-eu/youtube/ --recursive --exclude "*" --include "*.json"

# To copy all data files to its own location, following Hive-style patterns:
aws s3 cp CAvideos.csv s3://de-aws-raw-data-eu/youtube/region=ca/
aws s3 cp DEvideos.csv s3://de-aws-raw-data-eu/youtube/region=de/
aws s3 cp FRvideos.csv s3://de-aws-raw-data-eu/youtube/region=fr/
aws s3 cp GBvideos.csv s3://de-aws-raw-data-eu/youtube/region=gb/
aws s3 cp INvideos.csv s3://de-aws-raw-data-eu/youtube/region=in/
aws s3 cp JPvideos.csv s3://de-aws-raw-data-eu/youtube/region=jp/
aws s3 cp KRvideos.csv s3://de-aws-raw-data-eu/youtube/region=kr/
aws s3 cp MXvideos.csv s3://de-aws-raw-data-eu/youtube/region=mx/
aws s3 cp RUvideos.csv s3://de-aws-raw-data-eu/youtube/region=ru/
aws s3 cp USvideos.csv s3://de-aws-raw-data-eu/youtube/region=us/