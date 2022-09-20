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
while getopts r o; do
  case $o in
    (r) WIPE="true";;
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

if "$WIPE"
then
    echo "Creating a database with the name 'rpg_stat_tracker'..."
    echo "This will destroy any existing databases of this name"
    mysql --user=$USERNAME --password=$PASSWORD < "$SCRIPT_DIR/rebuild.sql" &&
    echo "Database created!"
fi
echo "Building database."
mysql --user=$USERNAME --password=$PASSWORD rpg_stat_tracker < "$SCRIPT_DIR/build.sql" &&
echo "Database built!"