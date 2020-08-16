# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## Blood Gluse Test Strips Price Information

# A user has gotten in touch as they require price information on blood glucose test strips for analysis they want to carry out. Our [OpenPrescribing drug tariff browser/viewer](https://openprescribing.net/tariff/) currently only support part 8 whereas test strips are located in the device section. [Prescribing patterns of blood glucose test strips](https://openprescribing.net/chemical/0601060D0/) can be viewed on OpenPrescribing.
#
# However on our price per unit tool we do incoproarte blood glucose test strips so we do have the price paid (accepted slightly different to drug tariff) in our database. The [PPU for blood glucose test strips and possible savings can be seen here](https://openprescribing.net/national/england/0601060D0AAA0A0/price-per-unit/?date=2020-05-01).
#
# In this notebook we will extract the median price paid for the user and export to csv for their own (and others) analysis.
#
#

#import libraries
import pandas as pd
import numpy as np
import os
from ebmdatalab import bq, maps, charts #possibly do graphs at later stage.

#this sets £ and pence properly
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# # SQL

# +
sql = '''
SELECT
ppu.date,
ppu.bnf_code,
dmd.nm,
ppu.median_price_per_unit
FROM
ebmdatalab.measures.vw__median_price_per_unit as ppu
LEFT JOIN
ebmdatalab.dmd.amp as dmd
ON
ppu.bnf_code = dmd.bnf_code
WHERE 
ppu.bnf_code LIKE '0601060D0%'
ORDER BY
ppu.bnf_code,
ppu.date
'''




df_median_ppu_bgt = bq.cached_read(sql, csv_path=os.path.join('..','data','df_median_ppu_bgt.csv'))
df_median_ppu_bgt.head(50)
