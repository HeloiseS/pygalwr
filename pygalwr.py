"""
pygalwr - module

This contains a quick utility function to download the most up to date version of the Galactic WR
Star catalogue as a clean dataframe.

Catalogue location http://pacrowther.staff.shef.ac.uk/WRcat/index.php (P. Crowther)

Author: H. F. Stevance - hfstevance@gmail.com

Dependencies: Python 3.6, pandas
"""

import pandas as pd

CAT_LOC = 'http://pacrowther.staff.shef.ac.uk/WRcat/index.php'


def download_catalogue(save_to=None):
    """
    Downloads the most up-to-date version of the Galactic WR star catalogue

    Notes:
    ------
    This requires an internet connection

    Parameters
    ----------
    save_to : str, optional
        Path to location where the csv should be saved

    Returns
    -------
    if no path is provided, returns a pandas.DataFrame containing the catalogue.

    """
    cat = pd.read_html(CAT_LOC)[0]
    for column in cat.columns:
        cat[column] = cat[column].map(lambda x: x.rstrip('&nbsp'))

    if save_to is not None:
        if not isinstance(save_to,str):
            print('I was expecting the path to the download location be a string. I will try'
                  'converting it now.')
            try:
                save_to = str(save_to)
            except:
                # I know this is a pokemon exception, but I figured it wouldn't hurt in this part
                # of the code.
                print('It looks like I could not convert your path to a string.')
                return "\nPlease check your path and try again"

        try:
            cat.to_csv(save_to, index=False)
        except FileNotFoundError as error:
            print(error)
            print("\nIt looks like the path you provided is not valid. See the error above (python "
                  "traceback) for more information about what went wrong and try again.")
            return

        return "Successfully downloaded the catalogue to "+save_to

    return cat



