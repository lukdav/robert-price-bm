# Robert Price Builders' Merchants

The construction industry has never been busier with growth year on year. Material suppliers and merchants have also advanced their strategies to cater to a greater market with online stores. UK national businesses have, perhaps, had an advantage as product availability and a greater number of store locations made such delieries more feasible. However as smaller and more local companies develope their strategies, it may be possible to compete with the larger companies with savvy techniques to overcome the disadvantages initially preventing an online presence.

Robert price Builders' Merchant is a real company and have given permission to use their name, logo and images for this demonstration. Robert Price Bilders' Merchants have recently commissioned a new website and are in the process of populating it with current images and information. They are hoping the new website will go live in the near future, however without an e-commerce aspect as the complications present a substantial hurdle.

I will plan, code and implement a website for an e-commerce store for Robert Price Builders' Merchants. The website will be linked to a database containing all of the products, the categories and users associated with it. A user must be able to view and buy products, while a superuser will be able to create, edit and delete items within the database. The additional functionality of adding, updating and deleting categories will also be considered but may be out of the scope for this project due to time constraints.
---
## Demo

The demonstration website can be viewed here - [Robert Price Builders' Merchants](https://robert-price.herokuapp.com/)

The GitHub repository can be seen here - [lukdav/robert-price-bm](https://github.com/lukdav/robert-price-bm)

## UX

The website will be targetted at DIY, professional builders and trade/account users to make buying and ordering products an easy and fast process.

- Users will be able to view products in a number of categories. They will be able to see the image, name, price, size and rating of the product, with a product description and the ability to buy the item from an individual product page.

- Registered users will have the ability to make an account to view previous orders and save delivery details.

- Admin and users with admin priveledges will have the ability to add, edit and delete products.

#### User Stories

As a shopper I want to:

- View a list of products to purchase.
- View a specific category of products in order to find the product I want.
- View individual product details such as the price, image, desciption, rating and possible sizes.
- Easily view the total cost of my purchases to ensure I don't go over budget.
- Sort the list of available products to assist with finding the required product.
- Sort a specific category of products or multiple categories of products simultaneously to find the most suitable product for my needs.
- Search for a product by name or description to find a specific product.
- Easily see what I've searched for and the number of results to decide if the required product is available.
- View quantities and sizes of items in my bag to be purchased, making them adjustable where possible.
- Easily enter my payment information, on a secure and trusted platform.
- View an order confirmation and receive an email confirmation after checkout to keep track of my finances.


As a site user I want to:

- Easily register for an account to view a personalised profile, to view previous orders and to save delivery information.
- Easily login and logout to have hassle-free access to my account.
- Read news articles and information to learn more about the company.
- Receive an email confirmation after registration for verification.


As the store manager, I want to:

- Be able to add a new product to the store.
- Be able to edit and/or update a product.
- Be able to delete a product.


---

#### Mockups

Wireframes were drawn to assertain how the layout of the website will fit together:

<!-- Home Page
![Home Page](     )

Products
![Products Page]() -->

---

## Features

### Existing Features

**Navigation bar:**
- A regular user will see links to the Home Page (the logo), the categories and sub-categories, the user's account (to register/login/logout or to view account page) and their shopping bag.
- An authorised user with superuser access will also have access to the Product Management link to add a product. 

**The Home page:**
- A carousel providing three links to the shopping/products section, the account section and to view the current deals.
- The remainder of the home page will give a number of links for individual item deals.

**The Register page:**
- Contains a form to create a new account.
- Form input fields include a Username input and double inputs for email and password, with a button to submit.

**The Login page:**
- Contains a form to sign in to an existing account.
- Form input fields include Username and Password, with buttons to go to the home page or to submit.
- Acheckbox is provided to Remember the user.
- A link to the Register page is provided.
- A link to change the password is given for account holders who have forgotten.

**The User's Account page:**
- A user's account page.
- Provides a saved delivery address and the option to update datails. 
- A table providing a list of previous orders - including the order date, order number, list of items bought and the total cost.

**The Products page:**
- Contains individual cards for each product.
- Each product card displays the product image, name, price and rating.
- Clicking on a product card will take the user to the Product Detail page.
- Authorised superusers will see edit and delete buttons on each product card.
- A back to top button assists the user to navigate the website, which will be more usefull as more products are added.

**The Product Detail page:**
- Specific page for each product.
- Provides an image, name, price, rating and description description.
- An adjustable quantity input with plus and minus buttons.
- A selector to select the specific size of item if the product has various sizes available.
- A button to add quantity of the selcted product to the shopping bag.
- The page also includes a rating system for account holders. This has yet to be fully implemented and is not affecting the rating score as yet.

**The Add Product page:**
- Superuser access only.
- Contains a form to submit a new product.
- Form input fields include a category selector with inputs for SKU, name, description, 'has sizes' selector, price, rating and an image uploader.
- A submit button will add the product, before redirecting the user to the new Product Detail Page.
- A cancel button returns the user to the Products page.

**The Edit Product page:**
- Superuser access only.
- Contains a form to edit an existing product.
- Form input fields are prepopulated with the product's details. They include a category selector with inputs for SKU, name, description, 'has sizes' selector, price, rating and an image uploader.
- A submit button will update the product, before redirecting the user to that Product Detail Page.
- A cancel button returns the user to the Products page.

**The Shopping Bag page:**
- Contains a table with a list of products in the shopping bag.
- Each product item in the list has displays an image, name, size, sku, adjustable quantity input and a reposonsive item subtotal.
- Below the table a bag total, delivery cost and grand total is calculated.
- Two buttons below provide links to keep shopping (return to products page), and to progress to the checkout, which takes the customer to the checkout page.

**The Checkout page:**
- Provides a form for the user to enter their personal details.
- Certain fields of the form are required.
- Unregistered users are encouraged to create an account or to sign in to save delivery details. Whereas registered account holders will be given the option toi save delivery details.
- Users logged in to accounts may have previously opted to save their delivery details, in which case those address fields are prepopulated.
- An order summary is shown as a final check; it contains the product image, name, size, quantity and a subtotal price.
- Finally the order total is calculated, delivery charge is added (depending on amount spent) and the grand total is given below.

**The News page:**
- Contains individual cards for each article.
- Each article card displays the article image, title, posting date, section of conent and a button to view the article.
- Clicking on an article image or button will take the user to the Article page.

**The News Article page:**
- Specific page for each article.
- Displays the title, image, Date posted, article content and buttons to return to the News page or to view products.


<!-- The Database (MongoDB):
- The "never-have-i-ever" database contains three collections: "users", "categories" and "games".
- The "users" collection contains a unique id number, the username and a hashed password for each user signed up to the website.
- The "categories" collection contains a unique id number and the category name for each category.
- The "games" collection contains a unique id number, the game name, description, requirements, rules, category names, submitted by and a game rating for each game.
- The "games" collection is linked to the "categories" collection through the category names. A game can fall under one or more categories.  -->


### Yet to be Implemented

Home Page:
It was planned to make the Home Page more visually appealling but time constraints prevented this being completed.

Sizes
It would have been desirable to have certain items in various sizes, lengths or thicknesses. The code has been designed to accomodate for items with various sizes, however it was not possible to adjust the product price inline with the size. For this reason all products have been set with no size. If however cetain products come in a variety of sizes with no price difference, then this feature is ready to implement, pending a change in size values as required.

Login:
- The option of a social media link/login feature would ease the signing up process and have greater potential for data gathering.

Profile Page:
- A possible link to social media.

Delete functionality:
- A final check on whether the admin would like to delete the product would be a necessity with implementation, as these buttons may be clicked by mistake, potentially losing important information.

Product Rating:
- The rating system has not yet been linked to the product rating score but will be researched further as to the best method to achieve this.
- Preventing the user from voting multiple times will be essential to make the system fair and representative, however adjusting their vote would be desirable.

News CRUD functionality:
- The ability for a superuser to Create, Update and Delete news articles without having to go into the Django Admin panel would be desirable.
- This section was started but I encountered some bugs and didn't have time to resolve them before deployment. The code for the 'add_article' has been left in but has been commented out.

Delivery:
- In a real setting delivery may not be possible for certain products and/or to certain areas, especially outside the UK.
- A postcode check would be required before the delivery cost is calculated and order approved/granted, for items over a certain weight/size. Smaller items may be posted and would follow the system demonstrated on this website.

---

## Technologies Used
- [Microsoft Word](https://www.microsoft.com/en-gb/microsoft-365/word) was used to construct the wireframes as the ability to add text and shapes is useful and fast to get an idea of layout.
- [Gitpod](https://gitpod.io/) is used as an online IDE as a platform on which to code.
- [Bootstrap 4.4](https://getbootstrap.com/docs/4.4/getting-started/introduction/) was used for structuring and template construction. Many of its components are used throughout the site.
- HTML5 is a markup language and has been used to structure and present the content of the webpage.
- CSS3 (Cascading Style Sheets) is a style sheet language used for describing the presentation of a document written in HTML.
- [JavaScript](https://www.javascript.com/) is a high-level programming language and has been used to add a small amount of interactivity.
- [Python3](https://www.python.org/download/releases/3.0/) is a coding language used to communicate with the database.
- [Heroku](https://www.heroku.com/) is a cloud platform as a service.
- [Heroku PostgreSQL](https://www.heroku.com/postgres) is a document-oriented database, used to store data.
- [Amazon Web Services - AWS](https://aws.amazon.com/) is a cloud based database, used to store static files - images and media.
- [Django](https://www.djangoproject.com/) is a python based web framework used to assist development and speed up programing.

---

## Testing

1. W3C testing for the code.
- The HTML was going to be validated by copying and then pasting the source code into the validator. The validator rturned a lot of problems but most were repeated issues. The first 9 results can be see in the image below: 

index.html
![Attempted Validation](static/images/html-val.png)

- The first error states that the section lacks a header. This is referring to the flash messages. 
- The second error states that a p element can not be the child of a span element. This is being rendered in the with data from the database, however a longer term fix will be sought.
- The third type of error states that there is a duplicate ID. This is due to many game images being rendered on each game card and a way around this is unknown.


2. CSS testing
- W3C CSS (Jigsaw) Validator was going to be used to test for errors. The successful test result is shown in the following image:

style.css
![CSS Validation](static/images/html-val.png)

3. Lighthouse (Dev Tools)
A report was conducted for a mobile device, and returned the following scores:
- Performance - 87%
- Accessibility - 90%
- Best Practices - 93%
- SEO - 92%

There are many things that could be optimised, such as efficiently encoding and serving images next-gen formats. All advisories will be considered and acted upon if possible and necessary.

4. User Stories
All User stories were completed as can be seen with the following screenshot of an excel table:
![]

## Individual Page Testing 

Navigation:
- Resize the screen to ensure the nav bar collapses to a button and the 'Free Delivery' banner disappears on smaller devices.
- Click all nav buttons to ensure they work and direct the user to the correct page.
- Before logging in, ensure the Top Navbar (and Mobile) contains only the Home, News, Shopping Bag and Account dropdown - containing Register and Login links.
- Ensure the 'Total Cost' responds (turn red) and is calculated accurately with the addition of products to the user's shopping bag.
- Log in as a registered user to ensure that the Navbar also contains the 'My Account' link.
- Log in as an Admin to check the Account dropdown also contains the Add Product link.
- Ensure all main product navigation links load to the correct pages.
- Ensure the home link is connected to the logo.

Home Page:
- Resize the screen to ensure the 'Call to Action' dissappears on the carousel, only on smaller devices and the carousel resizes accordingly.
- Ensure all forward/backword buttons work on the carousel (including the middle lower buttons).
- Click each button link of the carousel to ensure they redirect the user to the proper destination (both at small and large screen sizes).

Register/Login (and similar allauth) Pages:
- Ensure the forms loads correctly with required inputs displayed.
- Check form validation is working correctly.
- Register/Login/Logout the ensure correct pages load and allauth form work correctly, including errors.
- Use a real or temporary email address when registering to check if a confirmation email is received.
- Ensure the correct toast is displayed for each situation.

Products Page:
- Select 'All Products' from the Navigation bar - ensure all products are displayed.
- Resize the screen to check the responsiveness of the product page - check the hr element adjusts as required.
- Select each category from the Product Navigation bar and ensure that the correct products are displayed.
- Ensure all products are displaying the correct information from the database.
- Select each option of the sorting selector on every category to ensure the sorting functionality works.
- Using the Search input in the Top Navbar, search for items/terms to ensure it is functioning and filtering products as required.
- Ensure the product count is working and accurate for both categories and search queries.
- Click on product cards/images to check the links to the individual product detail page works.
- Click on the category links on product cards to ensure the correct filter is applied to the product list.
- Scroll down the product list and click the Top button (in the bottom right corner) to ensure the user returns to the top of the page.
- Log in as a super user and ensure the 'Edit/Delete' links are visible on each card (and they disappear when superuser is not logged in).
- Click the Edit button and check whether the user is redirected to the Edit Product page.
- Click delete (on an added 'test product' item) and ensure item is deleted from the product directory.

Product Detail Page:
- Resize the screen to check the responsiveness of the product detail page.
- Ensure all products are displaying the correct information from the database.
- Click the +/- buttons and make sure the quantity adjusts accordingly.
- Click the 'Keep Shopping' button to ensure you are returned to the products page.
- Click the 'Add to Bag' button with different quantities of items to ensure the button works and the correct toast is displayed with accurrate information.
- Add products to the bag below a value of ??40 (half the delivery cost) to ensure the "Free delivery is ??80" message is displayed on the toast.
- Add products to a bag total above ??40 (but below ??80) to ensure the "Free delivery is just... (a small amount) more" message is displayed on the toast.
- Add items so the total exceeds ??80 and ensure the toast "Free delivery" messages are not displayed on the toast.
- Ensure all calculations in the toast is correct.
- Click the 'Checkout' button in the toast and ensure it directs to the Shopping Bag page.
- Click the Edit button and check whether the user is redirected to the Edit Product page.
- Click delete (on an added 'test product' item) and ensure item is deleted from the product directory.
- Click on the ratings stars, one at a time and ensure they respond as needed. (The rating star are not yet functional however and do not affect the product rating as yet).

Shopping Bag Page:
- Ensure correct and accurate products and product information are present in the shopping bag list.
- Resizing the page has found a display issue - please see 'Bugs' section below.
- Click the +/- buttons and make sure the quantity adjusts accordingly, followed by 'update' to ensure the product list is adjusted correctly and the subtotal is recalculated correctly.
- Click the 'Remove' button to ensure the product is removed for the shopping bag and the correct toasts are displayed.
- Ensure the bag total, delivery and grand total prices are displayed accurately according to the shopping bag items.
- Add products to the bag below a value of ??40 (half the delivery cost) to ensure the "Free delivery is ??80" message is displayed.
- Add products to a bag total above ??40 (but below ??80) to ensure the "Free delivery is just... (a small amount) more" message is displayed.
- Add items so the total exceeds ??80 and ensure the toast "Free delivery" messages are not displayed.
- Click the 'Keep Shopping' button to ensure you are returned to the Products page.
- Click the 'Checkout' button and ensure it directs to the Checkout page.

Checkout Page:
- Resize the screen to check the responsiveness of the checkout page.
- Ensure the shoping bag items are displayed correctly with accurate information and totals.
- Ensure the form displays correctly with the correct placeholders and * for required fields.
- Ensure the 'Adjust Order' button works and redirects the user back to the Shopping Bag.
- Try submitting the form with missing required fields to ensure the validation works correctly.
- Ensure the 'Create Account' or 'Sign In' links are displayed if not signed in and they work as required.
- Ensure the links change to a 'Save my information' checkbox to users that are signed in.
- Enter an invalid card number to ensure the form validation works.
- Ensure the 'Charge to the user's card' warning is displayed.
- Enter the 'Test Card Number' (4242 4242 4242 4242) with any other numbers filling the card box and click 'Complete Order'.
- Make sure the loading overlay is displayed while the transanction is procesing.
- Ensure the success toast is displayed, with order number and email address.
- Ensure the Checkout Success page is displayed with a thank you message and the order information.
- Use a real or temporary email address when ordering to ensure an order confirmation email is received.
- Click the Tools button and check it redirects to the correct section.
- Sign in and order again after checking the 'Save Delivery Information' box to ensure the fields are prepoluated upon returning to the checkout.

Add Product Page:
- As a superuser/admin click the link to 'Add a Product'
- Ensure the form loads correctly with the correct placeholders/dropdowns and labels.
- Ensure only the Name, Description and Price are required fields and check form validation by attempting to submit the form with missing information.
- Select an image and ensure it can be uploaded correctly.
- Click the 'Cancel' button to redirect to the Products page.
- Click Add a product and ensure the user is redirected to the product detail page and that all information was uploaded correctly.
- Submit without an image and ensure the 'noimage.png' is displayed, then with an image to ensure it is displayed correctly.

Edit product Page:
- As a superuser/admin ensure all Edit links work correctly, redirecting to the Edit Product page.
- Ensure the form loads correctly with prepolulated firlds and correct labels.
- Ensure only the Name, Description and Price are required fields and check form validation by attempting to submit the form with missing information.
- Select a different image and ensure it can be uploaded correctly.
- Click the 'Cancel' button to redirect to the Products page.
- Click Update Product button and ensure the user is redirected to the product detail page and that all information was uploaded correctly.
- Submit without an image and ensure the 'noimage.png' is displayed, then with an image to ensure it is displayed correctly.
- Ensure all toasts were displayed correctly (an alert to state that the user is editing a product and a success message post edit).

My Account:
- Click the My Account link to ensure the user is redirected to their Account page.
- Resize the screen to check the responsiveness of the Account page.
- Ensure the Delivery Information form is displayed correctly, with the correct labels, placeholders and dropdowns.
- Fill in some information and click the 'Update' button. 
- Ensure fields are prepopulated with accurate information upon returning to the Account page (and after 'Saving Information' during the Checkout process).
- With no previous orders ensure the 'You don't have any previous orders' message is displayed on the Order History section.
- Following making orders check that the Order History table is filled out accurately - date, order number, items, quantity, size and total cost.

News:
- Select 'News' from the Navigation bar - ensure all articles are displayed.
- Resize the screen to check the responsiveness of the product page - check the hr element adjusts as required.
- Ensure all products are displaying the correct information.
- Click on article cards/images and 'Read Article' buttons to check the links to the Article page works.

News Article:
- Ensure all elements are displayed clearly and the image centrally.
- Resize the screen to check the responsiveness of the article page.
- Click the 'Back to News' button to ensure the user is returned to the News page.
- Click the 'View Products' button and ensure the user is redirected to the Products page.


---

## Bugs

- The table layout on the shopping bag page becomes illegible on screens smaller than large. The responsiveness would need adjusting to ensure all items are displayed correctly and clearly.
- The images were taken directly from the old website. After multiple attempts to resize the images to fit, it was realised that certain images are cropped (presumably to fit the old website). In a real deployment, most images would require new and professional images provided by suppliers or the marketing team.

## Deployment

This project was developed on [Gitpod](https://gitpod.io/). It was committed to git and pushed to [Github](https://github.com/) using the built-in Gitpod function.

To deploy the website to [Github Pages](https://pages.github.com/) the following steps were taken.

1. Log in to Github.
2. From the list of repositories, select **lukdav/robert-price-bm**.
3. Select **Settings** from the right hand side of the menu near the top.
4. Scroll down to the **Github Pages** section.
5. Under **Source**, click the drop-down menu labelled **None** and select **Master Branch**.
6. Click **Save** and the page automatically refreshes.
7. Scroll back down to the **Github Pages** section to retrieve the link to the deployed site.

Note: the deployment of a website is not instant and can take up to 20 minutes.

At the moment of submitting the User Centric Milestone Project, both the Developement Branch and the Master Branch are identical.

### How to run this project locally

To clone this project from GitHub:

1. Follow this link to the [Project GitHub Repository].
2. Next to the green Gitpod button, open the drop-down marked **Code**.
3. In the Clone with HTTPS section, copy the URL for this repository.
4. In your local IDE open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone` and then paste the URL you copied in step 3.

    ```git clone https://github.com/lukdav/robert-price-bm.git```

7. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository can be found [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

### Deployment to Heroku

1. Log in to Heroku.
2. Create a new app by clicking 'new' and selecting 'create new app' in the drop-down.
3. Give the app a unique name and select the closest region.
4. Click the create app button.
5. Add Heroku Postgres by searching in the resources tab; selecting the free plan.
6. Install dj_database_url and psycopg2-binary to Gitpod using pip3 install.
7. Run ```pip3 freeze requirements.txt``` to store the apps requirements.
8. Import dj_database_url in settings.py.
9. Replace the default DATABASE setting with an if statement:
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
```
Returning the original database if not.

10. Run migrations using python3 manage.py migrate.
11. Load the fixtures using:
```
python3 manage.py loaddata categories.json
python3 manage.py loaddata products.json
```
12. Create a superuser with ```python3 manage.py createsuperuser``` and filling out the required information.
13. Run ```pip3 install gunicorn```.
14. Freeze requirements again.
15. Create a Procfile and add ```web: gunicorn robert_price_bm.wsgi:application```
16. Sign in to Heroku with ```heroku login -i``` in the terminal.

17. Type ```heroku config:set COLLECTSTATIC=1 --app robert-price``` to temporarily disable static files from being collected by Heroku.
18. Add ```'robert-price.herokuapp.com'``` and ```'localhost'``` to ALLOWED_HOSTS in settings.py.
19. Add and commit changes, pushing them to Github.
20. Initialize git remote with ```heroku git:remote -a robert-price``` and push with ```git push heroku main``` 
21. On the Heroku page, click the deploy tab and then connect to GitHub.
22. Search for robert-price-bm repository and connect.
23. Select 'Enable Automatic Deploys'.
24. In 'Config Vars' under the settings tab, set a SECRET_KEY variable (generated online):
25. Add ```SECRET_KEY = os.environ.get('SECRET_KEY', '')``` to settings.py.
26. Set ```DEBUG = 'DEVELOPMENT' in os.environ``` in settings.py.


### Setting up AWS

1. Create an [AWS account](https://aws.amazon.com/).
2. Go to the AWS management console.
3. In find services', search for 'S3' and select it.
4. Create a new bucket, giving it a name and selecting the closest region.
5. Uncheck 'Block all public access' acknowledging warning of the publicity, click create bucket button.
6. In the bucket's properties tab, select 'static website hosting' and then in 'use this bucket to host a website' type in 'index.html' and 'error.html' and save.
7. In the CORS configuration section on the permissions tab type:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
8. For the buckets permissions policy:
9. Select 'policy generator' on the permissions tab.
Copy the Amazon resource name (ARN) from the top of the page.
10. Select 'S3 Bucket Policy' in type of policy.
11. Allow all principals with '*'.
12. Select  'GetObject' in Actions.
13. Copy the Amazon Resource Name or ARN (from the previous tab) into the labelled box.
14. Click 'Add Statement' followed by 'Generate Policy" and copy the policy into the buckey policy.
15. Add /* on to the end of the 'Resource' key.
16. Click save.
17. In the access control list tab, set the public access' list objects to everyone.


### Setting up IAM (Identity and Access Management) 

1. In the AWS management console, search for, and select 'IAM'.
2. Select 'Groups', then 'Create New Group' and name the new group.
3. Select 'Policies' and then 'Create Policy'.
4. On the JSON tab, select 'import managed policy', search for 'S3' and 'AmazonS3FullAccess' policy. Click 'Import'.
5. Copy the ARN (from the S3 bucket policy) into the 'Resources' key of the JSON file in a list. 
6. Copy the ARN in a second time, adding ```/*``` on to the end. 
7. Select 'Review policy', give it a name and a description. Then click 'Create Policy'.
8. Go back to 'Groups' and select the group previously created.
9. Under the permissions tab click 'Attach Policy'.
10. Select the policy created and select 'Attach Policy'.
11. Select 'Users' and then the 'Add User' button.
12. Create a user, giving a name with 'Programatic Access' and click 'Next: Permissions'.
13. Select the group with the policy attached and click 'Create User'.
14. Download the .csv file.


### Connecting Django to S3
1. Install boto3 with  ```pip3 install boto3```.
2. Install django-storages with ```pip3 install django-storages```.
3. Run ```pip3 freeze > requirements.txt```.
4. Add 'storages' to the apps list in settings.py.
5. Add the following statement in settings.py:
```
if 'USE_AWS' in os.environ:
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    AWS_STORAGE_BUCKET_NAME = 'robert-price'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY_ID = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```

6. Add the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to Config Vars in Heroku (from .csv file).
7. Add USE_AWS variable to Config Vars with a value of 'True'.
8. Remove the DISABLE_COLLECTSTATIC variable.
9. Create a file called custom_storages.py and add:
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
10. Add the following code to the ```if 'USE_AWS' in os.environ:``` statement:
```
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
11. Add all changes, commit and git push for an automatic deployment to Heroku.


### Media Files and Stripe
1. On the S3 dashboard, create a new folder, name it 'media' and 'save'.
2. In 'media', click 'Upload', then 'Add Files' and select all the product images from their storage file on the computer, click 'Next'.
3. Under 'Manage Public Permissions', select 'Grant Public Read Access to these Objects'. Click next through to Upload.
4. From the live site's Django Admin page, authenticate the Admin's email (A login attempt with the email address may be required first).
5. Log in to Stripe account. Click 'Developers' and then API Keys from the menu on the left.
6. Copy the 'Publishable Key' and 'Secret Key' values and add them to Config Vars on Heroku, under STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY respectively.
7. Go to Webhooks on the left menu and click on 'Add Endpoint'.
8. Enter the Endpoint URL as follows:
```
https://robert-price.herokuapp.com/checkout/wh/
```
9. Select 'receive all events' and then 'Add Endpoint'.
10. Reveal webhook 'Signing Secret' and add to Heroku Config Vars, under STRIPE_WH_SECRET. 


## Credits

#### Media
All images used can be found on the existing Robert Price Builds' Merchants [website](https://www.robert-price.co.uk/). Permission to use all images was granted by Robert Price Builders' Merchants.

---

## Acknowledgements
To build this website, I followed the tutorial and mini Boutique Ado project again and feel that it shows a close resemblance to the project. Further iteration and a greater effort will be made to create a more visually unique website. For this project it was felt the Python, Jinja, Stripe and database usage was of greater importance to show my understanding of the content of this module.

A special thanks must go to Robert Price Builders' Merchants for allowing me to use their data, product images and logos, along with their branding style. The existing website was used as inspiration of style and fuction in order to develope an e-commerce aspect to their website.

Read Me example: [mitchdavenport88](https://github.com/mitchdavenport88/hop_shop/blob/main/README.md)

The code for the rating system was found at [Leonardo Schmitt](https://dev.to/leonardoschmittk/how-to-make-a-star-rating-with-js-36d3)

The many tutors, users and other students on slack who are always willing to assist in solving any issue presented.

Finally I'd like to acknowledge the help provided by my tutor Brian Macharia who has assisted and guided me through the Web Development Course.

## Disclaimer
This site has been made only for educational purposes.