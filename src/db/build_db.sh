#! /bin/sh -
PROGNAME=$0

usage() {
  cat << EOF >&2
Usage: $PROGNAME [-r]

-r <rebuild>: Build a new database called "rpg_stat_tracker". WIPES ANY DATABASES OF THAT NAME!
EOF
  exit 1
}

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

WIPE="false"
PROD="false"
while getopts ":rp" o; do
  case $o in
    (r) WIPE="true";;
    (p) PROD="true";;
    (*) usage
  esac
done
shift "$((OPTIND - 1))"


echo "Mysql Username:"
read USERNAME

stty -echo
printf "Password: "
read PASSWORD
stty echo
printf "\n"

if "$PROD"
then
    DB_NAME="rpg_stat_tracker"
else 
    DB_NAME="rpg_stat_tracker_test"
fi

if "$WIPE"
then
    echo "Creating a database with the name '$DB_NAME'..."
    echo "This will destroy any existing databases of this name"
    SQL_Q="DROP DATABASE IF EXISTS $DB_NAME; CREATE DATABASE $DB_NAME;"
    mysql --user=$USERNAME --password=$PASSWORD -e "$SQL_Q" &&
    echo "Database created!"
fi
echo "Building database."
mysql --user=$USERNAME --password=$PASSWORD $DB_NAME < "$SCRIPT_DIR/build.sql" &&
echo "Database built!"