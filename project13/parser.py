from xml.etree import ElementTree as ET
from os import getcwd

class FileParser(object):

    def __init__(self, data_stream):
        self.filepath = getcwd() + "/output"
        self.data_stream = data_stream

    def write_file(self):
        with open(self.filepath + "/newfile.txt", 'w') as f:
            f.write(self.data_stream)
        return self


class XmlFile(FileParser):

    def __init__(self, data_stream):
        super(XmlFile, self).__init__(data_stream)
        self.extension = ".xml"

    def write_file(self):
        with open(self.filepath + "/newfile" + ".xml", 'w') as f:
            f.write(self.data_stream)
        return self
