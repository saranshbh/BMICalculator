
from constants.BmiCalculatorConstants import *
from queue import Queue
import random
# from models.BmiCalculator import BmiCalculator
# from services.interface.IBmiCalculator import IBmiCalculator


class BmiCalculatorService:

    def calculateBMI(self, df):

        # Vectorization to calculate the bmi given weight and height

        df['bmi'] = df['WeightKg'] / (df['HeightCm'] / 100) ** 2

        return df

    def categorize(self, df):

        # categorize with importing a few constants predefined in the constants file

        import numpy as np

        condition = [(df['bmi'] < 18.5),
                     (df['bmi'] >= 18.5) & (df['bmi'] < 25),
                     (df['bmi'] >= 25) & (df['bmi'] < 30),
                     (df['bmi'] >= 30) & (df['bmi'] < 35),
                     (df['bmi'] >= 35) & (df['bmi'] < 40),
                     (df['bmi'] >= 40)
                     ]

        df['category'] = np.select(condition, categories)
        df['health_risk'] = np.select(condition, health_risk)

        return df

    def countOverweight(self, df):

        # Finally, calculating the number of overweight after performing the categorization over all values.

        return df.category.value_counts()['Overweight']



