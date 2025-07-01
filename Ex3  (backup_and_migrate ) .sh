#!/bin/bash

# Configuration
MYSQL_USER="root"
MYSQL_DB="kavindb"
POSTGRES_USER="kavin"
POSTGRES_DB="kavindb"
TABLE_NAME="employees"
DUMP_FILE="employees_data.sql"

# Step 1: Export from MySQL
echo "Exporting data from MySQL..."
mysqldump -u $MYSQL_USER -p $MYSQL_DB $$TABLE_NAME \
  --no-create-db --skip-add-drop-table > $DUMP_FILE

echo "Cleaning dump file (removing backticks)..."
sed -i 's/`//g' $DUMP_FILE

# Step 2: Import into PostgreSQL
echo "Importing data into PostgreSQL..."
psql -U $POSTGRES_USER -d $POSTGRES_DB -f $DUMP_FILE

echo "Migration complete. Run verification queries manually to ensure data integrity."