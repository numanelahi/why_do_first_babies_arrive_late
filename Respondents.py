from Table import Table

class Resopndents(Table):
    """ Represents the respondent table. """

    def ReadRecords(self, data_dir='.', n=None):
        filename = self.GetFilename()
        self.ReadFile(data_dir, filename, self.GetFields(), Respondent, n)
        self.Recode()



    def GetFilename(self):
        return '2002FemResp.dat'



    def GetFields(self):
        """Returns a tuple specifying the fields to extract.

        The elements of the tuple are field, start, end, case.

                field is the name of the variable
                start and end are the indices as specified in the NSFG docs
                cast is a callable that converts the result to int, float, etc.
        """
        return [
            ('caseid', 1, 12, int),
        ]