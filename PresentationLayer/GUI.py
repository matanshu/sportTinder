from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from datetime import datetime
from ServiceLayer.programmanager import ProgramManager


#Home page, initiate first buttons, size, pictures
class First_screen(Tk):
    def __init__(self):
        super().__init__()
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.join_click = False
        self.create_click= False
        ProgramManager.create_db()
        self.background_photo=ImageTk.PhotoImage(Image.open("./resources/sportLogo.png"))
        self.background = Label(self, image=self.background_photo)
        self.background.place(x=0, y=0)

        self.font=("helvetica Bold", 20)
        self.title("SPOTINDER")
        self.labelOfTheSystem = Label(self, text="Welcome to sporTinder", font=("Arial Bold", 30))
        self.labelOfTheSystem.place(relx=0.35, rely=0.1)


        image = Image.open("./resources/sport4.jfif")
        image = image.resize((400, 400), Image.ANTIALIAS)
        self.picture1 = ImageTk.PhotoImage(image)

        self.picture1_lbl = Label(self, image=self.picture1)
        self.picture1_lbl.place(relx=0.35, rely=0.2)


        self.attributes('-fullscreen', True)

        self.btn_join = Button(self, text="JOIN GAME", command=self.clicked_join, font=self.font)
        self.btn_join.place(relx=0.35, rely=0.8)


        self.btn_create = Button(self, text="CREATE GAME", command=self.clicked_create, font=self.font)
        self.btn_create.place(relx=0.55, rely=0.8)


        self.btn_exit = Button(self, text="EXIT", command=self.destroy, font=self.font)
        self.btn_exit.place(relx=0.94, rely=0)



# the page when the user click on join game button, the fucntion show a query that the user need to fill.
    def clicked_join(self):


        self.btn_create.destroy()
        self.btn_join.destroy()
        self.labelOfTheSystem.destroy()
        self.picture1_lbl.destroy()
        self.lbl_name = Label(self, text="Enter your username", font=self.font)
        self.lbl_name.place(relx=0.2, rely=0.1)
        self.txt_name = Entry(self, width=12, font=self.font)
        self.txt_name.place(relx=0.5, rely=0.1)
        self.lbl_street = Label(self, text="What your current street", font=self.font)
        self.lbl_street.place(relx=0.2, rely=0.2)
        self.txt_street = Entry(self, width=12, font=self.font)
        self.txt_street.place(relx=0.5, rely=0.2)

        self.lbl_distance = Label(self, text="How far would you go?(km)", font=self.font)
        self.lbl_distance.place(relx=0.2, rely=0.3)
        self.txt_distance = Entry(self, width=12, font=self.font)
        self.txt_distance.place(relx=0.5, rely=0.3)

        self.lbl_sport = Label(self, text="Choose your sport", font=self.font)
        self.lbl_sport.place(relx=0.2, rely=0.4)
        self.combo_sport = Combobox(self, font=self.font, width=12,state = "readonly")
        self.combo_sport['values'] = ('basketball', 'baseball', 'tennis')
        self.combo_sport.place(relx=0.5, rely=0.4)
        self.combo_sport.current(0)

        self.lbl_hours = Label(self, text="Choose your hours to play", font=self.font)
        self.lbl_hours.place(relx=0.2, rely=0.5)
        self.combo_hours = Combobox(self, font=self.font, width=12, state = "readonly")
        self.combo_hours['values'] = (
        "10:00 - 12:00", "12:00 - 14:00", "14:00 - 16:00", "16:00 - 18:00", "18:00 - 20:00", "20:00 - 22:00")
        self.combo_hours.place(relx=0.5, rely=0.5)
        self.combo_hours.current(0);

        self.lbl_calender = Label(self, text="Choose date", font=self.font)
        self.lbl_calender.place(relx=0.2, rely=0.6)
        self.calender = DateEntry(self, width=12, background='darkblue',font=self.font,state = "readonly")
        self.calender.place(relx=0.5, rely=0.6)


        self.btn_submit = Button(self, text="FIND ME A MATCH", command=self.validation, font=self.font)
        self.btn_submit.place(relx=0.2, rely=0.7)
        self.join_click = True

        self.btn_back = Button(self, text="GO BACK", command=self.go_back, font=self.font)
        self.btn_back.place(relx=0.4, rely=0.7)



    # the page when the user click on create game button, the fucntion show a query that the user need to fill.
    def clicked_create(self):
        self.create_click = True
        self.btn_create.destroy()
        self.btn_join.destroy()
        self.labelOfTheSystem.destroy()
        self.picture1_lbl.destroy()
        self.lbl_name = Label(self, text="Enter your username", font=self.font)
        self.lbl_name.place(relx=0.2, rely=0.1)
        self.txt_name = Entry(self, width=12, font=self.font)
        self.txt_name.place(relx=0.5, rely=0.1)
        self.lbl_street = Label(self, text="What your current street", font=self.font)
        self.lbl_street.place(relx=0.2, rely=0.2)
        self.txt_street = Entry(self, width=12, font=self.font)
        self.txt_street.place(relx=0.5, rely=0.2)

        self.lbl_distance = Label(self, text="How far would you go?(km)", font=self.font)
        self.lbl_distance.place(relx=0.2, rely=0.3)
        self.txt_distance = Entry(self, width=12, font=self.font)
        self.txt_distance.place(relx=0.5, rely=0.3)

        self.lbl_sport = Label(self, text="Choose your sport", font=self.font)
        self.lbl_sport.place(relx=0.2, rely=0.4)
        self.combo_sport = Combobox(self, font=self.font, width=12, state = "readonly")
        self.combo_sport['values'] = ('basketball', 'baseball', 'tennis')
        self.combo_sport.place(relx=0.5, rely=0.4)
        self.combo_sport.current(0)

        self.lbl_hours = Label(self, text="Choose your hours to play", font=self.font)
        self.lbl_hours.place(relx=0.2, rely=0.5)
        self.combo_hours = Combobox(self, font=self.font, width=12, state = "readonly")
        self.combo_hours['values'] = (
            "10:00 - 12:00", "12:00 - 14:00", "14:00 - 16:00", "16:00 - 18:00", "18:00 - 20:00", "20:00 - 22:00")
        self.combo_hours.place(relx=0.5, rely=0.5)
        self.combo_hours.current(0)

        self.lbl_calender =  Label(self, text="Choose date", font=self.font)
        self.lbl_calender.place(relx=0.2, rely=0.6)
        self.calender = DateEntry(self, width=12, background='darkblue', font=self.font,state = "readonly")

        self.calender.place(relx=0.5, rely=0.6)

        self.lbl_max_participants = Label(self, text="Max pariticipants", font=self.font)
        self.lbl_max_participants.place(relx=0.2, rely=0.7)
        self.txt_max_participants = Entry(self, width=12, font=self.font)
        self.txt_max_participants.place(relx=0.5, rely=0.7)

        self.btn_submit = Button(self, text="FIND ME A MATCH", command=self.validation, font=self.font)
        self.btn_submit.place(relx=0.2, rely=0.8)

        self.btn_back = Button(self, text="GO BACK", command=self.go_back, font=self.font)
        self.btn_back.place(relx=0.4, rely=0.8)

#go back button, allow to go back to the first screen
    def go_back(self):
        self.destroy()
        self = First_screen()

#validation check, the function show validation errors if there are in the query, and if not it create the next pages (create/join)
    def validation(self):
        text_error = ""

    #date check
        time_now = datetime.now()
        date_split = self.calender.get().split('/')
        hour_split = self.combo_hours.get().split(':')
        year = int("20" + date_split[2])
        month = int(date_split[0])
        day = int(date_split[1])
        hour = int(hour_split[0])
        user_date = datetime(year,month,day,hour)

        if user_date< time_now:
            text_error = text_error + "Selected date cant be in the past.\n"

        #empty check
        if len(self.txt_name.get())==0:
                text_error = text_error +"Username is empty\n"
        if len(self.txt_street.get())==0:
                text_error = text_error +"Street is empty\n"
        if len(self.txt_distance.get())==0:
                text_error = text_error +"Distance is empty\n"
        if self.create_click == True and len(self.txt_max_participants.get())==0:
            text_error = text_error + "Max participants is empty\n"

            #is valid state/city/street maybe from matan
        if not ProgramManager.is_legal_address(self.txt_street.get()):
            text_error = text_error + "Not legal address\n"
            # is only a number check
        if not self.txt_distance.get().isdigit():
                text_error = text_error + "Distance must contains only digits\n"
        if self.create_click == True and not self.txt_max_participants.get().isdigit():
            text_error = text_error + "Max participants must contains only digits\n"

            #user name exist check - check from the db.

        if text_error !="":
               messagebox.showerror("Error", text_error)
               return False
        else:
            messagebox.showinfo("Confirmed","Please choose!")
            name = self.txt_name.get()
            street =  self.txt_street.get()
            distance = self.txt_distance.get()
            sport = self.combo_sport.get()
            hours = self.combo_hours.get()
            date = self.calender.get()
            ProgramManager.set_user_location(street)
            if self.create_click ==True:
                max_participants = self.txt_max_participants.get()
                self.destroy()
                self = Create_Game(name, street, int(distance), sport, hours,date,int(max_participants))
            elif self.join_click==True:
                self.destroy()
                self = Join_Game(name, street,  int(distance), sport, hours,date)

#The page of create game, show the first accurate result of the user query with the button "yes" and button "no"
class Create_Game(Tk):
    def __init__(self,user_name,street,distance,sport,hours, date, max_participants):
        super().__init__()
        self.user_name = user_name
        self.street = street
        self.distance = distance
        self.sport = sport
        self.hours = hours
        self.date = date
        self.max_participants = max_participants
        self.index = 0

        self.width = self.winfo_screenwidth() #get display width
        self.height = self.winfo_screenheight() #get display height
        self.attributes('-fullscreen', True)
        self.font=("helvetica", 40)
        self.font_exit = ("helvetica", 20)
        self.font_details = ("helvetica", 15,"bold")
        date_split = self.date.split('/')
        hour_split = self.hours.split(':')
        self.year = int("20"+date_split[2])
        self.month = int(date_split[0])
        self.day = int(date_split[1])
        self.hour = int(hour_split[0])
        self.pitchs = ProgramManager.get_available_pitches(self.sport, self.year, self.month, self.day, self.hour, int(self.distance))
        if len( self.pitchs)==0:
            messagebox.showerror("No results","We dont found pitchs that fit to your query, please try again!")
            self.destroy()
            self = First_screen()
        else:
            imageYes = Image.open("./resources/tinderYes.png")
            imageYes = imageYes.resize((150, 150), Image.ANTIALIAS)
            self.pictureyes = ImageTk.PhotoImage(imageYes)

            self.pictureyes_lbl = Label(self, image=self.pictureyes)
            self.pictureyes_lbl.place(relx=0.55, rely=0.8)

            self.btn_approve = Button(self, image= self.pictureyes, command=self.register_game_in_db,borderwidth=0)
            self.btn_approve.place(relx=0.55, rely=0.8)

            imageNo = Image.open("./resources/tinderNo.png")
            imageNo = imageNo.resize((150, 150), Image.ANTIALIAS)
            self.pictureno = ImageTk.PhotoImage(imageNo)

            self.pictureno_lbl = Label(self, image=self.pictureno)
            self.pictureno_lbl.place(relx=0.35, rely=0.8)

            self.btn_dismiss = Button(self, image=self.pictureno, command=self.next_pitch, borderwidth=0)
            self.btn_dismiss.place(relx=0.35, rely=0.8)


            image = Image.open("./resources/think2.png")
            image = image.resize((100, 100), Image.ANTIALIAS)
            self.picture1 = ImageTk.PhotoImage(image)

            self.picture1_lbl = Label(self, image=self.picture1)
            self.picture1_lbl.place(relx=0.45, rely=0.05)

            first_pitch =  self.pitchs[0]
            self.pitch_id = first_pitch[0].id
            self.pitch_address= first_pitch[0].address
            self.pitch_distance = first_pitch[1]
            distance_split = str(self.pitch_distance).split('.')
            self.pitch_distance = distance_split[0]
            self.lbl_pitch_address_label = Label(self, text="Pitch Address: "+self.pitch_address, font=self.font_details)
            self.lbl_pitch_address_label.place(relx=0.1, rely=0.3)
            self.lbl_pitch_distance_label = Label(self, text="Distance(km): "+str(self.pitch_distance), font=self.font_details)
            self.lbl_pitch_distance_label.place(relx=0.1, rely=0.4)
            self.lbl_sport_branch_label = Label(self, text="Sport: "+self.sport, font=self.font_details)
            self.lbl_sport_branch_label.place(relx=0.1, rely=0.5)
            self.lbl_available_time = Label(self, text="Time: "+self.hours, font=self.font_details)
            self.lbl_available_time.place(relx=0.1, rely=0.6)
            self.btn_exit = Button(self, text="EXIT", command=self.destroy, font=self.font_exit)
            self.btn_exit.place(relx=0.94, rely=0)
            self.background_photo = ImageTk.PhotoImage(Image.open("./resources/sportLogo.png"))
            self.background = Label(self, image=self.background_photo)
            self.background.place(x=0, y=0)

#in case the user press on "yes" button the function register the game  in the db , show the user that the game createdand exit from the system
    def register_game_in_db(self):
            ProgramManager.create_game(self.sport,self.pitch_id,self.year,self.month,self.day,self.hour,self.max_participants)
            messagebox.showinfo("SUCSESS", "The game is created")
            self.destroy()
#in case the user press "no" button the function get the next pitch that available and fit to the user query.
    def next_pitch(self):
        # self.lbl_pitch_name.
        self.index = self.index + 1
        self.lbl_pitch_address_label.destroy()
        self.lbl_pitch_distance_label.destroy()


        if self.index >= len(self.pitchs):
            self.lbl_sport_branch_label.destroy()
            self.lbl_available_time.destroy()
            messagebox.showerror("Error", "No more pitchs available to your query")
            self.destroy()
            self = First_screen()
        else:
            next_pitch = self.pitchs[self.index]
            next_address = next_pitch[0].address
            next_distance = next_pitch[1]
            distance_split = str(next_distance).split('.')
            next_distance = distance_split[0]
            self.pitch_id=next_pitch[0].id
            self.lbl_pitch_address_label = Label(self, text="Pitch Address: "+next_address, font=self.font_details)
            self.lbl_pitch_address_label.place(relx=0.1, rely=0.3)
            self.lbl_pitch_distance_label = Label(self, text="Distance(Km): "+str(next_distance), font=self.font_details)
            self.lbl_pitch_distance_label.place(relx=0.1, rely=0.4)

#The page of join game, show the first accurate result of the user query with the button "yes" and button "no"
class Join_Game(Tk):
    def __init__(self,user_name,street,distance,sport,hours,date):
        super().__init__()
        self.user_name = user_name
        self.street = street
        self.distance = distance
        self.sport = sport
        self.hours = hours
        self.date = date
        self.index = 0
        date_split = self.date.split('/')
        hour_split = self.hours.split(':')
        self.year = int("20" + date_split[2])
        self.month = int(date_split[0])
        self.day = int(date_split[1])
        self.hour = int(hour_split[0])
        self.games = ProgramManager.get_available_games(sport,self.year,self.month,self.day,self.hour,self.distance)
        self.font = ("helvetica", 40)
        self.font_exit = ("helvetica", 20)
        self.font_details = ("helvetica", 15, "bold")
        self.background_photo = ImageTk.PhotoImage(Image.open("./resources/sportLogo.png"))
        self.background = Label(self, image=self.background_photo)
        self.background.place(x=0, y=0)
        self.width = self.winfo_screenwidth()  # get display width
        self.height = self.winfo_screenheight()  # get display height
        self.attributes('-fullscreen', True)
        if len( self.games)==0:
            messagebox.showerror("No results","We dont found games that fit to your query, please try again!")
            self.destroy()
            self=First_screen()
        else:

            imageYes = Image.open("./resources/tinderYes.png")
            imageYes = imageYes.resize((150, 150), Image.ANTIALIAS)
            self.pictureyes = ImageTk.PhotoImage(imageYes)

            self.pictureyes_lbl = Label(self, image=self.pictureyes)
            self.pictureyes_lbl.place(relx=0.55, rely=0.8)

            self.btn_approve = Button(self, image= self.pictureyes, command=self.register_in_db,borderwidth=0)
            self.btn_approve.place(relx=0.55, rely=0.8)

            imageNo = Image.open("./resources/tinderNo.png")
            imageNo = imageNo.resize((150, 150), Image.ANTIALIAS)
            self.pictureno = ImageTk.PhotoImage(imageNo)

            self.pictureno_lbl = Label(self, image=self.pictureno)
            self.pictureno_lbl.place(relx=0.35, rely=0.8)

            self.btn_dismiss = Button(self, image=self.pictureno, command=self.next_match, borderwidth=0)
            self.btn_dismiss.place(relx=0.35, rely=0.8)
            image = Image.open("./resources/think2.png")
            image = image.resize((100, 100), Image.ANTIALIAS)
            self.picture1 = ImageTk.PhotoImage(image)

            self.picture1_lbl = Label(self, image=self.picture1)
            self.picture1_lbl.place(relx=0.45, rely=0.05)

            first_game =  self.games[0]
            self.pitch_address = first_game[2].address
            self.pitch_distance = first_game[1]
            distance_split = str(self.pitch_distance).split('.')
            self.pitch_distance = distance_split[0]
            self.max_participants = first_game[0].max_participants
            self.curr_participants = first_game[0].current_participants
            self.game_id=first_game[0].id_game
            self.lbl_pitch_address = Label(self, text="Pitch address: "+self.pitch_address, font=self.font_details)
            self.lbl_pitch_address.place(relx=0.1, rely=0.3)
            self.lbl_distance_from_you = Label(self, text="Distance(Km): "+str(self.pitch_distance), font=self.font_details)
            self.lbl_distance_from_you.place(relx=0.1, rely=0.4)
            self.lbl_sport_branch = Label(self, text="Sport: "+self.sport, font=self.font_details)
            self.lbl_sport_branch.place(relx=0.1, rely=0.5)
            self.lbl_available_time = Label(self, text="Time: "+self.hours, font=self.font_details)
            self.lbl_available_time.place(relx=0.1, rely=0.6)
            self.lbl_max_par = Label(self, text="Max participants: "+str(self.max_participants), font=self.font_details)
            self.lbl_max_par.place(relx=0.1, rely=0.7)
            self.lbl_curr_par = Label(self, text="Current participants: "+str(self.curr_participants), font=self.font_details)
            self.lbl_curr_par.place(relx=0.1, rely=0.8)
            self.btn_exit = Button(self, text="EXIT", command=self.destroy, font=self.font_exit)
            self.btn_exit.place(relx=0.94, rely=0)

# in case the user press on "yes" button the function register the user into the game in the db , show the user that he joined to the game and exit from the system
    def register_in_db(self):
        ProgramManager.join_to_game(self.game_id)
        messagebox.showinfo("SUCSESS", "You successfully joined to a game!")
        self.destroy()

# in case the user press "no" button the function get the next game that available and fit to the user query.
    def next_match(self):
        self.index = self.index + 1
        self.lbl_distance_from_you.destroy()
        self.lbl_pitch_address.destroy()
        self.lbl_curr_par.destroy()
        self.lbl_max_par.destroy()
        if self.index >= len(self.games):
            self.lbl_sport_branch.destroy()
            self.lbl_available_time.destroy()
            messagebox.showerror("Error", "No more games Available to your query")
            self.destroy()
            self = First_screen()
        else:
            next_game = self.games[self.index]
            self.game_id =next_game[0].id_game
            next_address = next_game[2].address
            next_distance = next_game[1]
            next_max_par = next_game[0].max_participants
            next_curr_par = next_game[0].current_participants
            distance_split = str(next_distance).split('.')
            next_distance = distance_split[0]
            self.lbl_pitch_address = Label(self, text="Pitch Address: " +next_address, font=self.font_details)
            self.lbl_pitch_address.place(relx=0.1, rely=0.3)
            self.lbl_distance_from_you = Label(self, text="Distance(Km): " +str(next_distance), font=self.font_details)
            self.lbl_distance_from_you.place(relx=0.1, rely=0.4)
            self.lbl_max_par = Label(self, text="Max participants: " +str(next_max_par), font=self.font_details)
            self.lbl_max_par.place(relx=0.1, rely=0.7)
            self.lbl_curr_par = Label(self, text="Current participants: " +str(next_curr_par), font=self.font_details)
            self.lbl_curr_par.place(relx=0.1, rely=0.8)



app = First_screen()
app.bind("<Escape>", lambda x: app.destroy())
app.geometry('500x500')
app.mainloop()