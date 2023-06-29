from PIL import Image
def imgshow():
    im_path = 'D:\\Pranav\\Titan I\\pinkbluebar.png'
    im = Image.open(im_path)
    im.show()
def begin():
    gif1_path = 'D:\\Pranav\\Titan I\\bar.gif'
    g1 = Image.open(gif1_path)
    g1.show()
def start_speak():
    gif2_path = 'D:\\Pranav\\Titan I\\blob.gif'
    g2 = Image.open(gif2_path)
    g2.show()

imgshow()