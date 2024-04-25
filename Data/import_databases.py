# code from https://github.com/buomsoo-kim/buomsoo-kim.github.io/blob/master/_posts/2018-04-16-Importing-files-from-Google-Drive-in-Google-Colab.md.md

import gdown

ids=["1nF6BqS2jMGEapfR0lGJ_7Eauc7zu-DDx", "12X2Rz6D0aTbUVHuEXmEp7GTBfhIxLagI", "1p9ndW7-FeZVVfxvCGNlF7-8K7Qi6wVOZ"]
outputs=['NIHCXR.npy', 'COVIDGR_1.0_N.npy', 'COVIDGR_1.0_P.npy']

for i in range(len(ids)):
    gdown.download(id=ids[i], output=outputs[i])


##to access the key and value from the compressed npy, after downloading it to your computer:
#df_nihcxr = np.load("Data/NIHCXR.npy", allow_pickle = True)
        #df_nihcxr_dict = df_nihcxr.item()
#key_1st = list(df_nihcxr_dict.values())[0]
#value_1st = df_nihcxr_dict[key_1st]
#plt.imshow(value_1st)




