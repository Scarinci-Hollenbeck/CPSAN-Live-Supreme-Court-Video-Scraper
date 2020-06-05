from crontab import CronTab

with CronTab(tabfile='logs/crontab.tab') as cron:
  job = cron.new(command='echo hello_world')
  job.minute.every(1)
print('cron.write() was just executed')