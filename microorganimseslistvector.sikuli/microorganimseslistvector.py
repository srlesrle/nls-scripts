##                                                          ##
##    beginning of the program when the research is done    ##
##    and you find yourself in card index                   ##
numberOfSubjects = 170
onlyAtBeginningCount = 0
howMuchOfiemsToTake = 10


for i in range(numberOfSubjects):
    if onlyAtBeginningCount == 0:
        click(Pattern("1493852876083.png").targetOffset(0,16))#click on first part
    else:
        type(Key.DOWN)#select next subject

    onlyAtBeginningCount = 1
    sleep(4)#when you click on  
    wait(Pattern("1493908245377.png").targetOffset(-118,250), 30*60)
    click(Pattern("1493908245377.png").targetOffset(-118,250))#click on the image of the part with offset
    
    wait("1493853550186.png", 30*60)#the button to appear can take a while, so wait till it appears
    click("1493853550186.png")#after you get button test
    wait("1493854280565.png", 30*60)#the button to appear can take a while, so wait till it appears

    click("1493853595491.png") #click on button clear to clear all previeous selected subjects
    sleep(0.3)
    click(Pattern("1493853625672.png").targetOffset(-43,0))#select pathology
    sleep(0.3)
    click(Pattern("1493860166847.png").targetOffset(-126,-2))
    click("1493853682961.png")#adjust all to get real info

    sleep(3) #sleep to give more time to load it TODO: this should later be replaced with better code
    click(Pattern("1493854868280.png").targetOffset(0,17))#click on list
    type(Key.DOWN)#click down arrow on list to come to subjects
    type(Key.DOWN)
    type(Key.DOWN)
    sleep(4)

    keyDown(Key.SHIFT)#in the windows to select them all press SHIFT and go with arrow down to select them all
    if not exists("1493927047356.png"):
        for i in range(7):#usually there are 90 items TODO: do only ones till 1.5
           type(Key.DOWN)
           #sleep(0.3)
    else:
        for i in range(howMuchOfiemsToTake):
            #myRegion = Region("1493928207507.png")
            #if exists(Pattern("1493926779828.png").similar(0.79)):
            #    break
            #else:
                type(Key.DOWN)
                sleep(0.1)
        

    #sleep(3)
    keyUp(Key.SHIFT)# let the shift go, it is already selected

    click("1493854906119.png")#place them all in epicrisis
    sleep(0.3)
    click("1493912629787.png")
    click("1493912659217.png")
    
    