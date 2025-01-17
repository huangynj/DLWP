#
# Copyright (c) 2019 Jonathan Weyn <jweyn@uw.edu>
#
# See the file LICENSE for your rights.
#

"""
Test retrieval and processing of ERA5Reanalysis data.
"""

from DLWP.data import ERA5Reanalysis

variables = ['geopotential']
levels = [300, 700]

era = ERA5Reanalysis(root_directory='/home/disk/wave2/jweyn/Data/ERA5', file_id='era5_2deg_3h_')
era.set_variables(variables)
era.set_levels(levels)

era.retrieve(variables, levels, request_kwargs={'grid': [2., 2.]}, verbose=True)

era.open()
print(era.Dataset)
era.close()
