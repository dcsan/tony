
from utils import prepper
from nlp.compare import Compare

from utils.logger import CLogger
logger = CLogger('main')


def compare():
    # prepper.load_csv()
    comp = Compare()
    comp.prepare()


logger.info('start')
compare()
