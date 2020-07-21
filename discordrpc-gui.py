try:
    from tkinter import *
    import tkinter.font as tkFont
    import os
    import json
    import datetime
    import time
    from pypresence import Presence
    import webbrowser
# checks if all modules installed    
except ModuleNotFoundError as e:
    print(e)
    print('pip install -r requirements.txt might fix it')
    exit()

app = Tk()

app.title("Advanced Discord RPC")
app.resizable(0, 0)


# check if config.json exists, if not create one with default values
if not os.path.isfile('./config.json'):
    data = {
        'CLIENT_ID': '123456789123456789',
        'State': 'Advanced Discord RPC',
        'Details': 'kaaaxcreators.de',
        'LImage': 'zero',
        'LTooltip': 'zero',
        'SImage': 'zero',
        'STooltip': 'zero',
        'Debug': 'False',
    }
    jstr = json.dumps(data, indent=4)
    f= open("config.json","w+")
    f.write(jstr)

# load config.json as variables
with open('config.json') as f:
    data = json.load(f)
    details = data['Details']
    state = data['State']
    client_id = data['CLIENT_ID']
    limage = data['LImage']
    ltooltip = data['LTooltip']
    simage = data['SImage']
    stooltip = data['STooltip']
    debug = data['Debug']

# title starts here
ltext=StringVar()
ltext.set("ADVANCED DISCORD RPC")
fontStyle = tkFont.Font(family="Lucida Grande", size=25, underline=1)
ltext=Label(app, textvariable=ltext, height=2, justify='center', anchor="center", fg="#00CC66", width="25", font=fontStyle)
ltext.grid(row=1,columnspan=6)

# details start here
dtext=StringVar()
dtext.set("Details")
dtext=Label(app, textvariable=dtext, height=4)
dtext.grid(row=2,column=1)

edetails=StringVar()
edetails.set(details)
dentry=Entry(app,textvariable=edetails,width=25)
dentry.grid(row=2,column=2)

# debug starts here
debugtext=StringVar()
debugtext.set("Debug")
debugtext=Label(app, textvariable=debugtext, height=4)
debugtext.grid(row=2,column=3)

edcheck = BooleanVar()
edcheck.set(debug)
debugcheck=Checkbutton(app, var=edcheck)
debugcheck.grid(row=2,column=4)

# state starts here
stext=StringVar()
stext.set("State")
stext=Label(app, textvariable=stext, height=4)
stext.grid(row=3,column=1)

estate=StringVar(None)
estate.set(state)
sentry=Entry(app,textvariable=estate,width=25)
sentry.grid(row=3,column=2)

# client id starts here
cidtext=StringVar()
cidtext.set("Client ID")
cidtext=Label(app, textvariable=cidtext, height=4)
cidtext.grid(row=3,column=3)

ecid=StringVar(None)
ecid.set(client_id)
lientry=Entry(app,textvariable=ecid,width=25)
lientry.grid(row=3,column=4)

# large image starts here
litext=StringVar()
litext.set("Large Image")
litext=Label(app, textvariable=litext, height=4)
litext.grid(row=4,column=1)

elimage=StringVar(None)
elimage.set(limage)
lientry=Entry(app,textvariable=elimage,width=25)
lientry.grid(row=4,column=2)

# large tooltip starts here
lttext=StringVar()
lttext.set("Large Tooltip")
lttext=Label(app, textvariable=lttext, height=4)
lttext.grid(row=4,column=3)

eltooltip=StringVar(None)
eltooltip.set(ltooltip)
ltentry=Entry(app,textvariable=eltooltip,width=25)
ltentry.grid(row=4,column=4)

# small image starts here
sitext=StringVar()
sitext.set("Small Image")
sitext=Label(app, textvariable=sitext, height=4)
sitext.grid(row=5,column=1)

esimage=StringVar(None)
esimage.set(simage)
sientry=Entry(app,textvariable=esimage,width=25)
sientry.grid(row=5,column=2)

# small tooltip starts here
sttext=StringVar()
sttext.set("Small Tooltip")
sttext=Label(app, textvariable=sttext, height=4)
sttext.grid(row=5,column=3)

estooltip=StringVar(None)
estooltip.set(stooltip)
stentry=Entry(app,textvariable=estooltip,width=25)
stentry.grid(row=5,column=4)

# run button starts here
erun=StringVar(None)
erun.set("RUN")
runbtn=Button(app,textvariable=erun,width=25, bg="#00CC00", command=lambda: run())
runbtn.grid(row=6,column=4)

# github button starts here
egit=StringVar(None)
egit.set("Github")
gitbtn=Button(app, textvariable=egit, width=25, bg="#808080", command=lambda: browser())
gitbtn.grid(row=6,columnspan=4,sticky=W+E)

def browser():
    webbrowser.open('https://github.com/kaaax0815/advanced-discord-rpc', new = 2)

RPC = Presence(ecid.get())
RPC.connect()

# get text out of entry and store it in config.json
def run():
    data['CLIENT_ID'] = ecid.get()
    newclientid = ecid.get()
    data['State'] = estate.get()
    newstate = str(estate.get())
    data['Details'] = edetails.get()
    newdetails = str(edetails.get())
    data['LImage'] = elimage.get()
    newlimage = str(elimage.get())
    data['LTooltip'] = eltooltip.get()
    newltooltip = str(eltooltip.get())
    data['SImage'] = esimage.get()
    newsimage = str(esimage.get())
    data['STooltip'] = estooltip.get()
    newstooltip = str(estooltip.get())
    data['Debug'] = str(edcheck.get())
    start = datetime.datetime.now().timestamp()
    with open("config.json", 'w') as f:
        json.dump(data, f, indent=4)
    if str(edcheck.get()) == "True":
        print(RPC.update(details=newdetails, state=newstate, large_image=newlimage, large_text=newltooltip, small_image=newsimage, small_text=newstooltip, start=int(start)))
    if str(edcheck.get()) == "False":
        # Set the presence              
        RPC.update(details=newdetails, state=newstate, large_image=newlimage, large_text=newltooltip, small_image=newsimage, small_text=newstooltip, start=int(start))
    
        # prints every setting
        print("Details:", newdetails,"; \nState:", newstate,"; \nClient-ID:", newclientid,"; \nLarge_Image:", newlimage,"; \nLarge_Tooltip:", newltooltip,"; \nSmall_Image:", newsimage,"; \nSmall_Tooltip:", newstooltip, ";")

def shutlol():
    RPC.close()
    app.destroy()
    exit()

app.mainloop()
