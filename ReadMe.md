# Overview 

The data being put into the Cloud SQL DB is expected to be in a JSON file which holds a list of obejcts that have an key attribute of `name`. The values for the key `name` are populated in the SQL DB `Products` within the `Products` table in the single column `Name`. 

# Known inefficiencies: 

* The target DB is expected to have explicit names
* The single `Name` can have duplicate entries
* Each item is a SQL commit. Batch commits should be done to increase efficiency and speed. 

# Build and Run this service

```
docker build -t data-dump .
docker run -it --name=data-dumper --rm -e HOST=sql.host.com -e USER=root -e PASS=PASSWORD data-dump
```