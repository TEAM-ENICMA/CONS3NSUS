"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import LabelFrame
from PIL import ImageTk, Image

main = tk.Tk()
main.geometry("1000x700")
main.title("CONS3NSUS")
main.iconphoto(True, ImageTk.PhotoImage(file = "C:/Users/Admin/Desktop/CONS3NSUS/for developers/imgs/consensus_icon.png"))

alignmentLabel = tk.Label(main, text = "Alignment")
alignmentLabel.place(x = 10, y = 180)

profileLabel = tk.Label(main, text = "Profile")
profileLabel.place(x = 10, y = 500)

consensusLabel = tk.Label(main, text = "Consensus")
consensusLabel.place(x = 10, y = 625)

lineLabel1 = tk.Label(main, text = "------------------------------------------------------------------------------------------")
lineLabel1.place(x = 125, y = 425)

lineLabel2 = tk.Label(main, text = "------------------------------------------------------------------------------------------")
lineLabel2.place(x = 125, y = 575)

header_png = ImageTk.PhotoImage(Image.open("C:/Users/Admin/Desktop/CONS3NSUS/for developers/imgs/consensus_header.png"))
headerLabel = tk.Label(image = header_png)
headerLabel.place(x = 650, y = 5)

descriptionLabel = tk.Label(main, text = "Find the consensus string from related sequences!")
descriptionLabel.place(x = 665, y = 110)

warningLabel1 = tk.Label(main, text = "Warning!!!")
warningLabel1.place(x = 665, y = 180)

warningLabel2 = tk.Label(main, text = "1) Make sure the lengths of sequences are equal")
warningLabel2.place(x = 665, y = 220)

warningLabel3 = tk.Label(main, text = "2) Make sure there is no other characters (U, *, etc.)")
warningLabel3.place(x = 665, y = 250)

warningLabel4 = tk.Label(main, text = "from 'A, T, G, C' letters in sequences")
warningLabel4.place(x = 665, y = 270)

input_box = st.ScrolledText(main, width = 55, borderwidth = 2, height = 20)
input_box.place(x = 125, y = 20)

def calculate():
    sequences = input_box.get("1.0", "end-1c").splitlines()

    if len(sequences[0]) > 37:
        popupWindow2 = tk.Tk()
        popupWindow2.title("ERROR")
        popupWindow2.geometry("250x100")
        popupWindow2Label1 = tk.Label(popupWindow2, text = "The given sequences are too long!!!")
        popupWindow2Label1.place(x = 30, y = 25)

        popupWindow2Label2 = tk.Label(popupWindow2, text = "(Max: 36 Nucleotide)")
        popupWindow2Label2.place(x = 60, y = 45)
        raise

    for s in range(len(sequences)):
        if len(sequences[s]) != len(sequences[s - 1]):
            popupWindow1 = tk.Tk()
            popupWindow1.title("ERROR")
            popupWindow1.geometry("250x100")

            popupWindow1Label = tk.Label(popupWindow1, text = "Unequal Sequence Lengths!!!")
            popupWindow1Label.place(x = 50, y = 35)
            raise


    totalA, totalT, totalG, totalC = [0] * len(sequences[0]), [0] * len(sequences[0]), [0] * len(sequences[0]), [0] * len(sequences[0])
    consensus = ""
    for n in range(len(sequences[0])):
        for s in range(len(sequences)):
            if sequences[s][n] == "A":
                totalA[n] += 1
            elif sequences[s][n] == "T":
                totalT[n] += 1
            elif sequences[s][n] == "G":
                totalG[n] += 1
            elif sequences[s][n] == "C":
                totalC[n] += 1
            else:
                popupWindow3 = tk.Tk()
                popupWindow3.title("ERROR")
                popupWindow3.geometry("250x100")

                popupWindow3Label1 = tk.Label(popupWindow3, text = "There are impermissible characters")
                popupWindow3Label1.place(x = 30, y = 25)

                popupWindow3Label2 = tk.Label(popupWindow3, text = "in your sequences!!!")
                popupWindow3Label2.place(x = 60, y = 45)
                raise

        if totalA[n] == max(totalA[n], totalT[n], totalG[n], totalC[n]):
            consensus = consensus + "A"
        elif totalT[n] == max(totalA[n], totalT[n], totalG[n], totalC[n]):
            consensus = consensus + "T"
        elif totalG[n] == max(totalA[n], totalT[n], totalG[n], totalC[n]):
            consensus = consensus + "G"
        elif totalC[n] == max(totalA[n], totalT[n], totalG[n], totalC[n]):
            consensus = consensus + "C"

    global ALabel, TLabel, GLabel, CLabel, consLabel

    ALabel = tk.Label(main, text = "A: " + str(totalA))
    ALabel.place(x = 125, y = 455)

    TLabel = tk.Label(main, text = "T: " + str(totalT))
    TLabel.place(x = 125, y = 485)
        
    GLabel = tk.Label(main, text = "G: " + str(totalG))
    GLabel.place(x = 125, y = 515)
        
    CLabel = tk.Label(main, text = "C: " + str(totalC))
    CLabel.place(x = 125, y = 545)

    consLabel = tk.Label(main, text = consensus)
    consLabel.place(x = 125, y = 625)

def clear():
    ALabel.destroy()
    TLabel.destroy()
    GLabel.destroy()
    CLabel.destroy()
    consLabel.destroy()

def showAboutSoftware():
    aboutSoftwareWindow = tk.Tk()
    aboutSoftwareWindow.geometry("205x150")
    aboutSoftwareWindow.title("About Software")

    frame = LabelFrame(aboutSoftwareWindow, padx = 35, pady = 35)
    frame.pack()

    nameLabel = tk.Label(frame, text = "Name: CONS3NSUS").pack()
    authorsLabel = tk.Label(frame, text = "Authors: ENICMA").pack()
    versionLabel = tk.Label(frame, text = "Version: 1.0").pack()
    environmentLabel = tk.Label(frame, text = "Developed at: Python 3.8").pack()

def showAboutUs():
    aboutUsWindow = tk.Tk()
    aboutUsWindow.geometry("250x195")
    aboutUsWindow.title("About Us")

    frame = LabelFrame(aboutUsWindow, padx = 35, pady = 35)
    frame.pack()

    teamLabel = tk.Label(frame, text = "Team: ENICMA").pack()
    membersLabel = tk.Label(frame, text = """Members:
    Bilgehan NEVRUZ
    Melih TEMEL
    Umut DURAK
    Özgür Can ARICAN""").pack()
    dateLabel = tk.Label(frame, text = "Date of Foundation: Aug. 8, 2021").pack()

def showContact():
    contactWindow = tk.Tk()
    contactWindow.geometry("300x135")
    contactWindow.title("Contact")

    frame = LabelFrame(contactWindow, padx = 35, pady = 35)
    frame.pack()

    githubLabel = tk.Label(frame, text = "Github: www.github.com/TEAM-ENICMA").pack()
    pypiLabel = tk.Label(frame, text = "Pypi: www.pypi.org/user/team_enicma/").pack()
    gmailLabel = tk.Label(frame, text = "Gmail: teamenicma@gmail.com").pack()

def showLicense():
    licenseWindow = tk.Tk()
    licenseWindow.geometry("600x420")
    licenseWindow.title("License")

    licLabel1 = tk.Label(licenseWindow, text = """CONS3NSUS v_1.0  Copyright © 2021  ENICMA
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    
    """).pack()

    licLabel2 = tk.Label(licenseWindow, text = """Disclaimer of Warranty.

    THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
    APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
    HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
    OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
    THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
    PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
    IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
    ALL NECESSARY SERVICING, REPAIR OR CORRECTION.""").pack()

calculateButton = tk.Button(main, text = "Calculate", width = 15, borderwidth = 3, height = 2, command = calculate)
calculateButton.place(x = 210, y = 370)

clearButton = tk.Button(main, text = "Clear", width = 15, borderwidth = 3, height = 2, command = clear)
clearButton.place(x = 370, y = 370)

aboutSoftwareButton = tk.Button(main, text = "About Software", width = 15, borderwidth = 3, height = 2, command = showAboutSoftware)
aboutSoftwareButton.place(x = 665, y = 450)

aboutUs = tk.Button(main, text = "About Us", width = 15, borderwidth = 3, height = 2, command = showAboutUs)
aboutUs.place(x = 805, y = 450)

contactButton = tk.Button(main, text = "Keep in touch!", width = 15, borderwidth = 3, height = 2, command = showContact)
contactButton.place(x = 665, y = 525)

licenseButton = tk.Button(main, text = "License", width = 15, borderwidth = 3, height = 2, command = showLicense)
licenseButton.place(x = 805, y = 525)

main.mainloop()
