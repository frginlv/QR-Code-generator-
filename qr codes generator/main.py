import qrcode

while True:
    link=input("Enter the Website's url : (Example: google.com) ") #siteweb url/link
    img_dir='./qr codes generator/qrcode.png'  #hna kat7et directory
    
    #img=qrcode.make(url)  #hna kat3ti link l qrcode module
    #img.save(img_file)  #hna kat3ti qrcode module directory fin y7t l output
    
    #advanced/detailed usage of the module
    qr = qrcode.QRCode()
    qr.add_data(link)
    img = qr.make_image(fil_color="black" ,back_color="white")
    img.save(img_dir)