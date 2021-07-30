import numpy as np
import cv2


def f(im, n=1, v=0.2, L=2, t=0):
    x = np.linspace(0, L, 2001)
    func = np.sin((n * np.pi * x) / L) * np.cos((n * np.pi * v * t) / L)

    ww2 = int(win_w / 2)
    wh2 = int(win_h / 2)
    scale = 100

    for i in range(len(x)):
        ix = x[i]
        iy = func[i]

        p = (int(ww2 + ix * scale), int(wh2 + iy * scale))

        cv2.circle(im, p, 1, (255, 255, 255))


win_w = 640
win_h = 480

# params={
# "n":(0, 10, 1),
# "v":(0.2, 5, 0.1),
# "L":(0.2, 2, 0.1),
# "t":(0, 10, 1)
# }

params = {
    "n": [10],
    "v": [5],
    "L": [2],
    "t": [0]
}

while True:

    im = np.zeros((win_h, win_w, 3), dtype="uint8")
    for i in range(len(params["n"])):
        n = params["n"][i]
        v = params["v"][i]
        L = params["L"][i]
        t = params["t"][i]

        f(im, n, v, L, t)
        cv2.imshow("f", im)

    k = cv2.waitKey(33) & 0xFF
    if k == ord('q'): break

    # Parameter setting with the keyboard

    # comment / uncomment this for animation:
    params["t"][0] += .001

    # n param setting +,- use n,b
    if k == ord('n'): params["n"][0] += .001
    if k == ord('b'): params["n"][0] -= .001

    # v param setting +,- use v,c
    if k == ord('v'): params["v"][0] += .001
    if k == ord('c'): params["v"][0] -= .001

    # L param setting +,- use l,k
    if k == ord('l'): params["L"][0] += .001
    if k == ord('k'): params["L"][0] -= .001

    # t param setting +,- use t,r
    if k == ord('t'): params["t"][0] += .001
    if k == ord('r'): params["t"][0] -= .001

    print(params)

cv2.destroyAllWindows()