import logging
import os

import constants


class LogFactory:
    @staticmethod
    def make_log(name, file_name='main.log'):
        log = logging.getLogger(name)
        log.setLevel(logging.DEBUG)

        f = logging.Formatter(
            '[%(asctime)s] [%(levelname)-8s]  [%(message)s] [%(name)s:%(lineno)s - %(funcName)s()]',
            datefmt='%d-%m-%Y %H:%M:%S')
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console.setFormatter(f)
        log.addHandler(console)

        log_dir = os.path.join(constants.BASE_DIR, 'logs')

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        file = logging.FileHandler(os.path.join(log_dir, file_name))
        file.setLevel(logging.DEBUG)
        file.setFormatter(f)
        log.addHandler(file)

        return log
