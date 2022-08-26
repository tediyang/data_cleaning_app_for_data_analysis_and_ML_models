from urllib.parse import parse_qsl
from xml.dom.pulldom import parseString
import pandas as pd

class Reader(object):
    def __init__(self, delimiter=None, header='infer', index_col=None, usecols=None, squeeze=None, \
        dtype=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0,\
        nrows=None, na_values=None, verbose=False, keep_date_col=False, compression='infer', \
        encoding=None, encoding_errors='strict', delim_whitespace=False, storage_options=None):
        self.delimeter = delimiter
        self.header = header 
        self.index_col = index_col
        self.usecols = usecols
        self.squeze = squeeze
        self.dtype = dtype
        self.true_values = true_values
        self.false_values = false_values
        self.skipinitialspace = skipinitialspace
        self.skiprows = skiprows
        self.skipfooter = skipfooter
        self.nrows = nrows 
        self.na_values = na_values
        self.verbose= verbose
        self.keep_date_col = keep_date_col
        self.compression = compression 
        self.encoding = encoding
        self.encoding_errors = encoding_errors
        self.delim_whitespace = delim_whitespace
        self.storage_options = storage_options
       

class Csv_reader(Reader):
    pass
