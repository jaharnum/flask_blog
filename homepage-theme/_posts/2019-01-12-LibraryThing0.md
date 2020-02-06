---
layout: post
title:  "LibraryThing Book Catalogue: Title grabbing with Python"
date:   2019-01-12
excerpt: My task: To take a 101 page long pdf exported from Library Thing and extract all the titles and authors into a neat list
project: true
feature: assets/img/postimg/LibraryThing.PNG'
tag:
- python
- data
- jupyter
---

> Oliver, [10.01.19 11:17] <br>
how easy would it b <br>
to export a library catalogue into a checklist <br>
i suppose i could just print it <br>
i need to see which books are actually still here lmao <br>
i need a thing where i can physically mark it off <br>
or else i will b confused

>Oliver, [10.01.19 11:35] <br>
1300 titles `@_@` <br>
printing would have been 101 pages rip <br>
write me a script <br>

>Jamie, [10.01.19 11:36] <br>
uh <br>
i probably could tbh <br>
send me a link to it

I guess there are some benefits to dating a programmer in training! :P

My task: To take a 101 page long pdf exported from Library Thing and extract all the titles and authors into a neat list that could be used to check what books were still around at my partner's workplace.

Since I was just looking for a quick solution, I quickly realized it would be much easier if I converted the pdf to another format rather than trying to download a new tool. I still want to learn to read directly from pdfs another time, but in this case it was a lot faster to export as a .txt document so I could handle it right away.

Since I'm practicing using Python for data analysis and manipulation right now anyways, I decided to go ahead and use a Jupyter notebook to work out a solution.

Luckily for me, a previous organizer of this catalogue assigned each book a code in the format ABC A12 - that is, three capital letters, a space, one capital letter, and two digits. Or, if you prefer going directly to the regex:

`([A-Z][A-Z][A-Z]\s[A-Z][0-9][0-9])`

It took some messing around with the formatting after I'd captured all the titles in order to capture the author's information as well. I ended up taking the first four lines following a regex match for best results. I also got a few "tags" in some of the shorter titles, but I still ended up with a nicely formatted list:

`ACT A01 Globalize Liberation : How to Uproot the System and Build a Better World 2003 activism,  
ACT A02 Take It Personally: How to Make Conscious Choices to Change the World Anita Roddick 2001 activism,  
ACT A03 Ideas for Action : Relevant Theory for Radical Change Cynthia Kaufman  
ACT A04 Another World Is Possible If.. Susan George 2004 activism, education, political  
ACT A05 Imagine Democracy Judy Rebick 2000 activism, democracy, political theory, citizenship,  
ACT A06 Marxism and Politics Ralph Miliband 2003 activism, Marxism, socialism, political theory, class struggle, working  
ACT A07 No Surrender: Writings From An Anti-Imperialist Political Prisoner David Gilbert 2004 activism, antiimperialism,  
ACT A09 The Growth of Philosophical Radicalism Elie Halevy 1955 philosophy, Jeremy Bentham, John  
ACT A10 Voice of Dissent: A Collection of Articles from Dissent Magazine Dissent  `
{: .notice}

I think from here it might be fun to make some data visualizations of what tags are used most frequently, the span of years the catalogue covers, or something like that. I could also refine my title captures a little by excluding everything that comes after the year, since it appears that most of the entries include the year of publication.

It was a really quick little project that only took me about half an hour to figure out, but it made me really happy being able to find an easy solution for my partner's problem!

<div markdown="0"><a href="https://github.com/jaharnum/BookListHandler" class="btn btn-info">Check out this project on GitHub!</a></div>
