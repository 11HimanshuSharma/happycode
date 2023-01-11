import pyqrcode

def qrcode():
  q = pyqrcode.create(input())
  q.jpeg("ile.png",scale=6)
  print("Qr generated")

if __name__=="__main__":
  qrcode()