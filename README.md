# FastBall

This website is a football e-commerce site. The users can find footballs of the best quality, users can also create an account and make an order from the website. Users can also categorize on the page so they can find the brand of the footballs they want.

The live site can be viewed [here](https://fastball-dc0773e894ca.herokuapp.com/)

![Am I responsive screenshot](documentation/readme/ami.responsive.png)

## Contents

* [Project Goals](#project-goals)
* [User Experience](#user-experience)
    * [User Stories](#user-stories)
    * [Epics](#epics)
    * [Site Structure](#site-structure)
        * [Wireframes](#wireframes)
        * [Database Schema](#database-schema)
    * [Design Choices](#design-choices)
        * [Typography](#typography)
        * [Colour Palette](#colour-palette)
* [Project Management](#project-management)
* [Features](#features)
    * [Existing Features](#existing-features)
        * [All The Pages](#all-the-pages)
        * [The Navigation Bar](#the-navigation-bar)
        * [The Main Content](#the-main-content)
            * [Admin/Staff](#adminstaff-product-management)
            * [Home Page](#home-page)
            * [Info Page](#info-page)
            * [Category Page](#category-page)
            * [Account Pages](#account-pages)
            * [Cart Page](#cart-page)
            * [Checkout Page](#checkout-page)
            * [Comment Page](#comment-page)
        * [The Footer](#the-footer)
    * [Future Features](#future-features)
* [Technologies Used](#technologies-used)
   * [Languages](#languages)
   * [Frameworks](#frameworks)
   * [Database](#database)
   * [Tools](#tools)
   * [Supporting Libraries and Packages](#supporting-libraries-and-packages)
* [Testing](#testing)
   * [Manual Testing](#manual-testing-for-fastball-website)
   * [Summary Table of Manual Testings](#summary-table-of-manual-testings-for-fastball-website)
   * [Other Tests](#other-tests)
   * [Validator Testing](#validator-testing)
* [Bugs](#bugs)
    * [Known Bugs](#known-bugs)
    * [Fixed Bugs](#fixed-bugs)
* [Deployment and Development](#deployment-and-development)
    * [Deploying the Site](#deployment)
    * [Forking the Repository](#forking-the-repository)
    * [Cloning the Repository](#cloning-the-repository)
    * [The ElephantSQL Database](#the-elephantsql-database)
    * [The Cloudinary API](#the-cloudinary-api)
* [Credits](#credits)
* [Acknoledgements](#acknowledgements)

## Project Goals

- I wanted to create a website that allows the admin/staff to add/delete/change product and handle the user account easy on the admin panel and that is linked to a database.

- I wanted to allow the admin/staff to see an admin link on the navbar when they are logged in, where they can add, update and delete products.

- I wanted to allow the admin/staff to be able to put products on sale price so they sell out the old stuff easy.

- I wanted to allow the users to create an account and be able to change the their account details.

- I wanted to allow users to be able to categorize on the page so they can find the brands they want easier.

[Back to top](#contents)

## User Experience

### User Stories

#### Epics 

During the planning for the project, I started and created 4 epics and then broke them down into 38 user stories.

The user stories that were broken down from the epics, I labeled them with different labels and I used the MoSCoW (must have, should have, could have and won't have) to develop them. I labeled them, so I could put energy on the important ones before I started with the non-important ones. You can se all of them on the project board [here.](https://github.com/users/balennouri/projects/5/views1) On the project board you will be able to see the future features as well.

Below here is the completed user stories for this version of this project listed by epics:

##### Epic: Initial Django Setup

* As a developer I want to set up Django and install the initial supporting libraries needed so that I can begin development of the site.

* As a developer I want to set up the environment to secure secret configuration variables so that I can ensure sensitive data is kept private.

* As a developer I want to deploy the site to Heroku so that I can ensure the site works in a production environment and share the completed site publicly.

##### Epic: User Authentication and Account Management

* As a first time user, I can create an account so that I can place an order and comment on products.

* As a user I can delete my account.

* As a returning user I can login/logout of my account.

* As returning user I can update my profile information.

* As site owner I can see all the detail information for the users in the admin panel.

##### Epic: Product Management and Cart/Checkout

* As a admin I can add/delete/update products on the admin panel and on the website.

* As a admin I can add new categories on the admin panel.

* As a user I can add products to the cart.

* As a user I can update the quantity of the product in the cart and delete the product from the cart.

* As user I can place an order and checkout.

* When a user or admin place a order the cart becomes empty.

##### Epic: The Webiste and Content:

* As a user I will have it easy to navigate on the page.

* As a user I will be able to see the rules and info for the store.

* As a user I will be able to categorize the brand of the balls.

[Back to top](#contents)

### Site Structure

#### Wireframes

I used Balsamiq to create my wireframes. I decided to make wireframes for larger screens and for mobile phones. I think wireframes are a good thing to do before starting with the project, so I can put my ideas on what I want the website to look like. Some pages are a little different from the wireframes, but it small details differ from page to page. The reason is because, during development, to make a website with good functionality.

##### Home page in wireframe

![wireframe home page](documentation/readme/wf.home.png)

##### Info page in wireframe

![wireframe Info page](documentation/readme/wf-info.png)

##### Category page in wireframe

![wireframe category page](documentation/readme/wf.category.page.png)

##### Your Profile page in wireframe

![wireframe update profile page](documentation/readme/wf.update.your.profile.png)

##### Sign Up page in wireframe

![wireframe sign up page](documentation/readme/wf.singup.png)

##### Login page in wireframe

![wireframe Login page](documentation/readme/wf.login.png)

##### Product Management page in wireframe

![wireframe product management page](documentation/readme/wf.staff.png)

##### Add Product page in wireframe

![wireframe add product page](documentation/readme/wf.addproduct.png)

##### Update Product page in wireframe

![wireframe update product page](documentation/readme/wf.updateproduct.png)

##### Shopping cart page in wireframe

![wireframe shopping cart page](documentation/readme/wf.shoppingcart.png)

[Back to top](#contents)

#### Database Schema

For this project, I utilized the built-in Django User Model for user accounts and created one model in the store app. In the store model, I built a customer model, order model, product model and category model.

The database schema seen below was created using [Drawsql.app.](https://drawsql.app/) All the fields are not labeled correctly because of limitations in the "drawsql" app. One are the email field and the cloudinary field. However, the diagram still shows the general layout of the models in the store app.

If you want to see the true field choices, head over to the models.py in the store app.

The Database schema:

![Database schema](documentation/readme/database.schema.png)

[Back to top](#contents)

### Design Choices

#### Typography

The starting bootstrap theme used for this project was coming with different fonts, but I chose to change it to Roboto and a secondary font as Sans-serif if the browser didn't read them.

I chose to change the fonts because I noticed that on Apple products the was not working.

#### Colour Palette

![colour pallete](documentation/readme/collor.pallet.png)

The color palette image was generated from [coolers.](https://coolors.co/) The colors came with the bootsrap I chose from [Start Bootstrap.](https://startbootstrap.com/)

- The white color is the main color for the website.

- The color of the fonts on the website is black or dark gray.

- The header and footer have light dark gray colors.

- All the buttons on the website are styled with bootstrap and the colors are chosen from the attribute they have.

[Back to top](#contents)

### Project Management

I used agile methodology throughout the development of this project utilizing GitHub projects and issues. You can read more about this in the AGILE.md file [here.](https://github.com/balennouri/pp4/blob/main/AGILE.md)

[Back to top](#contents)

## Features

### Existing Features

#### All The Pages

##### The Navigation Bar

The site navbar when user comes in to the page:

![navbar](documentation/readme-features/navbar-ingen.png)

The site navbar when user is logged in:

![navbar](documentation/readme-features/navbar-user.png)

The site navbar when admin is logged in:

![navbar](documentation/readme-features/navbar-admin.png)

##### The Main Content

###### Admin/Staff: Product Management

* When a staff member is logged in they will see a extra link on the navbar, which is the admin link
* This paged is only allowed if you are admin or staff member of the FastBall
* The staff member can add/remove and update products
* The staff can perform a full crud functionality on the products

![product management](documentation/readme-features/product-management.png)

![add product](documentation/readme-features/add-product.png)

Messages staff users see when they do something on the product management page:

![Add product mess](documentation/readme-features/mess-add-prod.png)

![Delete product mess](documentation/readme-features/mess-delete-prod.png)

![Update product mess](documentation/readme-features/mess-update-prod.png)

###### Home page

* This is the first page the users see when they jump on the website
* They can view all the products of the store here

![home page](documentation/readme-features/home-page.png)

###### View Product page

* This page is seen when the users view a product
* They will be able to see comments on the product
* They will be able to add product to their cart

![product page](documentation/readme-features/product.png)

###### Info page

* This page is the information page for the store
* Here can the users read about the owner and the information for the page

![info page](documentation/readme-features/info.png)

###### Category page

* This is the categories page where the user has chosen their choice of category

![Category page](documentation/readme-features/category-page.png)

###### Account pages

The customer users can:

* Register, login and logout
* View the home page, info page and categories
* Perform a full crud functionality on their own account

![login page](documentation/readme-features/login.png)

![signup page](documentation/readme-features/sign-up-page-new.png)

![profile page](documentation/readme-features/your-profile-page.png)

![password page](documentation/readme-features/password-update-new.png)

Messages users see if they do some changes for their account:

![account messages](documentation/readme-features/mess-loggedin.png)

![account messages](documentation/readme-features/mess-logged-out.png)

![account messages](documentation/readme-features/mess-password-change.png)

![account messages](documentation/readme-features/mess-profile-updated.png)

![account messages](documentation/readme-features/mess-account-delete.png)

###### Cart page

* The users can remove and update the quantity of their chosen products

![cart page](documentation/readme-features/cart-product.png)

![cart page](documentation/readme-features/cart-empty.png)

Messages users see when they add/delete or update something in the cart:

![cart messages](documentation/readme-features/mess-cart-add.png)

![cart messages](documentation/readme-features/mess-cart-update.png)

![cart messages](documentation/readme-features/mess-cart-remove.png)

###### Checkout page

* To be able to place an order on this page, users need to be logged in or sign up.

![Checkout page](documentation/readme-features/checkout.png)

![Checkout page](documentation/readme-features/checkout-not.png)

Message user see when they place order:

![Checkout message](documentation/readme-features/mess-checkout.png)

###### Comment page

* The user needs to be logged in or sign up to comment on products

![comment page](documentation/readme-features/comment-page-not.png)

![comment page](documentation/readme-features/comment-page.png)

Message user see when they comment:

![comment message](documentation/readme-features/mess-comment.png)

##### The Footer

![footer](documentation/readme-features/footer.png)

[Back to top](#contents)

### Future Features

There are some features I would like to add in the future. You can see all of them on my kanban board [here.](https://github.com/users/balennouri/projects/5) But below here can you see the future features I would prioritize first of them on the kanban board.

* Stok update for the checkout. When a user order from the store the stock update it by self
* Payment and Coupons, so that the user will be able to order with their credit card at the checkout and be able to use a copoun code at the checkout
* Users will get email verification. Users can forget their password and reset it with their email

## Technologies Used

### Languages
* [HTML5](https://html.spec.whatwg.org/)
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
* [JavaScript](https://www.javascript.com/)

### Frameworks

* [Django](https://www.djangoproject.com/)
   * Django was used as the python framework in the project.
* [Bootstrap](https://getbootstrap.com/)
   * The CSS framework that was used for styling the website, saved me a lot of time when I learned to use it.
* [Cloudinary](https://cloudinary.com/)
   * Cloudinary was used to save my media. It's a cloud-based platform for saving and storing images.
* [Start Bootstrap](https://startbootstrap.com/)
   * Start bootstrap was used for the project's theme. Start boostrap creates open source themes, templates and snippets.

### Database
 [ElephantSQL](https://www.elephantsql.com/)
   * ElphantSQL is used as a database for the FastBall project. ElphantSQL is a PostgresSQL database that saves and stores databases.

### Tools
* [Gitpod](https://www.gitpod.io/#get-started)
   * An online integrated development environment (IDE) used for developing and testing the FastBall project. 
* [GitHub](https://github.com/)
   * A web-based hosting service for version control repositories, used for storing and managing the project's source code.
* [Balsamiq](https://balsamiq.com/wireframes/)
   * A wireframing tool used for creating mockups and prototypes of the FastBall website.
* [Heroku](https://dashboard.heroku.com/)
   * Used for deploying the page and publish it. Heroku is a cloud platform that enables deployment and hosting of web applications.

### Supporting Libraries and Packages

* asgiref==3.7.2
* autoflake==2.2.1
* black==24.1.1
* click==8.1.7
* cloudinary==1.38.0
* dj-database-url==0.5.0
* dj3-cloudinary-storage==0.0.6
* Django==4.2.9
* django-allauth==0.60.1
* django-cors-headers==4.3.1
* gunicorn==20.1.0
* oauthlib==3.2.2
* pathspec==0.12.1
* pillow==10.2.0
* psycopg2==2.9.9
* PyJWT==2.8.0
* python3-openid==3.2.0
* requests-oauthlib==1.3.1
* sqlparse==0.4.4
* whitenoise==6.6.0

[Back to top](#contents)

## Testing

### Manual Testing for FastBall Website

#### Test Schedule Plan:

1. #### Navbar Functionality:
   - **Test Scenario**: Ensure that all navbar buttons and links are functional and correctly linked with the users and admin/staff choice.
   - **Test Steps**:
     - Click on each navbar link, including Home, Info, Categories(Nike, Adidas, Puma), Profile, Admin and the Cart.
     - Verify that each click navigates to the respective page without errors.
     - Verify that clicking on "Sign Up" redirects users to the sign-up page.
     - Verify that clicking on "Sign In" redirects users to the sign-in page.
     - Test the functionality of the Cateories dropdown menu and ensure that options such as "All Products", "Nike", "Adidas", "Puma" work as expected.

2. #### Sign Up Functionality:
   - **Test Scenario**: Validate the sign-up process, including account registration and form submisson.
   - **Test Steps**:
     - Fill out the sign-up form with valid user information.
     - Submit the form and verify that no validation errors come up.
     - Attempt to sign in with the newly created account. Ensure that sign-in is successful and redirects users to the home page.

3. #### Sign In Functionality:
   - **Test Scenario**: Validate the sign-in process.
   - **Test Steps**:
     - Navigate to the sign-in page.
     - Enter valid (username and password) into the sign-in form.
     - Submit the form and verify that no validation errors come up. Ensure that sign-in is successful and redirects users to the home page.
     - Test sign-in with invalid (username and password) to verify that something went wrong when trying to login.

4. #### Checkout Functionality:
   - **Test Scenario**: Test the checkout process, including add to cart, remove from cart and update cart.
   - **Test Steps**:
     - Navigate to the cart page
     - Ensure that the button back to the store works if the cart is empty.
     - Ensure that the 2 button links work, when user try to checkout but are not logged in.
     - Click on the checkout buttin verify that no errors come up.
     - Submit the checkout form and ensure that no errore come up. Get the success message when the order is placed.

5. #### Product Management Functionality:
   - **Test Scenario**: Test the product management, including add/remove and update products.
   - **Test Steps**:
     - Navigate to the All Products or Add Product page in the Admin dropdown menu.
     - Ensure that product get updated on all pages.
     - Ensure that product get added on all pages.
     - Ensure that product get deleted from all pages.
     - Ensure that the products is added or deleted in the database in ElphantSQL.

6. #### Profile Management:
   - **Test Scenario**: Validate the functionality related to managing user profiles, including updating, and deleting account.
   - **Test Steps**:
     - Navigate to the profile page.
     - Ensure that the account's information is correct. Test editing account details such as username, name, last name and email. Verify that changes are saved successfully and reflected in the profile page.
     - Verify that changes of password are saved successfully and that old password wont work.
     - Test the "Delete Account" functionality. Verify account is deleted and can't logged in to.

7. #### Product Comments Functionality:
   - **Test Scenario**: Test of the comment process, including add new comment and delete latest comment.
   - **Test Steps**:
     - Navigate to the add comment page on a product page.
     - Add new comment.
     - Ensure that user need to be logged in to comment.

By doing this manual testing using the above scenarios and steps, you can ensure that the FastBall website is an error-free experience for the users and the staff.

### Summary Table of Manual Testings for FastBall Website

### Test Case #1: Navbar Functionality

| Test Step # | Test Description | Action / Input | Expected Result | Result |
|-------------|------------------------------------------|-------------------------------------|------------------------------------------|---------|
| 1 | Click navbar links | Click on each of the navbar link          | Navigate to respective pages | Pass |
| 2 | Verify navigation | Verify each click navigation | Navigate to respective pages | Pass |
| 3 | Test "Sign Up" button | Click on "Sign Up" | Redirect to sign-up page | Pass |
| 4 | Test "Sign In" button | Click on "Login" | Redirect to sign-in page | Pass |
| 5 | Test categories dropdown menu | Click on categories dropdown menu | Ensure options work as expected | Pass |

### Test Case #2: Sign Up Functionality

| Test Step # | Test Description | Action / Input | Expected Result | Result |
|-------------|------------------------------------------|-------------------------------------|------------------------------------------|---------|
| 1 | Fill out sign-up form | Enter valid user information | Form submitted without errors | Pass |
| 2 | Submit form | Click submit button | Account created successfully | Pass |
| 3 | Attempt sign-in | Sign in with new account | Sign-in successful, redirected to home page | Pass |

### Test Case #3: Sign In Functionality

| Test Step # | Test Description | Action / Input | Expected Result | Result  |
|-------------|------------------------------------------|-------------------------------------|------------------------------------------|---------|
| 1 | Navigate to sign-in page | Click on "Sign In" | Sign-in page displayed | Pass |
| 2 | Enter valid login | Enter username and password | Sign-in form submitted without errors | Pass |
| 3 | Submit form | Click submit button | Sign-in successful, redirected to home page | Pass |
| 4 | Test sign-in with invalid login   | Enter incorrect username/password | Get a message that the username or password is incorrect | Pass |

### Test Case #4: Checkout Functionality

| Test Step # | Test Description | Action / Input | Expected Result | Result |
|-------------|------------------------------------------|-------------------------------------|------------------------------------------|---------|
| 1 | Navigate to cart page | Click on checkout | checkout page is displayed | Pass |
| 2 | If cart is empty verify that back to store button works | Click on back to store | Redirect to home page | Pass |
| 3 | Ensure that the 2 button links work, when user try to checkout but are not logged in | Click on Login/Sign up | Redirect to Login/Sign up | Pass |
| 4 | Click on checkout, ensure that no errors comes up | Click on checkout button | Redirect user to checkout page | Pass |
| 5 | Submit the checkout form and ensure that no errore come up. | Click on place order | redirect to home page and get the message | Pass |

### Test Case #5: Product Management Functionality

| Test Step # | Test Description                                  | Action / Input                      | Expected Result                                       | Result  |
|-------------|--------------------------------------------------|-------------------------------------|--------------------------------------------------------|---------|
| 1 | Navigate to the add product/product management page on the admin link | Click on add product and product management | redirect to product management or add product page | Pass |
| 2 | Update one of the products | Change all the product details | The products details is changed on all pages | Pass |
| 3 | Add new product | click on on add product  | Product is added on all pages | Pass |
| 4 | Delete one of the products | Click on delete product | Product is deleted on all pages | Pass |
| 5 | Look if ElphantSQL database is updated | Product is added or deleted in the database | The products on the EplhantSQL database is deleted or added in the database | Pass |

### Test Case #6: Profile Management:

| Test Step # | Test Description                                  | Action / Input                      | Expected Result                                       | Result  |
|-------------|--------------------------------------------------|-------------------------------------|--------------------------------------------------------|---------|
| 1 | Navigate to the profile page | Click on profile | redirect to profile page | Pass |
| 2 | Ensure account information is correct | Change account details | Account details that got changed are changed | Pass |
| 3 | Click on change pssword | Change password  | Password is changed | Pass |
| 4 | Click on delete account | Delete the account | Account is deleted and you can't login into the account anymore. | Pass |

### Test Case #7: Product Comments Functionality:

| Test Step # | Test Description                                  | Action / Input                      | Expected Result                                       | Result  |
|-------------|--------------------------------------------------|-------------------------------------|--------------------------------------------------------|---------|
| 1 | Navigate to comment page on a product page | Click on add comment | redirect to comment page | Pass |
| 3 | Ensure users need to be logged in to comment | Click on add comment  | Show page for users that need to be logged in | Pass |
| 3 | Add new comment | Click on add comment | A comment is added and redirect to that product you commented on | Pass |

### Other Tests

#### Lighthouse Test

The performance, accessibility, best practices and SEO were tested with [Google Lighthouse.](https://developer.chrome.com/docs/lighthouse/overview) You can see the result below.

I tried to fix my score on the lighthouse test by removing the CSS and JS files that came with the start bootstrap theme and tried to use links for the bootstrap and JS instead, but the result of that was not good and the layout and design changed a lot is so I kept the CSS and JS files. That why the score is not as high I wanted it to be.

* Alot of unused CSS
* Alot of unused JS
Home Page:

![lighthouse](documentation/readme-features/lighthouse-test-info.png)

Info Page:

![lighthouse](documentation/readme-features/lighthouse-test-info.png)

Login Page:

![lighthouse](documentation/readme-features/lighthouse-test-signup.png)

Sign-Up Page:

![lighthouse](documentation/readme-features/lighthouse-test-signup.png)

#### WAVE

To be sure that the page has good contrast i tested the page with [WAVE.](https://wave.webaim.org/report#/https://8000-balennouri-pp4-n1yzb2ky0sf.ws-eu108.gitpod.io/product/15/add-comment) You can see the result below.

![WAVE](documentation/readme-features/wave.png)

#### Browsers And Devices

Tested on the following browsers:

* Google Chrome
* Safari
* Firefox

Tested on the following devices:

* Ipad Air
* Iphone 12, 13 and 14
* Samsung Galaxy

### Validator Testing

#### CSS

In my static/css folder you will see two CSS files. The styles.css came with the bootsrap theme i used and the main.css file is my own custom one.

I didn't choose to add a lot of my own CSS styling because of the bootstrap theme I chose to use, had a lot of styling already done. So, thanks to bootstraps, I could build the styling with bootstrap.

When I tested the CSS with the URL link for the page, I got a lot of error messages. The errors came from the bootstrap and JS that came with the theme I chose. However, I tested my own CSS file and got a good result for it.

This test is for my own custom CSS file, which is the main.css

![CSS Test](documentation/readme-features/css-test.png)

#### HTML

All pages were free from errors and got a good result from the HTML validator.

![HTML Test](documentation/readme-features/html-test.png)

#### Python Linter

I tested all of my python files with the [CI Python Linter](https://pep8ci.herokuapp.com/#) and got no error from those tests. It was only some of Django's own python files that came with the apps and the project that had some codes that were longer than 80 characters and I let them be as they were because Django seems to think shortening these lines is ill advisable.

When I tested my python files, I had one error on the views.py file that I solved. You can see the error and the solution to this below.

Error 1:

![Python Test 1](documentation/readme-features/python-test-views-store.png)

Solution 1:

![Python Test 1](documentation/readme-features/python-test-fix.png)

#### JSHint for Javascript

The JS files that are in the staticfiles folder came with the bootstrap theme I chose. I didn't test them because they were the bootstrap content.

The Javascript I used was in the script tags in cart_summary.html and product.html file. The result for them can you se below. 

![Cart Js](documentation/readme-features/js-test-cart.png)

![Product Js](documentation/readme-features/js-test-prod.png)

[Back to top](#contents)

## Bugs

All of these bugs can be found on the kanban board [here.](https://github.com/users/balennouri/projects/5)

### Known Bugs

* This known bugs is something that would be annoying for a user or a buyer because it takes some extra seconds.

* I think that the problem that is causing this bug is the jquery scripts on both files.  

| **Bug** | **Status** |
| ----------- | ----------- |
| When users add or update products on the product view page, it takes some extra seconds for the page to refresh | This is something I would like to fix but didn't find any solution for it. | 
| The same problem is on the cart summary page, if users try to update or remove a product from the cart | This is something I would like to fix but didn't find any solution for it. |

### Fixed Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| Removing products from the cart caused an error that the total price in the cart become $0, it was still products in the cart | By looking in the cart.py I saw that alot of the code was bad indented, that was caused by the "black ."  formater. |
| Adding a product to the cart could also cause the same error as above | This was fixed with. The same fix as above |
| (This can also count as a mistake from my side when i build the view) Users of the page could access the product management page by adding "/staff" to the url link. That was not good because they could delete and add products | This was fixed by adding "@user_passes_test(lambda u: u.is_staff, login_url='home')" in the views.py on function that i wanted to be secure |
| When I deploy the website with my images from Cloudinary I got an error on Google chrome console. The error was that I used http instead of https | The error was solved by adding a meta tag to the base.html file. You can see it [here](https://github.com/balennouri/pp4/blob/main/store/templates/base.html)|
| The Website had a problem showing the fonts that came with the boostrap theme for Apple products. | I solved this by importing my own Google fonts and adding them in the main.css |
| When testing the website with all the different validators I had small mistakes like semicolons and spaces between the functions | Fixed this by formatting the files and went through them just to be sure |


## Deployment and Development

* The project was developed using [Gitpod](https://www.gitpod.io/#get-started) to create the code and overall file structure.
* The repository for this project is hosted on [GitHub](https://github.com/).

### Deployment

The project was deployed using [Heroku](https://id.heroku.com/login).

INFO - to ensure a successful deployment of the project in Heroku, you need to ensure that you create a Procfile and a requirements.txt file.

* In the Procfile insert the following:
  * ``` web: gunicorn PROJECT_NAME.wsgi ```

Once you are certain that everything is ready to deploy the repo, you can do so through the following steps.

1. Log in to Heroku or create an account if necessary.
2. Click on the button labeled "New" from the dashboard in the top right corner and select the "Create new app" option in the drop-down menu.
3. Enter a unique name for the application and select the region you are in.
    * For this project, the unique name is "FastBall" and the region selected is Europe.
4. Click on "create app".
5. Navigate to the settings tab and click "Reveal config vars".
6. Add the config vars necessary for the project.
7. Navigate to the "Deploy" section by clicking the "Deploy" tab in the navbar.
8. Select "GitHub" as the deployment method and click "Connect to GitHub".
9. Search for the GitHub repository that you wish to deploy.
10. Click on "connect" to link the repository to Heroku.
11. Scroll down and click on "Deploy Branch" to manually deploy.
12. Once the app has deployed successfully, Heroku will notify you and provide a button to view the app.

INFO - If you wish to rebuild the deployed app automatically every time you push to GitHub, you may click on "Enable Automatic Deploys" in Heroku.

### Forking the Repository

To create a copy of the repository for viewing and editing without affecting the original repository you can fork the repository through the following steps:

1. In the "FastBall" repository, click on the "fork" tab in the top right corner.
2. Click on "create fork" to fork the repository in your own GitHub account.

### Cloning The Repository

To clone the repository through GitHub, follow these steps:

1. In the repository, select the "code" tab located just above the list of files and next to the gitpod button.
2. Select "HTTPS" in the dropdown menu.
3. Copy the URL under HTTPS.
4. Open Git Bash in your IDE of choice.
5. Change the working directory to the location where you want the cloned directory to be created.
6. Type "git clone" and paste the URL that was copied from the repository.
7. Press the "enter" key to create the clone.

### The ElephantSQL Database

The [ElephantSQL](https://www.elephantsql.com/) PostgreSQL Database was used for this project.

To set up a database, follow these steps:

1. Sign up or log in to ElephantSQL with your GitHub account.
2. Click on "Create New Instance".
3. Enter a name for the instance (this is usually the name of the project.)
4. Select "Tiny Turtle (Free)" free plan.
5. The "Tags" field can be left blank.
6. Click "Select Region".
7. Select a data center near you.
8. Click "Review".
9. Ensure that all details are correct and then click "Create instance".
10. Once created, you can return to the dashboard and click on the instance created to view relevant details such as the database URL and password.

### The Cloudinary API
[Cloudinary](https://cloudinary.com/) is used in this project to store media assets. This is done due to the fact that Heroku does not store media files reliably.

[Back to top](#contents)

## Credits

To style the page and the content to Read me:

- The screenshot at the top of the ReadMe was built from [Ami Responsive.](https://ui.dev/amiresponsive)
- The database schema for the ReadMe was built from [drawSQL.](https://drawsql.app/)
- The color palette image was generated from [coolers.](https://coolors.co/)

To write the code for this project:

- [Code institute LMS](https://learn.codeinstitute.net/dashboard)
- [W3Schools](https://www.w3schools.com/)
- [MDN Web Docs](https://developer.mozilla.org/en-US/)
- [Coding 4 You](http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf)
- [Docs.Djangoproject](https://docs.djangoproject.com/en/5.0/topics/forms/)
- [Docs.Djangoproject](https://docs.djangoproject.com/en/5.0/topics/auth/default/)

Youtube videos that helped me alot:

- [Django Ecommerce Website](https://www.youtube.com/playlist?list=PL-51WBLyFTg0omnamUjL1TCVov7yDTRng)
- [E-commerce FullStack Website using Django](https://www.youtube.com/playlist?list=PL_KegS2ON4s53FNSqgXFdictTzUbGjoO-)
- [Django Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

## Acknowledgements

This site was developed as my Fourth portfolio project for the Code Institute course in Full Stack Software Development. I would like to thank my mentor David Bowers, the slack community and the Code Institute team.

[Back to top](#contents)