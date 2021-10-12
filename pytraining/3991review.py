"""
- create instances of web pages with title and desc (already done)
- create web users with name, email and level (inherit from People)
- create web sites made up of a site name, web page instances and webuser instances
  (e.g. a list of pages and a list of users)
- The website should be able to derive how many pages and how many users
  (i.e. read-only properties that return the len() of the pages or users list)

Aim for modular code, where we declare classes in their own modules and import to a 

main module

Make sure webusers and websites have methods which can nicely print their details
(this can be in any way you like, but probably using the .format() method )
E.g. the Webuser class could override the existing 'showme()' method of Person

Add a method to your Website class which will write details out to a file
This should append the pages and users of the site as text (i.e. 'at' )

At least one of your classes should have get/set methods for it's properties
(use the setter method to validate the property before setting it)

Write immediate code to create and exercise some class instances
e.g. instantiate a few users and a few webpages
Then instantiate a website and use your pages and users as properties of this new 

web site instance

Optional
--------
Validate that the web user 'level' property is only ever one of these values:
	['guest', 'admin', 'owner']
Every time a web page or a web user is created, append their details to a text file
Write a class which can read in this log file and present the results in a nice way
If any setter method fails validation, write the nature of the problem to a text file.
Provide a way for this file to be read and displayed
"""

from webmodule import webpage as wp
from webmodule import webuser as wu

pages = []
users = []

pages.append(wp.WebPage('Home', 'Welcome to our website'))
pages.append(wp.WebPage('About Us', 'Information about our company'))
pages.append(wp.WebPage('Products', 'Our product offering'))
pages.append(wp.WebPage('Contact Us', 'How to get in touch'))
pages.append(wp.WebPage('Legal', 'The legal bits'))

for i in range(0,len(pages)):
    pages[i].logWebPageDetail()

users.append(wu.WebUser('Toby','toby@pycourse.org','Owner'))
users.append(wu.WebUser('Aimee','aimee@pycourse.org','Admin'))
users.append(wu.WebUser('Bharath','bharath@pycourse.org','Guest'))
users.append(wu.WebUser('Diego','deigo@pycourse.org','Guest'))
users.append(wu.WebUser('Sara','sara@pycourse.org','Guest'))
users.append(wu.WebUser('Tushar','sara@pycourse.org','Admin'))

for j in range(0,len(users)):
    users[j].logWebUserInfo()

