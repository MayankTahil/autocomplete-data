# SQL Notes

## Login: 

```bash
mysql --host=[INSTANCE_IP] --user=root --password=[YOUR-PASSWORD]
```

## Create new Database

```SQL
CREATE DATABASE Products;
USE DATABASE Products;
CREATE TABLE IF NOT EXISTS Products (Name text) PRIMARY KEY (Name)
```

## Insert Data into table 

```SQL
INSERT INTO Products (Name) VALUES ('Cardinal');
```