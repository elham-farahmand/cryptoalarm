import cryptocompare
from time import sleep
from pygame import mixer
import pyttsx3

mixer.init()
engine = pyttsx3.init()
low_thresh = int(input('Enter low threshhold: '))
high_thresh = int(input('Enter high threshhold: '))
threshhold = int(input('Enter threshhold: '))

while True:
    price = cryptocompare.get_price('BTC', currency='USD')['BTC']['USD']
    if ( price < low_thresh ):
        print('Bitcoin price went low! New price: %i' % price)
        high_thresh -= threshhold
        low_thresh -= threshhold
        mixer.music.load('alarm1.mp3')
        mixer.music.play()
        engine.say('Bitcoin is %i' % price)
        engine.runAndWait()

    elif ( price > high_thresh ):
        print('Bitcoin price went high! New price: %i' % price)
        high_thresh += threshhold
        low_thresh += threshhold
        mixer.music.load('alarm2.mp3')
        mixer.music.play()
        engine.say('Bitcoin is %i' % price)
        engine.runAndWait()

    else:
        print(low_thresh , '<' , price , '<' , high_thresh)
        
    sleep (5)

        
