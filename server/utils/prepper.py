'''
data prep
'''

from models.intent import Intent

import glob
import pandas as pd

from utils.logger import CLogger
logger = CLogger('prepper')


def make_csv():
    logger.info('main')

    files = [f for f in glob.glob("data/Train/*.json")]
    # outfile = 'data/csv/intents.csv'
    outfile = 'data/csv/sample.csv'
    print(files)

    for index, fpath in enumerate(files):
        intent = Intent(fpath)
        intent.read_file()
        intent.info()
        if index == 0:
            header = True
        else:
            header = False
        intent.to_csv(header=header, outfile=outfile, sample=50)


def load_csv(fpath=None):
    fpath = fpath or 'data/csv/sample.csv'
    df = pd.read_csv(fpath)
    df.drop(['data'], axis=1, inplace=True)
    logger.info('df items: %s', len(df))
    return df
