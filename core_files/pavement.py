from paver.easy import task, sh, consume_nargs
from paver.setuputils import setup
import multiprocessing

setup(
    name="Python (Web) Automation",
    version="0.0.1",
    author="Thiago Werner",
    author_email="thiago.werner@arctouch.com",
    description=("Python (Web) Automation: Python + Behave + Selenium"),
    license="ArcTouch",
    keywords="brief appium structure",
    url="https://github.com/arctouch/python-automation",
    packages=['features']
)


def run_behave_test(browsers, task_id=0):
    sh('TASK_ID=%s behave ./features -D browser=\"%s\"' % (task_id, browsers))


@task
@consume_nargs()
def run(args):
    if args[0] in ('single', 'local'):
        # TODO
        # run_behave_test(args[0], args[0])
        pass
    else:
        jobs = []
        browsers = list(args[1:])
        separator = ","
        browsers = separator.join(browsers)
        for i in range(len(args[1:])):
            p = multiprocessing.Process(target=run_behave_test, args=(browsers.split(',')[i], i))
            jobs.append(p)
            p.start()
