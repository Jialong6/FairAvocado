import tkinter
import csv
import Data_process

class Avocado_GUI:
    def __init__(self):

        # Create main window and set up the screen size
        self.main_window = tkinter.Tk()
        self.main_window.geometry("450x150")  # Width x Height

        # title
        self.prompt_label = tkinter.Label(self.main_window, \
                                          text="Avocado communist",fg = "green").grid(row=0,column=0,columnspan=4,sticky="n")

        # region (chosen value = self.v.get())
        self.region_label = tkinter.Label(self.main_window, \
                                        text="Region").grid(row=1,column=0)

        option_list_region = ['Albany', 'Atlanta','BaltimoreWashington','Boise', 'Boston', 'BuffaloRochester', \
'California', 'Charlotte', 'Chicago', 'CincinnatiDayton','Columbus', 'DallasFtWorth', 'Denver', 'Detroit', \
'GrandRapids', 'GreatLakes', 'HarrisburgScranton', 'HartfordSpringfield', 'Houston', 'Indianapolis', 'Jacksonville', \
'LasVegas', 'LosAngeles', 'Louisville', 'MiamiFtLauderdale', 'Midsouth', 'Nashville', 'NewOrleansMobile', \
'NewYork', 'Northeast', 'NorthernNewEngland', 'Orlando', 'Philadelphia', 'PhoenixTucson', 'Pittsburgh', \
'Plains', 'Portland', 'RaleighGreensboro', 'RichmondNorfolk', 'Roanoke', 'Sacramento', 'SanDiego', 'SanFrancisco', \
'Seattle', 'SouthCarolina', 'SouthCentral', 'Southeast', 'Spokane', 'StLouis', 'Syracuse', 'Tampa', 'TotalUS', \
'West', 'WestTexNewMexico']
        self.v = tkinter.StringVar()
        self.v.set("TotalUS")
        self.optionMenu_Region = tkinter.OptionMenu(self.main_window, self.v , *option_list_region).grid(row=2,column=0)

        # type(chosen value = self.v2.get())
        self.type_label = tkinter.Label(self.main_window, \
                                        text="Type").grid(row=1,column=1)
        option_list_type = ["conventional",
                            "organic",
                            "None"
                            ]
        self.v2 = tkinter.StringVar()
        self.v2.set("None")
        self.optionMenu_Type = tkinter.OptionMenu(self.main_window, self.v2 , *option_list_type).grid(row=2,column=1)

        # single_price
        self.price = tkinter.Label(self.main_window,text='Single Price').grid(row=1,column=2)
        self.price_entry = tkinter.Entry(self.main_window, \
                                        width=5)
        self.price_entry.grid(row=2,column=2)

        # botton
        self.button = tkinter.Button(self.main_window, \
                                     text = "convert", \
                                     command = self.compare).grid(row=2,column=3)

        # result
        self.result01 = tkinter.Label(self.main_window,text='The single price is').grid(column=0,columnspan=3)

        tkinter.mainloop()

    # Define a function used to calculate windchill when user click the botton
    def compare(self):
        r = self.v.get()
        t = self.v2.get()
        p = float(self.price_entry.get())
        rtp = Data_process.readinuser(r,t,p)
        output = Data_process.compare_price(rtp,p)
        #laabel = tkinter.Label(self.main_window,text=output).grid(row=3,column=3)



# Create an instance of the Windchill_Calculator_GUI class.
no_bug_please = Avocado_GUI()