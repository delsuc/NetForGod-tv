# README #

# the NetForGod program
This repository contains the code which handles the www.netforgod.tv film repository.

The system is supposed to work on two independent machines

### the postproduction machine
 * It produces the various videos and sound files independently
   * for sounds : *.wav $\Rightarrow$ *.ac3 $\Rightarrow$ *.mp3
   * for video *.mp' $\Rightarrow$ *.HD $\Rightarrow$ *.avi
      * .HD is a .mp4 containing a 720p version of the source
 * this code is run periodically by cron to prepare the video and sounds file
 * this is mostly a large `Makefile` program, it relies heavily on `ffmpeg` to realise is task
 * the files are then copied using rsync on the Web server.

  
### the WebServer machine that distributes the films in their final form, both flv or avi.
 * A large `Makefile/Python` program is run periodically through cron which :
   * finalizes the video
     * join the language audio tracks to the video track and produces a film for each language
     * produces lowres *.flv files from the *.avi
   * produces the static html files that present the site
   * computes statistics
 * a set of `PHP` programs that handle the back-office

# The code distributed here is composed in several parts
 * the code of **prostproduction** machine is found here in the `prostproduction` directory
 * the code of the **WebServer** is found in the `WebServer` directory.
 * the code of the back-office is in the `www` sub-directory.
 

# Set-Up
For the **WebServer**

* the file `WebServer/configuration.sh` should be adapted to your needs
* the languages used by the prgm should be defined fully in `WebServer/langues.py`
* then run the `deploy.sh` script and all should be set, along with dependencies computed from both files above.

The organsation on the disk is as follows :

    WebServer/   - the program
        ... all program files ...
        www/  the distributed copy of the live WEB site, copied over during deployment
    www/ the Web site
        videos - all the films are in there, protected and not directly accessible
        VOD    - the main site,
            index.php
            links to the *.flv files into ../VOD
        css
        html
        images      - static pictures
        index.php   - redirecting to VOD/index.php
        js          - all the js scripts
        pdf         - pdf doc
        s           - all the php scripts
        prgm        - the backoffice
        
The video is  jw_flvplayer.swf

and a picture browser `viewer.swf` is used : http://www.airtightinteractive.com/simpleviewer/

Additional doc can be found in the file `WEB_Server / www / prgm / doc.php`
This is the live documentation of the back-office (probably a bit out-dated)