#!/bin/bash
# call_by_crontab.sh
# cron
# */5 0 * * * /Users/admin/MoninterSshMaps/call_by_crontab.sh

source /Users/admin/MoninterSshMaps/venv/bin/activate
cd /Users/admin/MoninterSshMaps
python3 call_by_crontab.py


