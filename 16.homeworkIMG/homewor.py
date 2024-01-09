from PIL import Image

img1 = Image.open('mask.png')
img2 = Image.open('word_matrix.png')
img1 = img1.resize(img2.size)
# mask = img1.split()[3]  
img1.putalpha(200)
img2.paste(img1, (0, 0), img1)

img2.save("secret.png")