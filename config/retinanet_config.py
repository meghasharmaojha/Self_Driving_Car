import os

BASE_PATH = 'dataset'
ANNOT_PATH = os.path.sep.join([BASE_PATH, 'annotations'])
IMAGES_PATH = os.path.sep.join([BASE_PATH, 'images'])

TRAIN_TEST_SPLIT = 0.75

TRAIN_CSV = os.path.sep.join([BASE_PATH, 'train.csv'])
TEST_CSV = os.path.sep.join([BASE_PATH, 'test.csv'])

CLASSES_CSV = os.path.sep.join([BASE_PATH, 'classes.csv'])

OUTPUT_DIR = os.path.sep.join([BASE_PATH, 'predictions'])
