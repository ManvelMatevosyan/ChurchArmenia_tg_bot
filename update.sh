#!/bin/bash
if [ -e ./ChurchArmenia_tg_bot/app/runner.py.lock ]
then
        echo "runner.py is running and locked"
        exit 1
fi

BAKNAME="ChurchArmenia_tg_bot_"$(date -d "today" +"%Y%m%d%H%M%S")
echo "BACKUP_NAME:"$BAKNAME
mv ./ChurchArmenia_tg_bot/ ./$BAKNAME/
git clone https://github.com/ManvelMatevosyan/ChurchArmenia_tg_bot.git
if [ -e ./$BAKNAME/app/data/statuses.json ]
then
        cp ./$BAKNAME/app/data/statuses.json ./ChurchArmenia_tg_bot/app/data/
else
        echo "Can't find old statuses.json in "$BAKNAME"/app/data/"
fi
echo "UPDATE FINISHED"

