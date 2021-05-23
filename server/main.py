import glob

from models.intent import Intent

from utils.logger import CLogger
logger = CLogger('intent')


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


make_csv()
