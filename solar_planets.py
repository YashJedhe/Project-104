import cv2

img=cv2.imread("solar-system.jpg")




cv2.putText(img,
            "Sun",
            (90,50),
            cv2.FONT_HERSHEY_COMPLEX,
            1.0,
            (255,0,0)
            )

cv2.putText(img,
            "Mecury",
            (110,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Venus",
            (190,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Earth",
            (290,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Mars",
            (390,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (490,355),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Saturn",
            (690,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Uranus",
            (950,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Neptune",
            (1100,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Moon",
            (310,160),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)
            )

cv2.imshow("output",img)
cv2.imwrite("Solar_systemwithname.jpg",img)
cv2.waitKey(0)