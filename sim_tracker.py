
from tkinter import*
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root = Tk()
root.title("Phone Number Information")
root.geometry("365x584+300+200")
root.resizable(False,False)

def Track():
    enter_number = entry.get()
    number = phonenumbers.parse(enter_number)

    #country
    locate = geocoder.description_for_number(number, "en")
    country.config(text = locate)

    #operator like idea, jio others
    operator = carrier.name_for_number(number,"en")
    sim.config(text=operator)

    #phone timezone
    time = timezone.time_zones_for_number(number)
    zone.config(text = time)

    #latitude and longitudde
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(locate)

    lng = location.longitude
    lat = location.latitude
    longitude.config(text = lng)
    latitude.config(text = lat)

    #timezone
    obj = TimezoneFinder()
    result = obj.timezone_at(lng = location.longitude, lat = location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%p")
    clock.config(text = current_time)

#upload image
icon = PhotoImage(file= "logo image.png")
root.iconphoto(False, icon)

#logo image
logo = PhotoImage(file= "logo image.png")
Label(root, image=logo).place(x = 240, y = 70)

#search image
Eback = PhotoImage(file= "search png.png")
Label(root, image= Eback).place(x=20, y = 190)

#heading title
Heading = Label(root, text= "Track Number", font= ("monospace", 15, "bold"))
Heading.place(x = 90, y = 110)

#bottoom box
box = PhotoImage(file = "bottom png.png")
Label(root, image=box).place (x = -2, y = 335)

#entry box
entry = StringVar()
enter_number = Entry(root, textvariable= entry, width=25, justify="center", bd = 0,font= ("arial", 15, "bold"))
enter_number.place(x = 50, y=220)

#search button
search_image = PhotoImage(file= "search.png")
search = Button (root, image = search_image, borderwidth=0, cursor= "hand2", bd = 0, command=Track)
search.place(x =35, y = 300)

#add country
country = Label(root, text= "Country:", bg= "#EAF932", fg = "black", font= ("arial", 10, "bold"))
country.place(x = 50 ,y = 400 )

#add sim
sim = Label(root, text= "Sim:", bg= "#EAF932", fg = "black", font= ("arial", 10, "bold"))
sim.place(x = 200 ,y = 400 )

#add zone
zone = Label(root, text= "Zone:", bg= "#EAF932", fg = "black", font= ("arial", 10, "bold"))
zone.place(x = 50 ,y = 450 )

#add phonetime
clock = Label(root, text= "Phone Time:", bg= "#EAF932", fg = "black", font= ("arial", 10, "bold"))
clock.place(x = 200 ,y = 450 )

#set latitude
latitude = Label(root, text= "latitude:", bg= "#EAF932", fg = "black", font= ("arial", 10, "bold"))
latitude.place(x = 50 ,y = 500 )

#set longitude
longitude= Label(root, text= "Longitude:", bg= "#EAF932", fg = "black", font= ("arial", 10, "bold"))
country.place(x = 200 ,y = 500 )

root.mainloop()
