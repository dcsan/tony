import csv
import json
import random

# import logging
# from google.cloud import bigquery
# client = bigquery.Client()

from utils.logger import CLogger
logger = CLogger('intent')

'''
parses incoming data to a csv file with intent,utterance,data

incoming:

{
  "IntentName": [
    {
      "data": [
        {
          "text": "Add another "
        },
        {
          "text": "song",
          "entity": "music_item"
        },
        {
          "text": " to the "
        },
        {
          "text": "Cita Romantica",
          "entity": "playlist"
        },
        {
          "text": " playlist. "
        }
      ]
    },

'''


class Intent:

    def __init__(self, fpath):
        '''takes a file path to a json file'''
        name = fpath.split('/').pop()
        name = name.replace('.json', '')
        self.fpath = fpath
        self.name = name
        pass

    def read_file(self):
        with open(self.fpath) as file:
            raw = json.load(file)
            logger.info('read %s', self.fpath)

            name = list(raw.keys()).pop()
            # self.name = name
            logger.info('intent %s', name)
            rows = []
            for item in raw[name]:
                data = item['data']
                texts = [elem['text'] for elem in data]
                text = ''.join(texts)
                row = {
                    'utterance': text,
                    'intent': name,
                    'data': data,
                    # 'items': items
                }
                rows.append(row)

            self.rows = rows
            # logger.info('items %s', len(items))

    def info(self):
        logger.info(' name: %s', self.name)
        logger.info('rows: %s', len(self.rows))
        logger.json('row0', self.rows[0])

    def sample(self, count=50):
        return random.sample(self.rows, count)

    def to_csv(self, header=False, outfile=None, mode='a', sample=None):
        '''dump rows to a csv file'''
        outfile = outfile or f'data/csv/{self.name}.csv'
        fieldnames = ['intent', 'utterance', 'data']

        rows = []
        if sample:
            rows = self.sample(count=sample)
        else:
            rows = self.rows

        with open(outfile, mode=mode) as csv_file:
            writer = csv.DictWriter(
                csv_file, fieldnames=fieldnames, extrasaction='ignore')
            if header:
                writer.writeheader()

            for row in rows:
                writer.writerow(row)
