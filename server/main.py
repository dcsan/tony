
from utils import prepper

from utils.logger import CLogger
logger = CLogger('main')


def compare():
    prepper.load_csv()


logger.info('start')
compare()
