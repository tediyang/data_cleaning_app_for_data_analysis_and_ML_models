import pandas as pd

class Reader(object):
    def __init__(self, delimiter=None, header='infer', index_col=None, usecols=None, squeeze=None, \
        dtype=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0,\
        nrows=None, na_values=None, verbose=False, keep_date_col=False, compression='infer', \
        encoding=None, encoding_errors='strict', delim_whitespace=False, storage_options=None,  match='.+', \
        flavor = None, attrs = None, parse_dates = False, thousands = ',', decimal = '.', converters = None, \
        displayed_only = True):
        self.delimiter = delimiter
        self.header = header 
        self.index_col = index_col
        self.usecols = usecols
        self.squeeze = squeeze
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
        self.match = match 
        self.flavor = flavor
        self.attrs = attrs 
        self.parse_dates = parse_dates
        self.thousands = thousands
        self.decimal = decimal 
        self.converters = converters
        self.displayed_only = displayed_only
       

    def csv_reader(self):
        dataset = pd.read_csv('./', self.delimiter, self.header, self.index_col, self.usecols, self.squeeze, \
        self.dtype, self.true_values, self.false_values, self.skipinitialspace, self.skiprows, self.skipfooter,\
        self.nrows, self.na_values, self.verbose, self.keep_date_col, self.compression, \
        self.encoding, self.encoding_errors, self.delim_whitespace, self.storage_options)
        return dataset

    def table_reader(self):
        dataset = pd.read_table('./', self.delimiter, self.header, self.index_col, self.usecols, self.squeeze, \
        self.dtype, self.true_values, self.false_values, self.skipinitialspace, self.skiprows, self.skipfooter,\
        self.nrows, self.na_values, self.verbose, self.keep_date_col, self.compression, \
        self.encoding, self.encoding_errors, self.delim_whitespace, self.storage_options)
        return dataset

    def html_reader(self):
        dataset = pd.read_html('./',  self.match, self.flavor, self.header, self.index_col, self.skiprows, \
        self.attrs, self.parse_dates, self.thousands, self.encoding, self.decimal, self.converters, self.na_values, self.displayed_only)
        return dataset

    def json_reader(self):
        dataset = pd.read_json('./',)
        return dataset

    def excel_reader(self):
        dataset = pd.read_excel('./',)
        return dataset


