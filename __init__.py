import datetime
def extract_format(date_column):
    list_date_formats = ["yyyy-mm-dd", "dd-mm-yyyy", "mm/dd/yyyy", "%m/%d/%Y", "%m/%d/%y", "%d/%m/%Y", "%d/%m/%y", "%d-%m-%Y", 
                         "%d-%m-%y", "%m-%d-%Y", "%m-%d-%y", "%Y-%m-%d", "%f/%e/%Y", "%f/%e/%y", "%e/%f/%Y", "%e/%f/%y", 
                         "%f-%e-%Y", "%f-%e-%y", "%e-%f-%Y", "%e-%f-%y", "%b %e, %Y", "%B %e, %Y", "%b %d, %Y", "%B %d, %Y", 
                         "%Y-%m-%d %H:%M:%S", "%H:%M:%S", "%Y-%m-%d %I:%M:%S %p","%b %Y", "%Y-%m-%d %I:%M:%S %p", "%b %d, %Y", "%b %Y"]

    for date_format in list_date_formats:
        succeed = True
        for date in date_column:
            if(date != None):
                try: 

                    datetime.datetime.strptime(date, date_format)
                except ValueError:
                    succeed = False
                    break
            else:
                continue
        if(succeed == True):
            print("the date format of this column is : " + date_format)
            return(date_format)
            break
        else:
            continue
    return "failed extraction"