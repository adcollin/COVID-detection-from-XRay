# code from https://github.com/buomsoo-kim/buomsoo-kim.github.io/blob/master/_posts/2018-04-16-Importing-files-from-Google-Drive-in-Google-Colab.md.md

import gdown

ids=["1nF6BqS2jMGEapfR0lGJ_7Eauc7zu-DDx", "12X2Rz6D0aTbUVHuEXmEp7GTBfhIxLagI", "1p9ndW7-FeZVVfxvCGNlF7-8K7Qi6wVOZ"]
outputs=['NIHCXR.npy', 'COVIDGR_1.0_N.npy', 'COVIDGR_1.0_P.npy']

for i in range(len(ids)):
    gdown.download(id=ids[i], output=outputs[i])
