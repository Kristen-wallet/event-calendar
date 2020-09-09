from tkinter import Tk,Canvas
from datetime import date,datetime

def get_event():
    list_event = []
    with open('events.txt','r') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date = datetime.strptime(current_event[1],'%d/%m/%Y').date()
            current_event[1]=event_date
            list_event.append(current_event)
        return list_event
def days_btn_dates(eventdate,todaydate):
    time_between=str(eventdate-todaydate)
    number_of_days=time_between.split(' ')
    return number_of_days[0]

events = get_event()
today = date.today()
vertical_space = 80
events.sort(key=lambda x: x[1])

root = Tk()
root.title('countdown calender')
c = Canvas(root,height=500,width=800,bg='black')
c.pack()
c.create_text(280,50,anchor='w',fill='orange',font='Algerian 18 underline', text='My Countdown Calendar')
for event in events:
    event_name=event[0]
    days_until = days_btn_dates(event[1],today)
    display = "\u2764It is %s days until %s "%(days_until,event_name)
    if int(days_until) <= 7:
        text_col = 'red'
    else:
        text_col = 'white'

    c.create_text(50,vertical_space,anchor='w',fill=text_col,font='Arial 13', text=display)
    vertical_space = vertical_space + 25
root.mainloop()