import logging
import inspect
import yaml
from utilities import excel_utils
import pandas as pd


#File Paths
yaml_file_path="testdata/yatra_testdata.yaml"
xl_file_path="testdata/excel_testdata.xlsx"
csv_file_path="testdata/csv_testdata.csv"

#reusable methods
class Utils:
    def assertListItemtext(self,list,expected):
        if expected=="1":stops="1 Stop"
        elif expected=="2":stops="2 Stops"
        elif expected=="0":stops="Non Stop"
        actual_stops=[item.text.strip() for item in list if item.text.strip()!=""]
        for stop in actual_stops:            
            assert stop==stops, f"Stop is {stop} and Asseert is fail"

    @staticmethod        
    def custom_logger(loglevel=logging.DEBUG):
        # set class or method name from where this logger is called
            logger_name=inspect.stack()[1][3]
        #create logger
            logger=logging.getLogger(logger_name)
            logger.setLevel(loglevel)
        #create console handler or file handler and set the log lever

            file_handler=logging.FileHandler("utilities/automation.log")
        #create formator, how you want you log to appear

            file_formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',datefmt='%d-%m-%y %H:%M %p')
        #add formatter tp consols handler or file handler

            file_handler.setFormatter(file_formatter)
        #Add console handler or file handler to logger

            logger.addHandler(file_handler)
            return logger
        #log massage
    
    @staticmethod
    def read_yaml():
        with open(yaml_file_path, 'r') as file:
             yaml_containt=yaml.safe_load(file)
        return  yaml_containt
    
    @staticmethod
    def read_excel():
        sheet = "Sheet1"
        test_data = []
        rows =excel_utils.get_row_count_xl(xl_file_path,sheet)
        for r in range(2, rows + 1):
            departurecity = excel_utils.read_data(xl_file_path,sheet, r, 1)
            arrivalcity = excel_utils.read_data(xl_file_path,sheet, r, 2)
            traveldate = excel_utils.read_data(xl_file_path,sheet, r, 3)
            stops= excel_utils.read_data(xl_file_path,sheet, r, 4)

            test_data.append({
                "depart_from":departurecity,
                "going_to":arrivalcity,
                "travel_date":traveldate,
                "stops":stops
           } )
        print(test_data)
        return test_data
    
    @staticmethod
    def read_csv():
        test_data=pd.read_csv(csv_file_path)
        return test_data.to_dict(orient="records")