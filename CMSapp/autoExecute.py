import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Contract_management_system.settings")  # project_name 项目名称
django.setup()
from CMSapp import models

import datetime

from apscheduler.schedulers.blocking import BlockingScheduler


def contractTimeout():
    contractStatelist = models.contract_state.objects.all()
    for contractState in contractStatelist:
        if contractState.conid.endtime < datetime.date.today():
            contractState.type = 6
            contractState.save()
    print('Tick! The time is: %s' % datetime.datetime.now())


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(contractTimeout, 'cron', hour=14, minute=30)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
