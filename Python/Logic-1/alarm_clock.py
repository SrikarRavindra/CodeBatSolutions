def alarm_clock(day, vacation):
  return "7:00" if (not vacation and (day >=1 and day <=5)) else "10:00" if (not vacation and not (day >=1 and day <=5)) or (day>=1 and day<=5) else "off" 
