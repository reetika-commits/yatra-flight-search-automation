class Utils:
    def assertListItemtext(self,list,expected):
        actual_stops=[item.text.strip() for item in list if item.text.strip()!=""]
        for stop in actual_stops:            
            assert stop==expected, f"Stop is {stop} and Asseert is fail"
            


