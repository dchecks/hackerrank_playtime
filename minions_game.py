def minion_game(string):
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']
    k_dawg = 0
    s_dawg = 0

    s_len = len(string)
    for s_ptr, ch in enumerate(string):
        if ch in vowels:
            # Kevin
            k_dawg += s_len - s_ptr
        else:
            # Stuart
            s_dawg += s_len - s_ptr

    if k_dawg > s_dawg:
        print("Kevin %s" % k_dawg)
    elif k_dawg < s_dawg:
        print("Stuart %s" % s_dawg)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)