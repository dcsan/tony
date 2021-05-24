from nlp.compare import Compare
from utils import prepper
from utils.logger import CLogger
logger = CLogger('test_compare')


def test_compare():
    # df = prepper.load_csv()
    # items = len(df)
    # logger.info('columns: %s', df.columns)
    comp = Compare()
    comp.prepare()
