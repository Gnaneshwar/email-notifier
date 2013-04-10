#EMail Notifier

A simple python script that checks your gmail using gmail atom feed and shoots a GNOME notification if any unread mails are
found.
Add it to cron so that it checks your mail periodially. Make sure to add the DISPLAY environment variable while adding it to cron. For ex. add "*/5 * * * * env DISPLAY=:0.0 /path/to/file/email.py"  to cron to run the script every 5 minutes.
