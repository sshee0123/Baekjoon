def solution(sizes):
    answer = 0
    mw, mh = 0, 0
    for w, h in sizes:
        if w < h:
            w, h = h, w
        mw = max(mw, w)
        mh = max(mh, h)
    answer = mw * mh
    return answer