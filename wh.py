def workhours(wh):
    if wh < 4:  #less than 4 hours
        msg = "No breaks"
        ph = wh
        return msg, ph

    elif (wh >= 4 and wh < 5):  #bw 4 hours to less than 5 hours
        msg = "You get one 15 min break"
        ph = wh
        return msg, ph

    elif (wh >= 5 and wh <= 7):  #bw 5 to 7 hours
        ph = wh - 0.5
        msg = "You get one 15 min break and one 30 min break"
        return msg, ph

    elif (wh > 7 and wh < 9):  #More than 7 hours, less than 9 hours
        msg = "You get one 15 min break and one 1 hour break"
        ph = wh - 1
        return msg, ph

    elif (wh >= 9):  #9 hours or more
        msg = "You get two 15 min breaks and one 1 hour break"
        ph = wh - 1
        return msg, ph
