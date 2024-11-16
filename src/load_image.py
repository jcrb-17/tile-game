import cv2

size = 300

if __name__=="__main__":

    a,b,c = size//3,(size//3)*2,(size//3)*3
    # print(a,b,c)
    # assert that size %3 == 0

    img = cv2.imread("image.png")
    # print(img.shape)
    img = cv2.resize(img,(size,size))
    # print(img.shape)

    # cv2.imwrite("image2.png",img)

    #make subdivisions
    s1 = img[0:a,0:a]
    s2 = img[0:a,a:b]
    s3 = img[0:a,b:c]

    s4 = img[a:b,0:a]
    s5 = img[a:b,a:b]
    s6 = img[a:b,b:c]

    s7 = img[b:c,0:a]
    s8 = img[b:c,a:b]
    # s9 = img[0:100,0:100]

    sections = [s1,s2,s3,s4,s5,s6,s7,s8]
    for i in range(len(sections)):
        cv2.imwrite("imgs/{}.png".format(i+1),sections[i])

# for i in dir(cv2):
    # print(i)
# print(dir(cv2))
