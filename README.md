Welcome to this MASTERMIND game created by Martin Zadora, Alphonse Raynaud, Kilian Bujon and Naël Godefroy.


### Setting up the app.

Make sure Flask is installed on your computer. 
You can create a virtual environment with Flask and play the game through it.

Once flask is installed, go into the game folder and launch the app :
$ python app.py

This should prompt a message, telling you that it is running on http://127.0.0.1:5000 .

Open http://127.0.0.1:5000 in your browser, and play!

Use Control-C to stop the server.


### Playing

You have to type in colour names in letters.
Right now, the winning combination is set to 'green, green, yellow, yellow'.

Here's how to interpret pegs (aka. indications) : if you get
'green blue green orange => => => red empty empty white'
this means that you got the first green one correct and that one of the others is orange.

Please refer to the game documentation available online if you don't understand pegs.