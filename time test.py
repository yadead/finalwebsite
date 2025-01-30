from datetime import datetime
import math


Start_Time = input("Start Time (hh:mm dd/mm/yyyy): ")
End_Time = input("End Time (hh:mm dd/mm/yyyy): ")
time_format = "%H:%M %d/%m/%Y"
start_dt = datetime.strptime(Start_Time, time_format)
end_dt = datetime.strptime(End_Time, time_format)
Time_Worked = end_dt - start_dt
total_minutes = Time_Worked.total_seconds() / 60
rounded_minutes = math.ceil(total_minutes / 15) * 15
rounded_hours = rounded_minutes / 60

# Diary_Entry = now.strftime("%H:%M %d/%B/%Y")
print(f"Time Worked: {rounded_hours:.2f} hours")

