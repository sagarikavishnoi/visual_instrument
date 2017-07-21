import cv2
import numpy as np
import winsound 
import subprocess
import os
cap =cv2.VideoCapture(0)
d=cv2.imread('Dchord.jpg',0)
a=cv2.imread('Achord.jpg',0)
g=cv2.imread('Gchord.jpg',0)
e=cv2.imread('Echord.jpg',0)
A,D,G,E=1,1,1,1
h=350
w=280
while True:
	ret,frame1 = cap.read()
	frame = frame1[w:w+100,h:h+100]
	img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	wd,hd=d.shape[::-1]
	wa,ha=a.shape[::-1]
	wg,hg=g.shape[::-1]
	we,he=e.shape[::-1]
	# print frame

	resultd=cv2.matchTemplate(img_gray,d,cv2.TM_CCOEFF_NORMED)
	resulta=cv2.matchTemplate(img_gray,a,cv2.TM_CCOEFF_NORMED)
	resultg=cv2.matchTemplate(img_gray,g,cv2.TM_CCOEFF_NORMED)
	resulte=cv2.matchTemplate(img_gray,e,cv2.TM_CCOEFF_NORMED)

	threshold=0.67

	cv2.rectangle(frame1,(w,h),(w+100,h+100),(0,0,255),4)
	
	locd=np.where(resultd>=threshold)
	loce=np.where(resulte>=threshold)
	loca=np.where(resulta>=threshold)
	locg=np.where(resultg>=threshold)

	for pt in zip(*locd[::-1]):
		#D chord
	    cv2.rectangle(frame,pt,(pt[0]+wd,pt[1]+hd),(0,0,255),3)
	    if(D):
                retval=os.getcwd()
	     	subprocess.Popen(['retval'])
	    	D=0
	    	E,A,G = 1,1,1

	for pt in zip(*loce[::-1]):
		#E chord
	    cv2.rectangle(frame,pt,(pt[0]+we,pt[1]+he),(255,0,255),3)
	    if(E):
	     	subprocess.Popen(['C:\Users\lenovo\Downloads\hackathon-20160731T091129Z\hackathon\Emajor.wav'])
	    	E=0
	    	D,A,G = 1,1,1
	
	for pt in zip(*loca[::-1]):
		#A chord
	    cv2.rectangle(frame,pt,(pt[0]+wa,pt[1]+ha),(0,255,255),3)
	    if(A):
	     	subprocess.Popen(['C:\Users\lenovo\Downloads\hackathon-20160731T091129Z\hackathon\Amajor.wav'])
	        A=0
	    	E,D,G = 1,1,1 

	for pt in zip(*locg[::-1]):
		#G chord
	    cv2.rectangle(frame,pt,(pt[0]+wg,pt[1]+hg),(156,156,255),3)
	    if(G):
	     	subprocess.Popen(['C:\Users\lenovo\Downloads\hackathon-20160731T091129Z\hackathon\Gmajor.wav'])
	    	G=0
	    	E,A,D = 1,1,1    	   	    	


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	# winsound.PlaySound('song.wav', winsound.SND_FILENAME)
	cv2.imshow('frame',frame1)

	#w insound.PlaySound("song.wav", winsound.SND_FILENAME)


# cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()