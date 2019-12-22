#### Control camera behaviour from MedPC input/outputs

![alt-text-1](images/operant_gif.gif "operant camera control")

* Controls [White Matter](https://white-matter.com/) cameras through http [requests](https://realpython.com/python-requests/) and [json](https://docs.python.org/3/library/json.html)
* Each MedPC control box is connects to a [24V-5V optocoupler](https://www.amazon.com/dp/B07NNP4H7S/ref=cm_sw_r_tw_dp_U_x_Co5.DbJ6NHHB8) which output runs to an [Arduino mega](https://www.amazon.com/dp/B01H4ZLZLQ/ref=cm_sw_r_tw_dp_U_x_sq5.DbM8QDZ1X)
* The  pins are read by the arduino script and parsed by [PySerial](https://pythonhosted.org/pyserial/)
* The cameras turn on when 5V is coming out of the optocopler.
* Press q to disconnect all cameras when session is complete. 
* Displays camera status, last onset and offset times, and the number of recorded sessions in terminal window 
* Recording example on [YouTube](https://youtu.be/vqdYUS3bM68)






 

   


 
 


  
