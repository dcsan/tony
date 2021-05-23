import logging
import json

# logging.basicConfig(format='[%(module)s]\t %(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(message)s', level=logging.DEBUG)


class CLogger():

    def __init__(self, name):
        self.name = name

    def json(self, msg, blob):
        # logging.info('arg count %s', len(args))
        # logging.info('args %s', args)
        # msg = args[0]
        msg = f'[{self.name}] {msg}'
        # print(msg)

        try:
            blob = json.dumps(blob, indent=4)
            logging.info(f'{msg} \n=> %s', blob)
        except BaseException as err:
            logging.warning('err %s', err)
            logging.info(f'{msg}=> \n %s', blob)

    def info(self, *args):
        logging.info(*args)
