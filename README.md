Download the Galactic WR star Catalogue with pygalwr
---

This module contains a quick utility function to download the most up to date version of the Galactic WR
Star catalogue as a clean dataframe.

## Quick Start

- Just getting the catalogue as a dataframe
```bash
>>> from pygalwr import download_catalogue as dnld_cat
>>> catalogue_df = dnld_cat()
>>> type(catalogue_df)
<class 'pandas.core.frame.DataFrame'>
>>> catalogue_df.shape
(662, 30)

```

- Saving the catalogue locally

```bash
from pygalwr import download_catalogue as dnld_cat
>>> catalogue_df = dnld_cat(save_to='WR_CAT')
```


**Catalogue location:** http://pacrowther.staff.shef.ac.uk/WRcat/index.php 

**Catalogue owner:** P. Crowther

**Author:** H. F. Stevance - hfstevance@gmail.com

**Dependencies:** pandas

**Tested for Python3.6**
