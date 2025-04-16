# CTF Sripts

Just a bunch of automation scripts or exploits I wrote while playing CTFs
Here mostly for re-usability (Yeah I am just that lazy).
you guessed those will be mostly in python buuut...

Some of those might be linked later to writeups (If I am not too lazy)

I write them on [zerOne](https://dev.nairolf32.com/zerOne) my cybersecurity blog.

## Usage

I could let you figure it yourself but hey... it's quite simple:

- clone the repo
- install the requirements (for all the scripts I used `pip install -r requirements.txt`)
- run the script with `python3 <script_name>.py`
- scripts are named after the challenge I am solving
- scripts are placed in subfolders corresponding to the challenge platform
- if the script requires multiple files to work (crypto challs much) I add all that in a subfolder

Also note that all scripts here are WORKING! those were used by me to solve the challenges, BUT some refining might be needed.
By example for challenges that use http requests, you might need to change the headers or the cookies or the data sent in the request,
as for security reasons should be different for each user. I don't always handle that!


## DISCLAIMER

HUGE SPOILER ALERT! If you are playing the same CTFs or solving the same challenges you should make sure to solve them yourself (or at least try a lot)
before looking at the scripts. I put these here mostly for myself (re-usability) and for educational purposes (others can compare their solutions to mine and
vice versa). DO NOT RUIN THE FUN OR THE LEARNING EXPERIENCE!
