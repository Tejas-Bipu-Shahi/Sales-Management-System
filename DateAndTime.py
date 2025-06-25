from datetime import datetime
'''=======================================================For Date And Time ============================================================='''
year = str(datetime.now().year)
month = str(datetime.now().month)
day = str(datetime.now().day)
hour = str(datetime.now().hour)
minute = str(datetime.now().minute)

def returnDateandTime():
    """
    Returns the current date and time in a specific formatted string.

    This function combines the current year, month, day, hour, and minute into a string 
    representing the date and time in the format: 'YYYY_MM_DD_HH_MM'.

    Parameters:
    None

    Returns:
    str: A string representing the current date and time in the format 'YYYY_MM_DD_HH_MM'.

    Raises:
    NameError: If the variables `year`, `month`, `day`, `hour`, or `minute` are not defined.

    """
    realDate = year +"_"+ month +"_"+ day
    realTime = hour + "_" + minute
    return realDate +"_"+ realTime

'''======================================================Date and time work ends ========================================================='''
