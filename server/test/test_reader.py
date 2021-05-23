from utils import prepper
from utils.logger import CLogger
logger = CLogger('test_compare')


def test_compare():
    df = prepper.load_csv()
    items = len(df)
    logger.info('columns: %s', df.columns)

    assert items == 350, 'wrong length'
    assert len(df.columns) == 2, 'two cols'
