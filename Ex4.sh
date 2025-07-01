#!/bin/bash

# ------------------------------------------
# Oracle Backup and Restore Script (Shell)
# ------------------------------------------

# Configuration
ORACLE_USER="kavin"
ORACLE_PASSWORD="kavin123"
ORACLE_SID="ORCL"
DIRECTORY_NAME="dpdir"
DUMPFILE="emp_backup.dmp"
LOGFILE_EXPORT="emp_export.log"
LOGFILE_IMPORT="emp_restore.log"
TABLE_NAME="kavin.employees"
DUMP_PATH="C:\\oracle_backups"   # Use double backslashes for Windows path

# STEP 1: Create Directory Object in Oracle (Run in SQL*Plus manually)
echo "⚠️  Please ensure the Oracle directory object exists with:"
echo "   CREATE OR REPLACE DIRECTORY dpdir AS '$DUMP_PATH';"
echo "   GRANT READ, WRITE ON DIRECTORY dpdir TO $ORACLE_USER;"
echo

# STEP 2: Export the table
echo "📤 Exporting table $TABLE_NAME to $DUMPFILE..."
expdp $ORACLE_USER/$ORACLE_PASSWORD@$ORACLE_SID DIRECTORY=$DIRECTORY_NAME \
  DUMPFILE=$DUMPFILE LOGFILE=$LOGFILE_EXPORT TABLES=$TABLE_NAME

# STEP 3: Simulate failure (optional)
echo "⚠️  You can drop the table manually to simulate failure:"
echo "   DROP TABLE $TABLE_NAME;"

# STEP 4: Import the table back
echo "📥 Importing table $TABLE_NAME from $DUMPFILE..."
impdp $ORACLE_USER/$ORACLE_PASSWORD@$ORACLE_SID DIRECTORY=$DIRECTORY_NAME \
  DUMPFILE=$DUMPFILE LOGFILE=$LOGFILE_IMPORT TABLES=$TABLE_NAME

# STEP 5: Verification
echo "✅ To verify, run the following in SQL*Plus:"
echo "   SELECT COUNT(*) FROM $TABLE_NAME;"
echo "   SELECT * FROM $TABLE_NAME WHERE ROWNUM <= 10;"
