import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Contract_management_system.settings")  # project_name 项目名称
django.setup()
from CMSapp import models

import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

# 自动判断合同过期
def contractTimeout():
    contractStatelist = models.contract_state.objects.filter(type__lt=5)
    for contractState in contractStatelist:
        if contractState.conid.endtime < datetime.date.today():
            contractState.type = 6
            contractState.save()
    print('Tick! The time is: %s' % datetime.datetime.now())


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(contractTimeout, 'cron', hour=0, minute=1)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
