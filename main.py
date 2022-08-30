import pandas as pd

class Reader(object):
    def __init__(self, delimiter=None, header='infer', index_col=None, usecols=None, squeeze=None, \
        dtype=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0,\
        nrows=None, na_values=None, verbose=False, keep_date_col=False, compression='infer', \
        encoding=None, encoding_errors='strict', delim_whitespace=False, storage_options=None,  match='.+', \
        flavor = None, attrs = None, parse_dates = False, thousands = ',', decimal = '.', converters = None, \
        displayed_only = True, orient=None, typ='frame', convert_axes=None, convert_dates=True, keep_default_dates=True, \
        numpy=False, precise_float=False, date_unit=None, lines=False, chunksize=None, sheet_name=0, names=None, engine=None,\
        keep_default_na=True, na_filter=True, date_parser=None, comment=None, convert_float=None, mangle_dupe_cols=True):
        
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
        self.convert_axes = convert_axes
        self.convert_dates = convert_dates
        self.keep_default_dates = keep_default_dates
        self.numpy = numpy
        self.precise_float = precise_float
        self.date_unit = date_unit
        self.lines = lines
        self.chunksize = chunksize
        self.orient = orient
        self.typ = typ
        self.sheet_name = sheet_name
        self.names = names
        self.engine = engine 
        self.keep_default_na = keep_default_na
        self.na_filter = na_filter
        self.date_parser = date_parser
        self.comment = comment
        self.convert_float = convert_float
        self.mangle_dupe_cols = mangle_dupe_cols


       

    def csv_reader(self, file):
        dataset = pd.read_csv(file, self.delimiter, self.header, self.index_col, self.usecols, self.squeeze, \
        self.dtype, self.true_values, self.false_values, self.skipinitialspace, self.skiprows, self.skipfooter,\
        self.nrows, self.na_values, self.verbose, self.keep_date_col, self.compression, \
        self.encoding, self.encoding_errors, self.delim_whitespace, self.storage_options)
        return dataset

    def table_reader(self, file):
        dataset = pd.read_table(file, self.delimiter, self.header, self.index_col, self.usecols, self.squeeze, \
        self.dtype, self.true_values, self.false_values, self.skipinitialspace, self.skiprows, self.skipfooter,\
        self.nrows, self.na_values, self.verbose, self.keep_date_col, self.compression, \
        self.encoding, self.encoding_errors, self.delim_whitespace, self.storage_options)
        return dataset

    def html_reader(self, file):
        dataset = pd.read_html(file,  self.match, self.flavor, self.header, self.index_col, self.skiprows, \
        self.attrs, self.parse_dates, self.thousands, self.encoding, self.decimal, self.converters, self.na_values, self.displayed_only)
        return dataset

    def json_reader(self, file):
        dataset = pd.read_json(file, self.orient, self.typ, self.dtype, self.convert_axes, self.convert_dates, \
        self.keep_default_dates, self.numpy, self.precise_float, self.date_unit, self.encoding, self.encoding_errors,\
        self.lines, self.chunksize, self.compression, self.nrows, self.storage_options)

        return dataset

    def excel_reader(self, file):
        # header and thousands are different for excel reader.
        dataset = pd.read_excel(file, self.sheet_name, self.header, self.names, self.index_col, self.usecols, self.squeeze, \
        self.dtype, self.engine, self.converters, self.true_values, self.false_values, self.skiprows, self.nrows, self.na_values,\
        self.keep_default_na, self.na_filter, self.verbose, self.parse_dates, self.date_parser, self.thousands, self.decimal, \
        self.comment, self.skipfooter, self.convert_float, self.mangle_dupe_cols, self.storage_options)

        return dataset


