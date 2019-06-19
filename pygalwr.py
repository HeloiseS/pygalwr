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
    pandas.DataFrame containing the catalogue

    """
    cat = pd.read_html(CAT_LOC)[0]
    for column in cat.columns:
        cat[column] = cat[column].map(lambda x: x.rstrip('&nbsp'))

    if save_to:
        #TODO: add assertion that the path is sensible, if not, raise a warning and give default
        # name.
        cat.to_csv('save_to')

    return cat



