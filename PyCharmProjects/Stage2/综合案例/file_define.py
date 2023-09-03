from data_define import Record
import json
class FileReader:
    def read_data(self):
        pass

class TextFileReader(FileReader):
    def __init__(self,path):
        self.path = path

    def read_data(self):
        f = open(self.path,'r',encoding='UTF-8')
        record_list = []
        for line in f.readlines():
            data_list = line.strip().split(',')
            record = Record(data_list[0],data_list[1],data_list[2],data_list[3])
            record_list.append(record)
        f.close()
        return record_list

class JsonFileReader(FileReader):
    def __init__(self,path):
        self.path = path

    def read_data(self):
        f = open(self.path,'r',encoding='UTF-8')
        record_list = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"],data_dict["order_id"],data_dict["money"],data_dict["province"])
            record_list.append(record)
        f.close()
        return record_list

