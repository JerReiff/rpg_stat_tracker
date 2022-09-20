#/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

if [ -z "$1" ] 
then 
    BUILD_SCRIPT="$SCRIPT_DIR/build.sql" 
else 
    BUILD_SCRIPT=$1 
fi


echo "Mysql Username:"
read USERNAME
stty -echo
printf "Mysql Password: "
read PASSWORD
stty echo
printf "\n\n\n"

mysql --user=$USERNAME --password=$PASSWORD < "$SCRIPT_DIR/test_setup.sql" &&
echo "Teardown of rpg_stat_tracker_test database complete."
echo "Building the database..."
mysql --user=$USERNAME --password=$PASSWORD rpg_stat_tracker_test <  "$BUILD_SCRIPT" &&
echo "Database built!"
echo "Running test..."
mysql --user=$USERNAME --password=$PASSWORD rpg_stat_tracker_test < "$SCRIPT_DIR/test.sql" &&
echo "Success, maybe?"