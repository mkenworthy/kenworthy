"""
kenworthy
=========


Provides
	kepler3 - Kepler orbit routines
	exorings3 - calculations and generating light curves for transiting disks and ring systems
	isocosa - generating nets of isocosahedra distributed on a sphere
	tag_plot - labelling up matplotlib plots
"""

from . import kepler3
from . import exorings3
from . import isocosa
from . import tag_plot

import os

__version__ = '0.1.2'
__author__ = 'Matthew Kenworthy'
__credits__ = 'Leiden Observatory'
