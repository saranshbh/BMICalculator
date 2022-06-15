from queue import Queue

# import pandas as pd

from constants.BmiCalculatorConstants import *
from collections import OrderedDict

class BmiCalculatorUtils:

    def getDataFrame(self, filename):

        import pandas as pd

        ## Change file location.

        bmi = pd.read_json(filename)

        return bmi


