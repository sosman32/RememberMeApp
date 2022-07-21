# Tkinter is imported to be able to create the UI
import tkinter as tk
# Filedialog is imported to allow file/directory selection window
from tkinter import filedialog
# os is imported to allow communication with the operating system to launch the applications
import os

# variable root set for the root tk.TK()
root = tk.Tk()
# apps array declared
apps = []



if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        print(apps)

# function created for the addApp button
def addApp():
    # this prevents the duplicated children widgets when adding new apps to the list
    for widget in frame.winfo_children():
        widget.destroy()

    # line below will append the file name selected to the variable filename to be used later to append to apps list
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    # this line will append the application to the apps list if one is selected,
    if filename:
        apps.append(filename)
        # this below is terminal output to confirm app added title
        print("The app added is: ")
        # this below is terminal output to confirm app added by displaying the filename
        print(filename)
        print("\n")

        # if an app is appended than this following block of code will be executed to add labels
        for app in apps:
            # this below is used to display the frame title "app added to list",
            # also will show the index position converted to string as part of title
            labelTitle = tk.Label(frame, text="List item number: \n" + str(apps.index(app)+1), fg="black", font=1, bg="goldenrod1")
            # this below is used to populate the filename which was appended to apps
            labelFile = tk.Label(frame, text=app, font=1, bg="wheat")

            labelTitle.pack()
            labelFile.pack()

    # if no app is appended then this block will be executed
    else:
        print("No file selected to add\n")
        for app in apps:
            # this below is used to display the frame title "app added to list",
            # also will show the index position converted to string as part of title,
            # it's not perfect, if duplicate it will return first index position of duplicate, need to fix
            labelTitle = tk.Label(frame, text="List item number: \n" + str(apps.index(app)+1), fg="black", font=1, bg="goldenrod1")
            labelFile = tk.Label(frame, text=app, font=1, bg="wheat")
            labelTitle.pack()
            labelFile.pack()


# Added the function for the remove button to remove the item at index[0] in apps array
# and also remove the labelFile/labelTitle associated will the app in index[0]
def removeApp():
    # this will destroy all children frames upon refresh of the screen
    for widget in frame.winfo_children():
        widget.destroy()

    # if there are apps stored in the apps array, then delete the app in index[0]
    # then console log display the app which was removed
    # then console log display all the remaining apps in the list
    if apps:
        deleteItem = apps.pop(0)
        print("The file removed is:") # this line is just for console log neatness
        print(deleteItem)
        print("\nthe remaining file(s) are: ") # this line is just for console log neatness
        print(apps)
        print("\n")  # this line is just for console log neatness
    else:
        print("\n No list items remain to delete")

    # this below is used to display the frame title "app added to list".
    # also will show the index position converted to string as part of title,
    # it's not perfect, if duplicate it will return first index position of duplicate, need to fix
    for app in apps:
        labelTitle = tk.Label(frame, text="List item number: \n" + str(apps.index(app) + 1), fg="black", font=1, bg="goldenrod1")
        labelFile = tk.Label(frame, text=app, font=1, bg="wheat")
        labelTitle.pack()
        labelFile.pack()


# function created to run the apps for the runnApps button
def runApps():
    # following will check if there are any apps added to apps[], if so launch them all,
    # if not display message to inform no items in list
    if apps:
        for app in apps:
            os.startfile(app)
            print("The following app was launched successfully: ")
            print(app)
    else:
        print("Unable to launch, no apps in the list")




# Configure the ROOT color
root.configure(bg='tomato')
# Create label for Root Title
rootLabel = tk.Label(root, text="Remember Me App Launcher", font=1, bg="wheat2")
# add label to pack() to display on root
rootLabel.pack()


canvas = tk.Canvas(root, height=400, width=700, bg="tomato")
canvas.pack()

frame = tk.Frame(root, bg="tan1")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

openFile = tk.Button(root, text="Add File", padx=25,
                     pady=10, fg='white', bg="#263D42", command=addApp)
openFile.pack()

# Added a remove file button
removeFile = tk.Button(root, text="Remove File", padx=25,
                       pady=10, fg='white', bg="#263D42", command=removeApp)
# This will append the remove button to the root, which will display on the screen
removeFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=25,
                    pady=10, fg='white', bg="#263D42", command=runApps)
runApps.pack()

# this displays the list after app is launched again, not a rerun, just a fresh new launch
for app in apps:
    # this below is used to display the frame title "app added to list",
    # also will show the index position converted to string as part of title,
    # it's not perfect, if duplicate it will return first index position of duplicate, need to fix
    labelTitle = tk.Label(frame, text="List item number: \n" + str(apps.index(app)+1), fg="black", font=1, bg="goldenrod1")
    labelFile = tk.Label(frame, text=app, font=1, bg="wheat")
    labelTitle.pack()
    labelFile.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')