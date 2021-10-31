"""
Christerpher Hunter
Lab 15: Rain Data

Download or use requests to get one of these files. The two columns that are
most important are the date and the daily total. The simplest representation
of this data is a list of tuples, but you may also use a list of dictionaries,
or a list of instances of a custom class.
"""

from requests import get
from pathlib import Path
from colorama import Fore as F
import pandas as pd


R = F.RESET


class Data:

    def __init__(self, url=None):

        self.url = 'https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain'
        self.file = str()

    def grab_data(self) -> None:
        """Grab the data from a website"""

        self.file = Path("rain_dat.txt")
        if not self.file.exists():
            response = get(self.url)
            with open(self.file, "w") as f_write:
                f_write.write(response.text)
        else:
            print(f"\n{F.YELLOW}DATA ALREADY MIGRATED{R}\n")

    def get_data(self) -> list:
git
        df = pd.read_csv(self.file, sep=" ")
        
        return df


def main() -> None:

    raining = Data()
    raining.grab_data()

    print(raining.get_data()[3])


if __name__ == "__main__":
    main()
