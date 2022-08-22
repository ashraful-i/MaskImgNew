# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PIL import Image
from os import listdir
from os.path import isfile, join
import pandas as pd
from glob import glob


def read():
    mypath = "D:\ibtd\ibtd\Mask"
    maskImages = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    R_skin = [0 for x in range(256)]
    G_skin = [0 for x in range(256)]
    B_skin = [0 for x in range(256)]
    Skin_RGB = [[[0 for x in range(256)] for y in range(256)] for z in range(256)]
    total_skin = 0
    for maskimg in maskImages:
        # print(maskimg)
        im = Image.open(mypath + "\\" + maskimg)
        pix = im.load()
        im_w = im.size[0]
        im_h = im.size[1]
        # print(im_h, im_w)

        for x in range(im_w):
            for y in range(im_h):
                Blue = pix[x, y][2]
                Green = pix[x, y][1]
                Red = pix[x, y][0]
                Skin_RGB[Red][Blue][Green] += 1
                if Red == 255 and Blue == 255 and Green == 255:
                    continue
                else:
                    R_skin[Red] += 1
                    G_skin[Green] += 1
                    B_skin[Blue] += 1
                    total_skin += 1
    print(R_skin)
    non_skin = "D:\ibtd\ibtd\Test"
    non_skin_Images = [f for f in listdir(non_skin) if isfile(join(non_skin, f))]
    Non_Skin_RGB = [[[0 for x in range(256)] for y in range(256)] for z in range(256)]
    total_non_skin = 0
    R_nskin = [0 for x in range(256)]
    G_nskin = [0 for x in range(256)]
    B_nskin = [0 for x in range(256)]
    for non_s in non_skin_Images:
        # print(maskimg)
        im = Image.open(non_skin + "\\" + non_s)
        pix = im.load()
        im_w = im.size[0]
        im_h = im.size[1]
        # print(im_h, im_w)

        for x in range(im_w):
            for y in range(im_h):
                Blue = pix[x, y][2]
                Green = pix[x, y][1]
                Red = pix[x, y][0]
                Non_Skin_RGB[Red][Blue][Green] += 1

                R_nskin[Red] += 1
                G_nskin[Green] += 1
                B_nskin[Blue] += 1
                total_non_skin += 1
    print(R_nskin)
    Rb = list(range(0, 256))
    Gb = list(range(0, 256))
    Bb = list(range(0, 256))
    df = pd.DataFrame()
    R_t = list()
    G_t = list()
    B_t = list()
    S_NS = list()
    for R in Rb:
        for G in Gb:
            for B in Bb:
                R_t.append(R)
                G_t.append(G)
                B_t.append(B)
                # probab = ((Skin_RGB[R][G][B])/total_skin)/((Non_Skin_RGB[R][G][B])/total_non_skin)
                probab = ((R_skin[R] * G_skin[G] * B_skin[B]) / (total_skin * total_skin * total_skin)) / (
                        (R_nskin[R] * G_nskin[G] * B_nskin[B]) / (total_non_skin * total_non_skin * total_non_skin))
                S_NS.append(probab)
    df = pd.DataFrame()
    df['R'] = R_t
    df['G'] = G_t
    df['B'] = B_t
    df['Probab'] = S_NS
    df.to_csv("skin_db.csv", sep='\t')


def read2():
    mypath = "D:\ibtd\ibtd\Mask"
    maskImages = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    R_skin = [0 for x in range(256)]
    G_skin = [0 for x in range(256)]
    B_skin = [0 for x in range(256)]
    Skin_RGB = [[[0 for x in range(256)] for y in range(256)] for z in range(256)]
    total_skin = 0
    for maskimg in maskImages:
        # print(maskimg)
        im = Image.open(mypath + "\\" + maskimg)
        pix = im.load()
        im_w = im.size[0]
        im_h = im.size[1]
        # print(im_h, im_w)

        for x in range(im_w):
            for y in range(im_h):
                Blue = pix[x, y][2]
                Green = pix[x, y][1]
                Red = pix[x, y][0]
                Skin_RGB[Red][Blue][Green] += 1
                if Red == 255 and Blue == 255 and Green == 255:
                    continue
                else:
                    R_skin[Red] += 1
                    G_skin[Green] += 1
                    B_skin[Blue] += 1
                    total_skin += 1
    print(R_skin)
    non_skin = "D:\ibtd\ibtd\Test"
    non_skin_Images = [f for f in listdir(non_skin) if isfile(join(non_skin, f))]
    Non_Skin_RGB = [[[0 for x in range(256)] for y in range(256)] for z in range(256)]
    total_non_skin = 0
    R_nskin = [0 for x in range(256)]
    G_nskin = [0 for x in range(256)]
    B_nskin = [0 for x in range(256)]
    for non_s in non_skin_Images:
        # print(maskimg)
        im = Image.open(non_skin + "\\" + non_s)
        pix = im.load()
        im_w = im.size[0]
        im_h = im.size[1]
        # print(im_h, im_w)

        for x in range(im_w):
            for y in range(im_h):
                Blue = pix[x, y][2]
                Green = pix[x, y][1]
                Red = pix[x, y][0]
                Non_Skin_RGB[Red][Blue][Green] += 1

                R_nskin[Red] += 1
                G_nskin[Green] += 1
                B_nskin[Blue] += 1
                total_non_skin += 1
    print(R_nskin)

    im = Image.open("man.jpg")
    pix = im.load()
    im_w = im.size[0]
    im_h = im.size[1]
    # print(im_h, im_w)
    print("check")
    for x in range(im_w):
        for y in range(im_h):
            Red = pix[x, y][0]
            Green = pix[x, y][1]
            Blue = pix[x, y][2]
            probab = ((R_skin[Red] * G_skin[Green] * B_skin[Blue]) / (total_skin * total_skin * total_skin)) / (
                    (R_nskin[Red] * G_nskin[Green] * B_nskin[Blue]) / (
                    total_non_skin * total_non_skin * total_non_skin))
            if (probab > 1):
                pix[x, y] = (0, 0, 0)
    im.save("probab.jpg")
    im.close()


def make_dataset():
    mask_img_path = "D:\ibtd\ibtd\Mask"
    img_path = "D:\ibtd\ibtd\Test"


    mask_img_file_list = glob(mask_img_path + "\*")
    img_file_list = glob(img_path + "\*")

    total_images = len(img_file_list)
    RGB_S = []
    for cnt_img in range(total_images):
        print(cnt_img)
        im_main = Image.open(img_file_list[cnt_img])
        im_mask = Image.open(mask_img_file_list[cnt_img])
        pix_main = im_main.load()
        pix_mask = im_mask.load()
        im_main_w, im_main_h = im_main.size
        for x in range(im_main_w):
            for y in range(im_main_h):
                Blue_mask = pix_mask[x, y][2]
                Green_mask = pix_mask[x, y][1]
                Red_mask = pix_mask[x, y][0]

                #print("B G R "+ str(Blue) +" "+str(Green)+" "+str(Red)+"\n")
                if Blue_mask == 255 and Green_mask == 255 and Red_mask == 255:
                    Blue_main = pix_main[x, y][2]
                    Green_main = pix_main[x, y][1]
                    Red_main = pix_main[x, y][0]
                    rgb_nskin = []
                    rgb_nskin.append(Blue_main)
                    rgb_nskin.append(Green_main)
                    rgb_nskin.append(Red_main)
                    rgb_nskin.append(1)
                    RGB_S.append(rgb_nskin)
                else:
                    rgb_skin = []
                    rgb_skin.append(Blue_mask)
                    rgb_skin.append(Green_mask)
                    rgb_skin.append(Red_mask)
                    rgb_skin.append(2)
                    RGB_S.append(rgb_skin)
        im_main.close()
        im_mask.close()
    df_skin = pd.DataFrame(RGB_S, columns=['B', 'G', 'R', 'Skin'])

    print(df_skin.shape)


    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # read2()
    make_dataset()
