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
- Receive an email confirmation after registration for verification.


As the store manager, I want to:

- Be able to add a new product to the store.
- Be able to edit and/or update a product.
- Be able to delete a product.


---

#### Mockups

Wireframes were drawn to assertain how the layout of the website will fit together:

Home Page
![Home Page](     )

Products
![Products Page]()

---

## Features

### Existing Features

Navigation bar:
- A regular user will see links to the Home Page (the logo), the categories and sub-categories, the user's account (to register/login/logout or to view account page) and their shopping bag.
- An authorised user with superuser access will also have access to the Product Management link to add a product. 

The Home page:
- A carousel providing three links to the shopping/products section, the account section and to view the current deals.
- The remainder of the home page will give a number of links for individual item deals.

The Register page:
- Contains a form to create a new account.
- Form input fields include a Username input and double inputs for email and password, with a button to submit.

The Login page:
- Contains a form to sign in to an existing account.
- Form input fields include Username and Password, with buttons to go to the home page or to submit.
- Acheckbox is provided to Remember the user.
- A link to the Register page is provided.
- A link to change the password is given for account holders who have forgotten.

The User's Account page:
- A user's account page.
- Provides a saved delivery address and the option to update datails. 
- A table providing a list of previous orders - including the order date, order number, list of items bought and the total cost.

The Products page:
- Contains individual cards for each product.
- Each product card displays the product image, name, price and rating.
- Clicking on a product card will take the user to the Product Detail page.
- Authorised superusers will see edit and delete buttons on each product card.
- A back to top button assists the user to navigate the website, which will be more usefull as more products are added.

The Product Detail page:
- Specific page for each product.
- Provides an image, name, price, rating and description description.
- An adjustable quantity input with plus and minus buttons.
- A selector to select the specific size of item if the product has various sizes available.
- A button to add quantity of the selcted product to the shopping bag.
<!-- - The page also includes a rating and a button in order to Upvote the game, incrementing its rating by one. -->

The Add Product page:
- Superuser access only.
- Contains a form to submit a new product.
- Form input fields include a category selector with inputs for SKU, name, description, 'has sizes' selector, price, rating and an image uploader.
- A submit button will add the product, before redirecting the user to the new Product Detail Page.
- A cancel button returns the user to the Products page.

The Edit Product page:
- Superuser access only.
- Contains a form to edit an existing product.
- Form input fields are prepopulated with the product's details. They include a category selector with inputs for SKU, name, description, 'has sizes' selector, price, rating and an image uploader.
- A submit button will update the product, before redirecting the user to that Product Detail Page.
- A cancel button returns the user to the Products page.

The Shopping Bag page:
- Contains a table with a list of products in the shopping bag.
- Each product item in the list has displays an image, name, size, sku, adjustable quantity input and a reposonsive item subtotal.
- Below the table a bag total, delivery cost and grand total is calculated.
- Two buttons below provide links to keep shopping (return to products page), and to progress to the checkout, which takes the customer to the checkout page.

The Pheckout page:



<!-- The Database (MongoDB):
- The "never-have-i-ever" database contains three collections: "users", "categories" and "games".
- The "users" collection contains a unique id number, the username and a hashed password for each user signed up to the website.
- The "categories" collection contains a unique id number and the category name for each category.
- The "games" collection contains a unique id number, the game name, description, requirements, rules, category names, submitted by and a game rating for each game.
- The "games" collection is linked to the "categories" collection through the category names. A game can fall under one or more categories.  -->


### Yet to be Implemented

Sizes
It would have been desirable to have certain items in various sizes, lengths or thicknesses. The code has been designed to accomodate for items with various sizes, however it was not possible to adjust the product price inline with the size. For this reason all products have been set with no size. If however cetain products come in a variety of sizes with no price difference, then this feature is ready to implement, pending a change in size values as required.

Login:
- The option of a social media link/login feature would ease the signing up process and have greater potential for data gathering.

Profile Page:
- A possible link to social media.

Delete functionality:
- A final check on whether the admin would like to delete the product would be a necessity with implementation, as these buttons may be clicked by mistake, potentially losing important information.

Product Rating:
- Preventing the user from upvoting multiple times will be essential to make the system fair and representative.
<!-- - Limiting the value to 5 (a rating as a fraction of 5) -->

Delivery:
- In a real setting delivery may not be possible for certain products and/or to certain areas.
- A postcode check would be required before the delivery cost is calculated and granted, for items over a certain weight/size. Smaller items may be posted and would follow the system demonstrated on this website.

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
- Performance - 80%
- Accessibility - 96%
- Best Practices - 93%
- SEO - 92%

There are many things that could be optimised, such as properly sizing images. All advisories will be considered and acted upon if necessary.

4. User Stories
- The first user story is addressed as the website provides a list of games and categorises them to make page navigation easier and so a better level of UX is achieved.
- The second user story is addressed as the website provides a method of submitting new games.
- The final user story is considered with the ability for admins to control website content; the ability to edit and delete games along with the ability to create, update and delete the categories.

## Individual Page Testing 

Navigation:
- Resize the screen to ensure the nav bar collapses to a button on smaller devices.
- Log in as a registered user to ensure that the Navbar contains the links for Home, Submit Game, Profile and Log Out.
- Log in as an Admin to the Navbar contains all of the links a registered user would see as well as the link to Manage Categories.
- Log out of all accounts and ensure the Navbar contains only the Home, Register and Log In links.
- Ensure all navigation links load to the correct pages, including the home link connected to the logo/page title.

Home Page:
- Resize the screen to ensure the ScrollSpy Navigation menu disappears on smaller devices.
- Ensure the correct categories are loaded in the ScrollSpy menu from the database.
- Ensure the ScrollSpy menu links target the correct section and games. 
- Click on the sign up call to action link to ensure the correct page is targeted.
- Click the game cards to ensure the collapsible drops down and the correct information is loaded from the database; Game Name, Game Categories, Game Rating, with the Game Description, and the 'Submitted By' username in the dropdown.
- Ensure the game rating shows the correct score.
- Check the image displayed matches the first Category listed for the game.
- Click the Rules button to ensure the Game Page is loaded.
- Ensure the the Edit and Delete button are only rendered with an Admin's account.
- Click the Edit button the ensure the Edit Game page is loaded.
- Click the Delete button and ensure the game is Deleted.

Register Page:
- Ensure the form loads correctly with Username and Password inputs, along with form validation.
- Try exiting username to ensure matching usernames do not occur.
- Click the 'Register' button with the fields correctly filled and ensure the user's details are stored in the database (Password hashed), with the correct flash message displayed.
- Click the Log In link below to ensure the Log In page is loaded.

Log In Page:
- Ensure the form loads correctly with Username and Password inputs, along with form validation.
- Enter incorrect details: first username, then password and vice versa to ensure the form and user accounts are secure.
- Log in with existing account to ensure form works as expected and the Profile page is loaded, with the correct flash message displayed.
- Click the Register link below to ensure the Register page is loaded.

Add Game Page:
- Ensure the form loads correctly.
- Ensure the form validation works as it should if sections are left blank(the validation for game requirement and rules sections has a bug as mentioned in the bugs section).
- Ensure the Add Requirement and Add Rule buttons work correctly adding the input to a list.
- Check the correct categories are loaded in the the multiple dropdown checklist and that the checklist works as it should.
- Click the 'Add Game' button with a different input missing to ensure required iputs are filled.
- Click the 'Add Game' button with the fields filled correctly to ensure the information is transfered and stored in the database (MongoDB: Games), with the correct flash message displayed.

Edit Game Page:
- Go to the "Submit Game" page.
- Ensure the form loads correctly with all fields prepopulated correctly with the game's details.
- Ensure all validation and inputs function as with the Add Game page.
- Click the 'Cancel' button to ensure the Game Page is reloaded.
- Click the 'Edit Game' button with the fields filled correctly to ensure the information is updated and stored in the database, with the correct flash message displayed.

Game Page:
- Ensure the Game Page Title is the Game's Name.
- Ensure the Game Description, Requirements and Rules are rendered correctly from the database.
- Check the Rating is correct and that the Upvote button increments the rating by one, which also updates the database value.

Profile Page:
- Ensure the Username of the profile is displayed.
- Further User details and personalisation of the page will be displayed here (Please see 'Yet to be implemented' section).

Manage Categories Page:
- Admin only.
- Ensure all categories are rendered in a card each.
- Each category/card has both an Edit and a Delete button.
- Check the Edit button takes the Admin to the Edit Category Page.
- Check the Delete button deletes the category, along with the flash message confirmation.

Edit Categories Page:
- Admin only.
- Ensure form is displayed correctly with an input field for Category Name.
- Check the input field is prepopulated with the current Category Name.
- After editing the name, click the 'Update Category' button to ensure the category is both updated in the Categories Page as well as the database.
- Ensure the flash message confirming the Updated Category is displayed as the Categories Page is loaded.
- Back to the Edit form, click the 'Cancel' button to ensure the user is diverted back to the Categories page.

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
4. Clicked the create app button where I was directed to the dashboard for the new app.
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



## Credits

#### Media
All images used can be found on the existing Robert Price Builds' Merchants [website](https://www.robert-price.co.uk/). Permission to use all images was granted by Robert Price Builders' Merchants.

---

## Acknowledgements
To build this website, I followed the tutorial and mini Boutique Ado project again and feel that it shows a close resemblance to the project. Further iteration and a greater effort will be made to create a more visually unique website. For this project it was felt the Python, Jinja, Stripe and database usage was of greater importance to show my understanding of the content of this module.

A special thanks must go to Robert Price Builders' Merchants for allowing me to use their data, product images and logos, along with their branding style. The existing website was used as inspiration of style and fuction in order to develope an e-commerce aspect to their website.

The many tutors, users and other students on slack who are always willing to assist in solving any issue presented.

Finally I'd like to acknowledge the help provided by my tutor Brian who has assisted and guided me through the Web Development Course.