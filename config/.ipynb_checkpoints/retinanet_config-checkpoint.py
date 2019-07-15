{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "\n",
    "BASE_PATH = 'dataset'\n",
    "ANNOT_PATH = os.path.sep.join([BASE_PATH, 'annotations'])\n",
    "IMAGES_PATH = os.path.sep.join([BASE_PATH, 'images'])\n",
    "\n",
    "TRAIN_TEST_SPLIT = 0.75\n",
    "\n",
    "TRAIN_CSV = os.path.sep.join([BASE_PATH, 'train.csv'])\n",
    "TEST_CSV = os.path.sep.join([BASE_PATH, 'test.csv'])\n",
    "\n",
    "CLASSES_CSV = os.path.sep.join([BASE_PATH, 'classes.csv'])\n",
    "\n",
    "OUTPUT_DIR = os.path.sep.join([BASE_PATH, 'predictions'])\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
