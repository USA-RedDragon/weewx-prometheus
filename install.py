#!/usr/bin/env python

from weecfg.extension import ExtensionInstaller

__title__ = 'PromPush'
__version__ = '1.1.6'
__author__ = 'Tom Mitchell <tom@tom.org>'
__license__ = 'Apache License, Version 2.0'


def loader():
    return WeewxPromPushInstaller()


class WeewxPromPushInstaller(ExtensionInstaller):
    def __init__(self):
        super(WeewxPromPushInstaller, self).__init__(
            version=__version__,
            name=__title__,
            description='post weather data to prometheus pushgateway.',
            author='Tom Mitchell',
            author_email='tom@tom.org',
            restful_services='user.prompush.PromPush',
            files=[('bin/user', ['bin/user/prompush.py'])],
            config={
                'StdRESTful': {
                    'PromPush': {
                        'host': 'PUSH_GW_HOST',
                        'port': 'PUSH_GW_PORT',
                        'job': 'PROMETHEUS_JOB_NAME',
                        'instance': 'PROMETHEUS_INSTANCE_NAME'
                    }
                }
            },
        )
