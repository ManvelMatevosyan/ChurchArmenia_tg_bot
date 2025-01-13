#!/bin/bash
if [ -e ./ChurchArmenia_tg_bot/app/runner.py.lock ]
then
        echo "runner.py is running and locked"
        exit 1
fi


cd ./ChurchArmenia_tg_bot/app/
python3.10 ./runner.py

cd ../../
echo "EXITED START.SH"
