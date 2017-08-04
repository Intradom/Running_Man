def point_inside(p_x, p_y, b_x, b_y, b_w, b_h):
    return ((p_x >= b_x - b_w / 2) and (p_x <= b_x + b_w / 2) and (p_y >= b_y - b_h / 2) and (p_y <= b_y + b_y / 2))

def box_collision(x1, y1, w1, h1, x2, y2, w2, h2): # Remember (0, 0) is UPPER left corner
    top1 = y1 - h1 / 2
    bot1 = y1 + h1 / 2
    left1 = x1 - w1 / 2
    right1 = x1 + w1 / 2
    
    if (point_inside(top1, left1, x2, y2, w2, h2) or
        point_inside(top1, right1, x2, y2, w2, h2) or
        point_inside(bot1, left1, x2, y2, w2, h2) or
        point_inside(bot1, right1, x2, y2, w2, h2)):
        return true
    else:
        return false