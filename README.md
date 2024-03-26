happy-sad-angry by Augustine M.
Last updated 3/26/24

This is a program that locates my face and classifies it as happy, sad, or angry, based on the YOLOv5m6 computer vision model.
Due to the rather diminutive training dataset, the model is quite bad, and only works for my face with proper lighting conditions.
Maybe I'll gather more data later and make it better. For now, it is what it is.

NOTE 0: Do not use this. It only works on my face. Really, there is no reason for you to use this.
NOTE 1: the python program will create a new folder called test and save images to it when using the single-image-saving mode.
NOTE 2: prereqs? I'll figure it out later, but if you go to run it and see that something is missing then you should probably get that thing.
NOTE 3: if you already have a .pt file that you would like to use with this program, you could just replace "best.pt" for it (and also call it best.pt).
  Only caveat is that it might not be perfectly compatible with the way the happySadAngry.py script is written.

Applications:
  As an occasional game developer, it might be funny to have the game get harder when the user is angry/not detected compared to when they are happy.
  Oh and also maybe pause the game if a user is not seen for a while.
  Honestly, I didn't think of how this could be helpful before I did it, I just did it and it worked a bit.
