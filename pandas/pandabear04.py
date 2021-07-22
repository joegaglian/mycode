#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Exploring using pandas to create graphs"""

import pandas as pd

def main():

    dataframe = pd.read_json("5movies.json")

    dataframe.to_csv("5movies_converted_to_csv")

if __name__ == "__main__":
    main()

