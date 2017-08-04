def point_inside(p_x, p_y, b_x, b_y, b_w, b_h):
    return ((p_x >= b_x) and (p_x <= b_x + b_w) and (p_y >= b_y) and (p_y <= b_y + b_y))

def box_collision(x1, y1, w1, h1, x2, y2, w2, h2): # Remember (0, 0) is UPPER left corner
    top1 = y1
    bot1 = y1 + h1
    left1 = x1
    right1 = x1 + w1
    
    if (point_inside(top1, left1, x2, y2, w2, h2) or
        point_inside(top1, right1, x2, y2, w2, h2) or
        point_inside(bot1, left1, x2, y2, w2, h2) or
        point_inside(bot1, right1, x2, y2, w2, h2)):
        return true
    else:
        return false