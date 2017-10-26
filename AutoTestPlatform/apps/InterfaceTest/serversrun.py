from AutoTestPlatform.apps.tools import plantool


def run(scheduler):
    scheduler.start()
    plantool.start_scheduler(scheduler)
