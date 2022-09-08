
def add_time(start, duration, day_of_week=False):

  #Defining variables
  days_of_the_week_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3,   "friday": 4, "saturday": 5, "sunday": 6}

  days_of_the_week_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",     "Saturday", "Sunday"] #This will be used with the output

  #Seperating the duration into parts
  duration_tuple = duration.split(":") #Split up durtation by ":"   DID TRY SPLIT HERE
  duration_hours = int(duration_tuple[0]) #Getting the hours from the duration tuple
  duration_minutes = int(duration_tuple[1]) #Getting the minutes from the duration tuple



  #Seperating the start into parts
  start_tuple = start.split(":") #Split start into hours and minutes+AM/PM
  start_minutes_tuple = start_tuple[1].split(" ") #Split the minutes from the AM/PM
  start_hours = int(start_tuple[0]) #Find the hours
  start_minutes = int(start_minutes_tuple[0]) #Find the minutes
  am_or_pm = start_minutes_tuple[1] #Find am or pm
  am_and_pm_flip = {"AM": "PM", "PM": "AM"} #what to do if need to flip

  amount_of_days = int(duration_hours / 24) #determine how many days go past

  #Determine the new_time minutes
  end_minutes = start_minutes + duration_minutes  #add the minutes up
  if (end_minutes >= 60): #add an hour if more than 60 minutes is passed on clock
    start_hours += 1
    end_minutes = end_minutes % 60
  amount_of_am_pm_flips = int((start_hours + duration_hours) / 12) #to determine if am or pm goes over 12
  end_hours = (start_hours + duration_hours) % 12

  #Fixing time format
  end_minutes = end_minutes if end_minutes > 9 else "0" + str(end_minutes) #to insure minutes has a 0 infront if it is in the single digits
  end_hours = 12 if end_hours == 0 else end_hours #showing 12 oclock instead of 0 oclock

  if(am_or_pm == "PM" and start_hours + (duration_hours % 12) >= 12): #if its PM and goes to a new day then
    amount_of_days += 1 #Add a day to the tracker


  am_or_pm = am_and_pm_flip[am_or_pm] if amount_of_am_pm_flips % 2 == 1 else am_or_pm #flip am or pm if it goes over 12
  
  return_time = str(end_hours) + ":" + str(end_minutes) + " " + am_or_pm

  if(day_of_week):#if there is an input for day of the week
    day_of_week = day_of_week.lower() #ensures it isnt case sensitive
    index = int((days_of_the_week_index[day_of_week]) + amount_of_days) % 7 #calculating which day to go to
    new_day = days_of_the_week_array[index]
    return_time += ", " + new_day #adding the new day to the output

  #how many days later
  if(amount_of_days == 1):
    return return_time + " " + "(next day)"
  elif(amount_of_days > 1):
    return return_time + " (" + str(amount_of_days) + " days later)"
    
  return return_time
