import os
import gzip

class Table(object):
    """ Represents a table as a list of objects. """

    def __init__(self):
        self.records = []



    def __len__(self):
        return len(self.records)



    def ReadFile(self, data_dir, filename, fields, constructor, n=None):
        """ Reads a compressed data file builds one object per record.

        Args:
            data_dir: string directory name
            filename: string name of the file to read

            fields: sequence of (name, start, end, cast) tuples specifying
            the fields to extract

            constructor: callable that makes an object for the record
        """
        filename = os.path.join(data_dir, filename)

        if filename.endswith('gz'):
            fp = gzip.open(filename)
        else:
            fp = open(filename)

        for i, line in enumerate(fp):
            if i == n:
                break
            record = self.MakeRecord(line, fields, constructor)
            self.AddRecord(record)
        fp.close()



    def MakeRecord(self, line, fields, constructor):
        """Scans a line and returns an object with the appropriate fields.

        Args:
            line: string line from a data file

            fields: sequence of (name, start, end, cast) tuples specifying
            the fields to extract

            constructor: callable that makes an object for the record.

        Returns:
            Record with appropriate fields.
        """
        obj = constructor()
        for (field, start, end, cast) in fields:
            try:
                s = line[start - 1:end]
                val = cast(s)
            except ValueError:
                # If you are using Visual Studio, you might see an
                # "error" at this point, but it is not really an error;
                # I am just using try...except to handle not-available (NA)
                # data.  You should be able to tell Visual Studio to
                # ignore this non-error.
                val = 'NA'
            setattr(obj, field, val)
        return obj



    def AddRecord(self, record):
        """Adds a record to this table.

        Args:
            record: an object of one of the record types.
        """
        self.records.append(record)



    def ExtendRecords(self, records):
        """Adds records to this table.

        Args:
            records: a sequence of record object
        """
        self.records.extend(records)



    def Recode(self):
        """Child classes can override this to recode values."""
        pass