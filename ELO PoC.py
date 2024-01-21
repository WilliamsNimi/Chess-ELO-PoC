"""Script for ELO calculations for chess"""
def win_prob(p_rating1, p_rating2):
    """Calculate win probability"""
    p1_diff = p_rating2 - p_rating1
    p2_diff = p_rating1 - p_rating2
    power1 = 10**(p1_diff/400)
    power2 = 10**(p2_diff/400)
    p1_win_prob = 1/(1+power1)
    p2_win_prob = 1/(1+power2)
    return (p1_win_prob, p2_win_prob)

def new_ELO(p1_win_prob, p2_win_prob, p1_rating, p2_rating, win):
    """Chosen K constant Values: K=32(below 2100), K=24(2100 - 2400), K=16(above 2400)"""
    if win == 1:
        p1_rating = p1_rating + 32*(1 - p1_win_prob)
        p2_rating = p2_rating + 32*(0 - p2_win_prob)
    elif win == 0:
        p1_rating = p1_rating + 32*(0 - p1_win_prob)
        p2_rating = p2_rating + 32*(1 - p2_win_prob)
    else:
        p1_rating = p1_rating + 32*(0.5 - p1_win_prob)
        p2_rating = p2_rating + 32*(0.5 - p2_win_prob)
    return (p1_rating, p2_rating)


p1_rating = 1200
p2_rating = 1800 
"""1 is a win for player 1, 0 is win for player 2, 0.5 is a draw"""
win = 0

win_probability = win_prob(p1_rating, p2_rating)
print(new_ELO(win_probability[0], win_probability[1], p1_rating, p2_rating, win))