def add_time(start, duration, weekday = False):
  
  day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

  day_time = 24
  
  time, aMorPM = start.split(" ")
  hours, mins = time.split(":")
  durationHours, durationMins = duration.split(":")

  #get the total hours and minutes of the new time
  totalHours = int(hours) + int(durationHours)
  totalMins = int(mins) + int(durationMins)

  #clean the new hours and minutes up so it makes more sense
  



    return new_time
