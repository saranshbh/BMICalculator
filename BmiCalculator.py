# from models.BmiCalculator import BmiCalculator
from services.BmiCalculatorService import calculateBMI, categorize, countOverweight
from utils.BmiCalculatorUtils import getDataFrame
# from typing import List
from constants.BmiCalculatorConstants import *
import os
from setup import import_or_install


if __name__ == '__main__':
    print(TASK_STARTED)
    # Using BmiCalculatorService and BmiCalculatorUtils to perform all our functions.

    # We are using 2 major libraries included in this
    import_or_install('pandas')
    import_or_install('numpy')

    import pandas as pd
    import numpy as np

    df = pd.DataFrame()

    # Loading all files and storing the json file into a dataframe for further processing.
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    for f in files:
        if '.json' in f:
            df = getDataFrame(f)

    df = calculateBMI(df)
    df = categorize(df)

    # Printing the final DataFrame
    print(df.head())


    print('Total Overweight People: ')
    print(countOverweight(df))
    print(TASK_ENDED)

else:
    raise Exception("Incorrect Execution")


