MFC Sales App
=============================

I created this site for my last job, working as a bookkeeper for MFC Office, which was an office furniture dealer. I created this site so that Sales Reps would have an easy way to quick-look up the cost and sell prices of different pieces of furniture. MFC Office has since gone out of business. I removed the actual inventory of furniture (since those vendors are still around and I wouldn't want to display any information I shouldn't) and added a few fake companies with a couple of items each, but when this site was active I had 8 different vendors loaded with over 15,000 items.

The landing page for the site has a quick sales tax lookup to and the option to select from two views: MFC or Customer. THe customer view is for when the sales rep was working with a customer so the information shown is limited. The MFC view has confidential information, such as the original cost and MFC's mark-up of the items, so it required a login. The dummy login is now login:test, password:test, which you may use to see how the confidential site differs. Once you are on the confidential pages, the background colors flip, as a visual cure of where you are.

Once past the login page, you can either view a vendor information sheet, or lookup items by vendor. All of this information, and the sales tax from the landing page, is all held in a PostgreSQL database. Each vendor currently only has two items, just click space on the form field and the options will show. I used an app called autocomplete_light to make it so that the fields show you all options as you type.

This site uses mainly Python with the Django web-framework and a little HTML and CSS.

View the live site hosted on Heroku:

http://mfcoffice.herokuapp.com/
