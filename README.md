# Django-IRC-Logs

IRC logs from #django 
Raw data from `#dango` and `#django-dev`.  This is a superset of the training data for the bot.

## Usage

Clone this repo, `cd` into it and run `python3 extractor.py`.  This will:
* Untar the files
* Create a CSV for `#django` and `#django-dev`
* Parse out channel activity, like joins and departs
* Merge all channel daily message activity into a CSV with `year`, `time`, `user` and `message` columns.

## About

The log files come in a tarball we had to pull from an IRC bouncer.  We tried getting access to the long
term historical data from [botbot.me](https://botbot.me/freenode/django/), but were met with no replies.  
We are still working on this.

These were pulled off a bouncer we had set up for a little over a year and a half.  This isn't a complete
list, but we thing it is enough for now.