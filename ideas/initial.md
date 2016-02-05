
  The idea is to make a new set-up of the netforgod WEB site and of the video pipe-line, 
  better for the visitors, and easier to maintain for brothers.

# what we currently have

Currently we have two machines

 - saul4 - located in 59
 - netforgod.tv

with on saul4

 - the in-house part of the video pipeline for production : `make / python`
 
 on  netforgod.tv

 - the remote part of the video pipeline for production : `make / python`
 - the site generator  : `python`
 - the generated site `html-static / php / js`
 - backoffice on netforgod.tv : `php`

# What I propose

 - improve the web-site
 - Keep the python technology (much safer and robust than PHP)
 - use more standard techniques

### for the pipelines
The current flow is based on `make`.
This tool allows to compute only incremental changes without recomputing everything evry time.
This is excellent for the video, as any change on the sound-track, on the video or on the texts is repercuted on the final filmM
However `make` is an old techno, efficient but difficult to understand and maintain,
we should change `make` by `doit` both on saul4 and netforgod.tv

See documentation:

 - doit web site: http://pydoit.org/contents.html
 - doit doc: http://swcarpentry.github.io/bc/intermediate/doit/01-doit_basics.html

### for the static pages
Currently the HTML code is generated hourly by a home-made generator in python, based on simplistic template system.
This should be replaced (it did not exist when I wrote the code).

There are now many static generators, for instance (to site only python based ones)

- pelican https://github.com/getpelican/pelican
- nikola https://github.com/getnikola/nikola
- cactus https://www.staticgen.com/cactus

there is a comparator here: https://www.staticgen.com/  
or here http://www.tummy.com/blogs/2013/02/09/a-quick-review-of-python-static-site-generators/
or here https://wiki.python.org/moin/StaticSiteGenerator

I have a clear preference for nikola

### comparaisons

| my_idea | name | multilangue | template | markdown | build | backOffice |
| -------- | --- | ----------- | -------- | -------- | ----- | ------- |
| oui    | Pelican | X         | Jinja2   | X        | ?     | ? |
| ?      | Lektor  | ?         | Jinja2   | X        | X     | X |
| ?      | Hyde    | ?         | Jinja2   | ?        | ?     | ? |
| **oui**| Nikola  | X         | Jinja2   | X        | X doit| ? |



# What has to be done - in details -
I propose the following plan:

**in General**

 1. improve the web site organisation for better viewing/download
 2. improve the graphic chart of the site
 3. Rewrite the code for easier maintenance

**In particular:**

  - change the viewer from flash to html5/mp4
  - generate HD video files
     - for download
     - for VOD (video on demand : on-line viewing )
  - replace `make` by `doit`
  - replace boiler plate python code by Nikola
  - try to improve the back Office
 
 
 This means the following tasks, here in decreasing order of urge

## 1st HD video
### for download
We want to provide HD video.
Since about a year ago, a HD master is already generated in 720p, and transmited from saul4 to netforgod.tv
So the material is on the site, it just has to be built and made available.


still required (some of this is already in progress, or even nearly done)

- genererate muxed HD video (mixing video and langage)
- adapt the download page for choosing the version
- write some documentation for the download
- implement the "flush" - MUCH REQUIRED - (as for each film, there will be about 4 resolution and ~20 languages; that about 15Gb to 20Gb - we cannot keep every thing on disk

### for VOD

- generate lower resolutions, probably 480p and 360p
  - and check them ! I got a lot of problems with that
  - propagate for older films
- adapt HWPlayer to be in HTML5/MP4 mode rather than flash - MUCH REQUIRED !
    - check on all browers and OS :
        - Windows7 / 8.1 / 10 / macOS / Linux
        - Firefox / Chrome / Safari / iOS / Android
- adapt the viewing pages so that the user can choose the version
  - I tried to implement the choice in JWPlayer, I could not have it working !


## 2nd rewrite the web-site generator
The actual site is a static one, generated incrementally.
The generator itself is a large set of python code, the incremental part is taken by a make/Makefile program.
There is a second part that takes care of muxing the films, and generating the lower resolutions.

This was created about 10 years ago, in a time when static generators where unknown, and no code was available.
It still is running fine 10 years after, but it has to be changed for several reasons

 - make/Makefile is powerfull but cryptic, and few people know how to handle it
 - the python code is too large and difficult to improved
 - using modern/standard tools/templates will allow a better maintenance

This is what we have to do

 - move the current HTML set-up (and/or the improved one from task above) to the `Jinja2` template
 - rewrite the generator in `Nikola`
 - rewrite the dependence list using the tool `doit`
 - improve the back-office (alas written in PHP !)
 - correct the old bug of problematic onwership....

## 3rd on saul4

 - ffmpeg is still running there, every thing is fine, should not change it
 - replace the large Makefile by a doit program
