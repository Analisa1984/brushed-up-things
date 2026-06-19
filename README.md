# Brushed Up Things! - An independent Art Gallery Catalog. 

## Table of Contents:

1. [About](#about)
2. [Business Goals](#business-goals)
3. [User Stories and Acceptance Criteria ](#user-stories-and-acceptance-criteria)
4. [Wireframes](#wireframes)
5. [Entity Relationship Diagrams](#entity-relationship-diagrams)
5. [Core E-Commerce, Checkout and Email Architechture](#core-e-commerce-checkout-and-email-architechture)
6. [Stripe Webhook Integration and Backend Architecture](#stripe-webhook-integration-and-backend-architecture)
6. [Design and How to use the website](#design-and-how-to-use-the-website)
7. [Agile Methodology Followed](#agile-methodology-followed)
8. [Languages and Technologies used](#languages-and-technologies-used)
9. [Links Used](#links-used)
10. [Media Used](#media-used)
11. [LightHouse Accessibility Checks](#lighthouse-accessibility-checks)
12. [HTML Validation Checks](#html-validation-checks)
13. [CSS Validation Checks](#css-validation-checks)
14. [Python Validation Checks and Explanation of Results](#python-validation-check)
15. [Automated Testing](#automated-testing)
16. [Manual Testing](#manual-testing)
17. [Responsiveness](#responsiveness-testing)
18. [Final Product](#final-product)
19. [Mobile Screen Views](#mobile-screen-views)
20. [Business Goals and User Stories met](#business-goals-and-user-stories-met)
21. [Deployment](#deployment)
22. [Bug Fixes](#bug-fixes)
23. [Future Developments](#future-developments)
24. [References](#references)
25. [Acknowledgements](#acknowledgements)
26. [Thank You](#thank-you-for-reviewing-this-product)

## About
Brushed Up Things! - This is a catolog showcasing artworks by our independent artists.  Art collectors and enthusiasts can review the items of our gallery and make purchases. Making purchases, involves the user first registering and creating an account then loggin in to make a purchase. 

## Business Goals: 
1. Provide an online platform that allows the exhibitions of our independent artists.
2. Allow purchases to be done online only for this online art gallery store. 
3. Deliver a browsing experience whereby once an item is sold the item is updated as sold once the item is purchased online. 
4. Create an online awareness of the store by using Search Engine Optimizations. 

## User Stories and Acceptance Criteria:

1. Viewing the Artwork Catalog

User Story: As a user, I can view the varioua artwork with descriptions, prices so that I can decide if I would like to purchase any artwork. 

Acceptance Criteria: 
- There must be an art gallery page which are available to all users (registered, not registered, logged-in, not logged-in)
- Each art piece must have a title, artist name, description, price. 

2. Account Registration for Purchasing

User Story: As a user, I can register for an account and log in so that I can have a safe means of purchasing items from the catalog (which is online only). 

Acceptance Criteria: 
- All users must first register to have their own account. Only after having an account, users can log in to make a purchase for the desired item(s). 
- Non-registered users or persons who are not logged-in will be directed to the register / log in page. 

3. Instant Updates on Sold Art Pieces

User Story: As a user or site owner, I can know when at art piece has been bought so that I know that it is no longer available for purchase. 

Acceptance Criteria: 
- Once an item is bought and payment is successfully made via the payment portal, the item in the database must be updated as "Sold" and no longer available to buy. 
- The catalog item on the gallery page must show as "Sold". and the purchase feature must be disabled. 

4. Managing Past Orders (Profile Page)

User Story: As a user, I can view my profile so that i can see a record of all the items that I have purchased. 

Acceptance Criteria: 
- A secure user profile area  should be accessible to the only the authenticated user who owns it. 
- The profile page should retrieve and sho a summary of all past transactions. 

5. Store Management: 

User Story: As a gallery manager, I can add, update, delete items from the gallery so that i dont have to go to the developer if there are changes in the gallery pieces(which there will be frequently).

Acceptance Criteria: 
- Only authenticated staff such as the gallery manager, can change gallery inventory (such as add, update, delete) on the website. 
- A Form should be available that allows the authenticated staff/manager to perform the processes above. 

6. Automated Email notifcations:

As a registered customer I can receive an itemized email receipt immediately after a successful checkout transaction so that I have a permanent digital record of my gallery purchase.

Acceptance Criteria
- Successful checkout triggers a background view method that compiles and executes an asynchronous transactional email confirmation.
- Sent emails pull structured content from isolated subject and body templates containing unique tracking numbers and item metrics.

7. Advanced Media Catalog Filtering

As a gallery explorer I can sort and filter artworks by specific mediums or individual artists so that I can quickly find pieces that fit my explicit stylistic interests.

Acceptance Criteria
- A responsive sidebar menu filters the live gallery view grid based on relational queries like Oil and Canvas or Sculptures.
- Text search functionality queries title and artist strings to return accurate matches.

8. Automated Transactional Webhooks

As a system administrator I can rely on a server-side webhook listener to handle payment events asynchronously so that orders are safely created even if a user closes their browser mid-transaction.

Acceptance Criteria
- A dedicated server endpoint handles incoming payment_intent.succeeded payloads.
- The system cryptographically validates the webhook signature and fallback-creates the database order if a session drop occurred.

9. Secure E-Commerce Checkout

As a registered customer I can submit my credit card details securely through an integrated payment form so that I can confidently complete my artwork order online.

Acceptance Criteria
- Checkout page integrates the official Stripe API and Elements script SDK to capture payments securely.
- Frontend JavaScript disables the checkout button immediately upon form submission to prevent duplicate card charges.

10. Store Management Inventory Controls

As a gallery manager I can add, update, and delete artworks and artists directly on the frontend UI so that I do not need to access the database admin backend to keep our inventory current.

Acceptance Criteria
- Frontend CRUD forms are restricted exclusively to authorized staff user accounts.
- Form submissions successfully write additions, edits, or deletes to the live data store.

11. Managing Shipping Costs
As a gallery director I can update delivery fee percentages or free-delivery limits from a central configuration row so that I can adjust shop rules without rewriting codebase parameters.

Acceptance Criteria
- Financial calculations reference variables isolated within a single StoreConfiguration database entry row.
- Editing the threshold row in the administration hub updates server-side transaction math rules immediately.

12. Instant Updates on Sold Art Pieces
As a site owner and buyer I can see an art piece automatically update to "Sold" once bought so that it is instantly marked as unavailable for anyone else to buy.

Acceptance Criteria
- A successful payment processing lifecycle automatically sets the database flag of the artwork to "Sold".
- The gallery view displays a prominent visual "Sold" badge over the piece and disables its purchase interface.

13. Interactive Artist Profiles
As a gallery explorer I can click on an artist's profile to view their biography and a dedicated grid of their specific artwork so that I can learn more about my favourite creators and browse their entire collection in one place.

Acceptance Criteria
- The platform implements a dedicated Artist Model linked to the Artwork Model via a One-to-Many ForeignKey relationship.
- Clicking an artist's name fetches their biographical details and runs a single database query to retrieve their inventory.
- A dynamic loop renders the artist's specific collection automatically without any hardcoded frontend page updates.

## Wireframes:

1. Home Page for mobiles and larger screens (tablets, laptops and PC):
   ![Home Page Wireframe](assets/images/brushed-up-things-wireframes/home.png)

2. Gallery Page for mobiles and larger screens (tablets, laptops and PC):
   ![Gallery Page Wireframe](assets/images/brushed-up-things-wireframes/gallery.png)

3. Log In Page for mobiles and larger screens (tablets, laptops and PC):
   ![Log In Wireframe](assets/images/brushed-up-things-wireframes/login.png)

4. Contact Us page for mobiles and larger screens (tablets, laptops and PC):
   ![Contact Us Page Wireframe](assets/images/brushed-up-things-wireframes/contact-us.png)

5. Register page for mobiles and larger screens (tablets, laptops and PC):
   ![Register Page Wireframe](assets/images/brushed-up-things-wireframes/signup.png)

6. Order Page for mobiles and larger screens (tablets, laptops and PC):
   ![Order Page Wireframe](assets/images/brushed-up-things-wireframes/order.png)

7. Checkout Page for mobiles and larger screens (tablets, laptops and PC):
   ![Checkout Page Wireframe](assets/images/brushed-up-things-wireframes/checkout.png)

---------------------------------------------------------------

## Entity Relationship Diagrams:

1. Logical Data Model (ERD):

    ![Logical Data Model](assets/images/erd-diagrams/logical-erd3.png)

2. Physical Data Model (ERD):

    ![Physical Data Model](assets/images/erd-diagrams/physical-erd3.png)

----------------------------------------------------------------

## Core E-Commerce, Checkout & Email Architecture

### 1. Design Rationale & User Control
The checkout infrastructure for "Brushed Up Things" is engineered to provide an elegant, secure, and transparent purchasing experience for art collectors. Every phase of the transaction pipeline prioritizes immediate user feedback and defensive application design:

* **Preventing Duplicate Transactions:** To eliminate common e-commerce friction points—such as accidental double-clicks causing multiple card charges—the frontend checkout architecture uses custom JavaScript (`stripe_elements.js`). The exact millisecond a user clicks the submission action, both the input fields and the submit button are programmatically disabled. 
* **State Control:** The system halts standard browser dispatch, securely hands processing control over to Stripe's remote servers to authorize the funds, and only triggers the final database save upon a verified success state.

### 2. Relational Database Schema & Architecture
Rather than processing purchases as flat data entries, the application implements a robust, relational database schema designed to preserve data integrity and prevent record duplication. The data framework relies on three interconnected custom components:

* **Store Configuration Model (`StoreConfiguration`):** A centralized administrative hub that allows gallery managers to dynamically alter shipping percentages or free-delivery thresholds via the Django Admin panel. By avoiding hardcoded metrics, operational business rules remain isolated from the core code.
* **Order Model (`Order`):** Acts as the parent container tracking a single transaction. It captures essential delivery metrics, timestamps, and country flags. Upon creation, it runs a private method leveraging Python's `uuid` library to stamp each record with a permanent, alphanumeric tracking reference. It also optionally maps the purchase to an authenticated `UserProfile`.
* **Order Line Item Model (`OrderLineItem`):** A dedicated bridge table establishing a Many-to-One relationship with the parent order. Because a collector might buy multiple distinct artworks in a single session, this model isolates each separate item, tracks the requested quantity, and handles individual pricing metrics.

### 3. Automated Backend Calculations
To enforce data integrity, all financial values and operational rules are evaluated directly on the server database layer through custom model methods, rather than trusting manipulation-prone frontend client scripts:

* **Line Item Totals:** On saving an `OrderLineItem`, the model hooks into the foreign key relationship to fetch the static price of the linked `Artwork`, multiplies it by the selected quantity, and updates its `lineitem_total`.
* **Aggregated Order Totals:** Saving a line item automatically signals the parent `Order` to trigger its internal `update_total` method. The system aggregates all connected line items using Django's `Sum` tool. It then queries the active `StoreConfiguration` model, compares the cumulative value against the active free-delivery threshold, applies the standard shipping percentage if applicable, and updates the database row with a definitive `grand_total`.

### 4. Transactional Automated Notification Pipeline
Communication is an integral extension of the user experience. Once the application processes a checkout success route, a private backend notification routine (`_send_confirmation_email`) executes instantly to reassure the customer.

* **Decoupled Messaging Layouts:** The notification system strictly separates messaging concerns. The email subject line is handled by an isolated text document (`confirmation_email_subject.txt`), dynamically interpolating the transaction's unique ID. The message interior utilizes an advanced HTML template (`confirmation_email_body.html`) that loops through the purchase line items to deliver an explicit, transparent breakdown of the collector's summary.
* **Dual-Environment Routing Strategy:** To ensure development safety and ease of maintenance, the email architecture uses a conditional environmental split:
  1. **Development Routing (Console Backend):** When the application detects a local development environment flag, Django routes the message via `django.core.mail.backends.console.EmailBackend`. This intercepts the notification and prints the raw layout directly to the local terminal server logs for safe debugging and structural review.
  2. **Production Routing (Live SMTP Backend):** In a live production deployment, the architecture switches dynamically to `django.core.mail.backends.smtp.EmailBackend`. It authenticates securely with external Google SMTP mail nodes using TLS cryptographic protocols and protected environment variables (`EMAIL_HOST_USER` and `EMAIL_HOST_PASS`) to send an email right to the buyer's inbox.

---------------------------------------------------------------------

## Stripe Webhook Integration and Backend Architecture:
![Stripe CLI Testing Logs](assets/images/webhook-images/webhook.png)

To ensure total checkout reliability and prevent data loss from unexpected browser session drops (e.g., a user closing the window or losing internet connection mid-payment), a custom, decoupled two-tier webhook processing pipeline was implemented.

Rather than handling both network validation and database logic inside a single monolithic view, the architecture separates responsibilities into two distinct processing files:

1. **`webhooks.py` (The Secure Endpoint Receiver):** Acts as the direct HTTP POST endpoint listener (`/checkout/wh/`) for incoming traffic from Stripe. It utilizes Stripe's official Python SDK (`stripe.Webhook.construct_event`) to securely validate the cryptographic signature header (`HTTP_STRIPE_SIGNATURE`) against the locally stored `STRIPE_WH_SECRET`. This prevents unauthorized script or payload injections.
   
2. **`webhook_handler.py` (The Business Logic Engine):** A dedicated Python class designed to process validated Stripe payloads. Upon receiving a verified `payment_intent.succeeded` event, the handler queries the database to check if a matching order already exists (created by the frontend view). If no order is found—signaling a frontend session crash—the handler parses the metadata payload to programmatically construct and save the `Order` and `OrderLineItem` objects directly back to the database.

--------------------------------------------------------------

### Webhook Event Testing & Local Verification

Because Stripe cannot directly communicate with a local development server (`localhost`), the **Stripe CLI** was deployed to securely listen to the Stripe Developer Dashboard account and forward incoming events to the local webhook endpoint.

#### Verification Logs
From the sripe CLI testing
  ![Stripe CLI Test](assets/images/webhook-images/webhook.png)

---------------------------------------------------------------

## Agile Methodology Followed

![userstoreies](assets/images/project-board/userstories-moscow.png)
![project board1](assets/images/project-board/project-board1.png)
![project board2](assets/images/project-board/project-board-2.png)
![project board3](assets/images/project-board/project-board3.png)
![project board4](assets/images/project-board/project-board4.png)
![project board5](assets/images/project-board/project-board5.png)
![project board6](assets/images/project-board/project-board6.png)
![project board7](assets/images/project-board/project-board7.png)
![project board8](assets/images/project-board/project-board8.png)
![project board9](assets/images/project-board/project-board9.png)


This project was developed using Agile practices. Breaking the work down into smaller tasks made it easier to manage the project development.

### 1. Project Management Tool
GitHub Projects was used to keep track of tasks. The board was divided into columns to follow the progress of the work:
* To Do: Tasks and user stories that needed to be started.
* In Progress: Features currently being coded and worked on.
* Done: Fully completed, tested, and working features deployed to the live website.

### 2. Development Phases
The project was built in phases to focus on one main area of the application at a time:

* Initial Setup: Creating the Git repository, setting up the basic Django project layout, and connecting the AWS database.
* Product Catalog: Creating the artwork and artist database models, and building the gallery grid with its sidebar filters.
* Accounts and Security: Adding Django Allauth for user registration and login, and setting up the profile page to show a user's past orders.
* Shopping Cart and Payments(Checkout): Creating the shopping cart logic, building the checkout forms, and connecting Stripe and webhooks to securely process payments and mark items as sold.
* Testing and Final Tweaks: Running automated and manual tests, validating the HTML, CSS, and Python code, checking accessibility with Lighthouse, and fixing any remaining warnings.

### 3. Task Prioritization
Every task on the project board was prioritized using the MoSCoW method to make sure the most important features were built first:
* Must Have: Basic required features like the product catalog, database connections, and the secure payment process.
* Should Have: Helpful features that improve the website, such as user profiles showing a history of past purchases.
* Could Have: Smaller optional features that add convenience but are not required for the shop to function, like the empty cart button.
* Wont Have: Features that are convenient but due to time constrainsts are not practical to add without compromising the basic features. 

-------------------------------------------------------------------------------------------

## Languages and Technologies used:

1. HTML
2. CSS
3. Python Validation (PEP 8)
4. Python 
5. Django framework 
6. Bootstrap version 5.3.3 Library - for navigation bar, footer and other body elements and class implementation for styling .
7. Bootstrap5 icon library for icons
8. Google Fonts to import additional fonts
9. Artificial Intelligence Technologies (Gemini) was used to create Brushed Up Things Logo, the favicons of various sizes as well as art pieces for all the sculptures and all the oil paintings.
10. Chrome developer tools, Inspector, to get screenshots of the product webpage on various sized devices.
11. LightHouse on Chrome Developer Tools to check for Accessibility.
12. Nu HTML Validator to check the HTML code.
13. W3C CSS Validator to check the CSS code.
14. Amazon Web Services for the AWS database - Postgres
15. Figma software was used to create the wireframes.
16. draw.io for Entity Relationship Diagrams (ERD).
17. Atripe API/ Stripe Python SDK - to handle payment processing, secure authorization loops and backend webhook confirmations. 
18. Gunicorn - The WSGI HTTP server used to run python application in production in heroku. 
19. AWS (Amazon Web Services) S3 - for static media storage and PostgreSQL database (a RDS database).
20. Heroku - The cloud platform used to host and deploy the live web application. 
21. GitHub - to store the code repository. 
22. Django Allauth - The specialized library used to manage user registration, authentication, login forms and email validations. 
23. psycopg2 - the PostgreSQL database adapter for Python that allows Django to communicate with the AWS database.
24. dj-database-url - this library was used to parse the database URL environment vaiable in settings.py
25. Flake8 - This was the python linter I used to verify PEP 8 style guidelines. 

----------------------------------------------------------------

## Links used:

- External links include the social media links below:

1. Facebook:
   [Facebook](https://www.facebook.com)

2. Instagram:
   [Instagram](https://www.instagram.com)

3. X (formerly known as Twitter):
   [X](https://www.twitter.com)

------------------------------------------------------------------

## Lighthouse Accessibility Checks:
![LightHouse Accessibility Checks](assets/images/validation-checks/accessablity.png)

------------------------------------------------------------------

## HTML Validation Checks:

1. Homepage
![Homepage](assets/images/validation-checks/validation-homepage.png)

2. About Us Page
![About Us Page](assets/images/validation-checks/validation-about.png)

3. Gallery Page
![Gallery Page](assets/images/validation-checks/validation-gallery.png)

4. Contact Us Page
![Contact Us Page](assets/images/validation-checks/validation-contact.png)

5. Sign Up Page
![SignUp Page](assets/images/validation-checks/validation-signup.png)

6. Log In  Page
![Login Page](assets/images/validation-checks/validation-login.png)

7. Shopping Cart Page
![Shopping Cart Page](assets/images/validation-checks/validation-shoppingcart.png)

8. Checkout Page
![Checkout page](assets/images/validation-checks/validation-checkout.png)

9. Successful Checkout Page
![Successful Checkout Page](assets/images/validation-checks/validation-checkout-success.png)

10. Profile Page
![Profile page](assets/images/validation-checks/validation-profile.png)

11. Staff Portal Page
![Staff Portal Page](assets/images/validation-checks/validation-staffportal.png)

12. Staff Edit page
![Staff Edit Page](assets/images/validation-checks/validation-editprofile.png)

------------------------------------------------------------------
 
## CSS Validation Checks:
![CSS Validation Checks](assets/images/validation-checks/validation-css.png)

## Python Validation Check

All Python code was checked via the Flake8 and had zero problems. 
![Python Validation Check](assets/images/validation-checks/python-validation-check.png)

One test did fail flake8, namely `profiles/apps.py`. The reason this failed is Django requires the import inside the ready method so the application registers the signal recievers when it loads. Therefore removing the import was not an option and to quell the concerns of flake8 `# noqa: F401` was used.

## Automated Testing
 
To ensure the stability and reliability of the project's core logic, a few automated tests were implemented using Django's built-in testing framework (`TestCase`). 

Specifically, three tests were written within `artwork/tests.py` to validate the **Contact Us** form submission and email:
1. **`test_contact_page_renders_correctly`**: Verifies that the contact page successfully loads with a HTTP 200 status code and utilizes the correct template.
2. **`test_valid_contact_form_submission`**: Mimics a user successfully submitting the form, checking that the view processes valid data and correctly redirects the user back to the contact page.
3. **`test_invalid_contact_form_submission`**: Ensures that missing or invalid form data is prevented from being submitted and safely re-rendering the form with errors without crashing the application.

#### Running the Tests
The test suite can be executed locally using the following terminal command:
in bash terminal 
python3 manage.py test artwork

Results below: 
![Automated Test](assets/images/automated-tests/automated-testing-contact.png)

------------------------------------------------------------------

## Manual Testing

Manual testing is the process whereby all components, including functions, of a page are tested by manually going through each aspect of a page or software. This is done by also checking against the user stories to check if the program / software complies. Manual testing is deployed if chosen as the only means to check the application or software created (functions and all other implementations). However, manual testing can be done after automated testing is completed. Many software is tested both by manual testing and automated testing. Automated testing tests the functions created. Automated testing does not test the user experience as this is usually subjective. In Brushed Up things, manual testing was done to check the user experience and to test parts of the application that did not have automated tests. In most programs or software development, a combination of both manual and automated testing is done.

Manual testing - The various parts of the website were checked such as the navigation bar, links, buttons. The various parts were also manually tested on mobile and tablet sizes using inspect and responsiveness checks on the page.

NOTE: 
Each part: 
 - Header 
 - Footer
 - Main Pages (Not Logged In)
 - Standard User Journey
 - Staff User Journey (requires a Staff User account)

Should be tested as one complete set of tests.

## Header 

### Logged Out
| Action | Expected Result | Pass |
| ------ | ------ | ----- |
| Load URL | Index Page loads | Y |
| Click About Us | About us Page Loads | Y |
| Click Logo top right | Index page loads | Y |
| Click Home | Index page loads | Y |
| Click Gallery | Index page loads | Y |
| Click Medium | Drop down menu appears | Y |
| Click Oil and Canvas | Gallery with Oil and Canvas paints load | Y |
| Click Oil and Canvas | Gallery with Water colours load | Y |
| Click Oil and Canvas | Gallery with Sculptures load | Y |
| Click Oil and Canvas | Gallery with Drawings load | Y |
| Click Contact Us | contact us page loads | Y |
| Type oil in the search menu | oil paints load | Y |
| Click Shopping cart | shopping card loads with no items in | Y |
| Click Login | login page loads | Y |

### Logged In as standard user
| Load URL | Index Page loads | Y |
| Click My Account | My Account Page Loads | Y |
| Click About us | about us page loads | Y |
| Click Logo top right | Index page loads | Y |
| Click Home | Index page loads | Y |
| Click Gallery | Index page loads | Y |
| Click Medium | Drop down menu appears | Y |
| Click Oil and Canvas | Gallery with Oil and Canvas paints load | Y |
| Click Oil and Canvas | Gallery with Water colours load | Y |
| Click Oil and Canvas | Gallery with Sculptures load | Y |
| Click Oil and Canvas | Gallery with Drawings load | Y |
| Click Contact Us | contact us page loads | Y |
| Type oil in the search menu | oil paints load | Y |
| Click Shopping cart | shopping card loads with no items in | Y |
| Click Logout | User Logged out | Y |

### Logged in as staff user
| Load URL | Index Page loads | Y |
| Click My Account | My Account Page Loads | Y |
| Click Logo top right | Index page loads | Y |
| Click Home | Index page loads | Y |
| Click About | about page loads | Y |
| Click Gallery | Index page loads | Y |
| Click Medium | Drop down menu appears | Y |
| Click Oil and Canvas | Gallery with Oil and Canvas paints load | Y |
| Click Oil and Canvas | Gallery with Water colours load | Y |
| Click Oil and Canvas | Gallery with Sculptures load | Y |
| Click Oil and Canvas | Gallery with Drawings load | Y |
| Click Contact Us | contact us page loads | Y |
| Type oil in the search menu | oil paints load | Y |
| Click Shopping cart | shopping card loads with no items in | Y |
| Click Logout | User Logged out | Y |

## Footer (Same for all pages and User Types)
| Action | Expected Result | Pass |
| ----- | ----- | ----- |
| Click Facebook Logo | Loads Facebook Home Page | Y |
| Click Instagram Logo | Loads Instagram Page | Y |
| Click X (Twitter Logo) | Loads X (Twitter Home Page) | Y |

## Main Pages (Authentication not required)
### Index:
| Action | Expected Result | Pass |
| ----- | ----- | ----- |
| Note: If user is logged in message appears welcoming them | Y |
| Click explore gallery collection | Gallery page loads | Y |
| Click Meet our creators | creators page loads | Y |

### About us: 
| Action | Expected Result | Pass |
| ----- | ----- | ----- |
| Note text displays correctly no links on page | | Y |

### Gallery
| Action | Expected Result | Pass |
| ----- | ----- | ----- |
| Note: Page loads and filters to the left | | |
| Choose a Painting and click add to cart | cart to right has a 1 against it | Y |
| Choose another painting and click add to cart | car to the top right has a 2 against it | Y |
| In medium click each option | any paintings with the relevent tag appears | Y |
| Under artist click each artist name | only painting by that artist appear in the page | Y |
| Click Cart | Order page appers (click back) | Y |

### Contact Us
| Action | Expected Result | Pass |
| ----- | ----- | ----- |
| Complete Name, an invalid email address press submit | request to put valid email address apears | Y |
| Complete a vailid email address but leave message empty | request to add a message appears | Y |
| Complete a full and valid form | for sends email | Y |

## Standard User Journey
### Signup
| Action | Expected Result | Pass |
| ----- | ----- | ----- |
| Access the Site Unathenticated and from the login page (See Header Section) click Signup | Signup page loads | Y |
| Leave the First name blank and click Sumbit | returns to the top of the page | Y |
| Complete the first name leave the Last name blank and click submit | returns to the last name field | Y |
| Complete the last name leave the Username blank and click Sumbit | Returns to the username field| Y |
| Enter an invalid Email address (eg. no @ included) | Return to the email address field | Y |
| Enter a valid address (Street2 & County are not required) other fields required | form moves on | Y | 
| Complete last name so Username, Email, First Name and Last Name are all complete but password blank | Warning asking for password | Y |
| Add a password and confirmation thats less than 8 Charaters | Error asking for a stronger password | Y |
| Add a password with 9 numbers in the password & confirmation fields | Error showing password is entirely Numeric | Y |
| Enter the Username in the password and confirmation fields | Error showing its two short | Y |
| Enter the password & confirmation as `qwertyuiop` and click Sumbit | Error showing password is two common | Y |
| Enter a password that is valid but something diffrent one in Confirmation then click Sumbit | Error showing the two fields dont match | Y |
| Enter a valid passwrd but change email address with a previously used address eg. ana_lisa8@hotmail.com | warning will appear says its already registered | Y |
| Enter a valid password and the same confirmation and click Create account | Logs user in, Messgage showing account created for username, Welcome email sent to registed email address. | Y |

### Login
| Action | Expected Result | Pass |
| ----- | ----- | ----- |
| Ensure you are logged out and click the login button top right | login form appears | Y |
| Type an invalid username and password combination | login failed appears | Y |
| Login with correct details and takes you to the home page with message | Y |

# My Account
| Action | Expected Result | Pass |
| ----- | ----- | ----- |
| Click edit on the personal & Shipping details | personal and shipping details become editable | Y |
| edit something and click save | changes are reflected on the details page | Y |
| Note order history has all previous orders included | | Y |

### Checkout
| Action | Expected Result | Pass |
| ----- | ----- | ----- |
| From the gallery testing add a artwork to the card and click the cart icon | order page appears | Y |
| Procced to the checkout button | checkout page appears | Y |
| Check the address has appeared from the signup page | Y |
| enter test card details from stripe | card should validate | Y |
| Click adjust bag | returns you to order details page | Y |
| click complete order | order confirmation screen and email appears | Y |
Note: test stripe card details are here: https://docs.stripe.com/testing?locale=en-GB

### Order confirmation
| Action | Expected Result | Pass |
| ----- | ----- | ----- |
| Note order confirmation number appears | | Y |
| Note order details match the order created | | Y |
| Click back to gallery | gallery page appers | Y |

## Staff User Journey
### Login
| Action | Expected Result | Pass |
| ----- | ----- | ----- |
| Ensure you are logged out and click the login button top right | login form appears | Y |
| Type an invalid username and password combination | login failed appears | Y |
| Login with correct details and takes you to the home page with message | Y |

# My Account
| Action | Expected Result | Pass |
| ----- | ----- | ----- |
| Click edit on the personal & Shipping details | personal and shipping details become editable | Y |
| edit something and click save | changes are reflected on the details page | Y |
| Click Access Master Control Dashboard | staff portal page loads | Y |
| Click Add new art pieces to gallery | form to add new artwork appears | Y |
| Click add new artist Profiles | new artist profile appears | Y |
| Note order history has all previous orders included | | Y |


### Checkout
| Action | Expected Result | Pass |
| ----- | ----- | ----- |
| From the gallery testing add a artwork to the card and click the cart icon | order page appears | Y |
| Procced to the checkout button | checkout page appears | Y |
| Check the address has appeared from the signup page | Y |
| enter test card details from stripe | card should validate | Y |
| Click adjust bag | returns you to order details page | Y |
| click complete order | order confirmation screen and email appears | Y |
Note: test stripe card details are here: https://docs.stripe.com/testing?locale=en-GB

### Order confirmation
| Action | Expected Result | Pass |
| ----- | ----- | ----- |
| Note order confirmation number appears | | Y |
| Note order details match the order created | | Y |
| Click back to gallery | gallery page appers | Y |

### Dashboard
| Action | Expected Result | Pass |
| ----- | ----- | ----- |
| Login as a staff member and click staff portal | | |
| Click Add Artist top right | Add artist appears | Y |
| fill in details about a new artist ensure a name is included | new artist is added to the DB | Y |
| Note Total artists has increased by 1 | | Y |
| go to edit artist | artist details appear | | Y |
| Edit details for your new artist | updates details for artist | Y |
| Click delete for your new artist | confirmation box to delete artist, artist deleted when confirmed | Y |
| Click add artwork | Add artwork appears page appears | Y |
| Click back | return to the staff portal | Y |
| Click edit next to an artwork | loads change artwork page | Y |
| Change a value of an item and click save | detail is updated on the gallery page | Y |

### add artwork
From the staff portal click add artwork

| Action | Expected Result | Pass |
| ----- | ----- | ----- |
| Select the dropdown of artists | pick a chosen artist box populates | Y |
| Add a title & Descrption | boxes complete | Y |
| Choose a medium from the dropdown | chosen option is added to the box | Y |
| Add a price | then select an image | Y |
| Click choose an image | choose a image from file browser and confirm | image uploads to S3 | Y |
| Click confirm | artwork appears in the list | Y |

-----------------------------------------------------------------------------------------------

## Responsiveness Testing
### Header
| Device | Desired view |
| ----- | ----- | 
| Desktop | All menu options display with logo to the left and card / Login on the right |
| Smaller Devices | the middle row drops to a burger button to save space |

### Footer
| Device | Desired view | 
| ----- | ----- | 
| Desktop | the three sections appear across the page |
| Mobile | the three sections now are on top of each other |

### Index
| Device | Desired view | 
| ----- | ----- | 
| Desktop | All text centralised with artists 4 wide across the page |
| Smaller Devices | All text centralised with smaller boarders with artists two wide across the page |
| Smaller Devices | all text remains in the boxes and buttons that were created |

### About us 
| Device | Desired view | 
| ----- | ----- | 
| Desktop | All text centralised |
| Smaller Devices | Text remains central with smaller boarders |

### Gallery
| Device | Desired view | 
| ----- | ----- | 
| Desktop | Filters appear to the left hand side with all availible options to the right artworks appear in cards |
| Smaller Devices | Filters drop to a button at the top to save space artworks drop to 1 wide a page |

### Contact Us
| Device | Desired view |
| ----- | ----- |
| Desktop | wider boards but all boxes clear on screen |
| Smaller devices | smaller boards to give room for text boxes in form |

### Login
| Device | Desired view |
| ----- | ----- | 
| Desktop | Login box is smaller in the middle of the screen |
| Smaller Devices | box remains the same or similar size the boarders aroud the box shrink to fit. |

### Signup
| Device | Desired view | 
| ----- | ----- | 
| Desktop | Login box is smaller in the middle of the screen |
| Smaller Devices | box remains the same or similar size the boarders aroud the box shrink to fit. |

### My Account and Edit buttons
| Device | Desired view | 
| ----- | ----- |
| Desktop | Login box is smaller in the middle of the screen |
| Smaller Devices | box remains the same or similar size the boarders aroud the box shrink to fit. |

### Shopping Cart page
| Device | Desired view | 
| ----- | ----- | 
| Desktop | Items in the order are showen with pics to the left, Cost and total to the right |
| Smaller Devices | Items appear 1 wide with order summary below |

### Checkout Page
| Device | Desired view | 
| ----- | ----- |
| Desktop | Login box is smaller in the middle of the screen |
| Smaller Devices | box remains the same or similar size the boarders aroud the box shrink to fit. |

### Order confirmation
| Device | Desired view | 
| ----- | ----- | 
| Desktop | Login box is smaller in the middle of the screen |
| Smaller Devices | box remains the same or similar size the boarders aroud the box shrink to fit. |

### Staff Portal
| Device | Desired view | 
| ----- | ----- | 
| Desktop | Summary goes across the screen and the Inventory shows all the way across |
| smaller devices | the summary goes on top of each other and the Inventory scrolls across. |

### Add Artwork
| Device | Desired view | 
| ----- | ----- | 
| Desktop | Login box is smaller in the middle of the screen |
| Smaller Devices | box remains the same or similar size the boarders aroud the box shrink to fit. |

### Edit Artists
| Device | Desired view | 
| ----- | ----- |
| Desktop | Artists appear in cards 3 wide across the screen |
| Smaller Devices | Artists appear in two then 1 wide across the screen |

### Editing an artist 
| Device | Desired view | 
| ----- | ----- | 
| Desktop | Login box is smaller in the middle of the screen |
| Smaller Devices | box remains the same or similar size the boarders aroud the box shrink to fit. |

### Edit artwork
| Device | Desired view | 
| ----- | ----- | 
| Desktop | Login box is smaller in the middle of the screen |
| Smaller Devices | box remains the same or similar size the boarders aroud the box shrink to fit. |

------------------------------------------------------------------------------------------

## Final Product 

### Larger Screen View (tablets, Laptops, PC views:)

Home page View: 
![Homepage](assets/images/final-product/desktop/desktop-index.png)

About Us View: 
![About Us](assets/images/final-product/desktop/desktop-aboutus.png)

Gallery: 
![Gallery](assets/images/final-product/desktop/desktop-gallery.png)

Medium
![Medium](assets/images/final-product/desktop/desktop-medium.png)

Log In View:
![Log In](assets/images/final-product/desktop/desktop-login.png)

Header View:
![Header](assets/images/final-product/desktop/desktop-header.png)

Footer View:
![Footer](assets/images/final-product/desktop/desktop-footer.png)

Order: 
![order](assets/images/final-product/desktop/desktop-order.png)

Payment Confirmation:
![Payment Confirmation](assets/images/final-product/desktop/desktop-order-confirmation.png)

Contact Us Page:
![Contact Us Page](assets/images/final-product/desktop/desktop-contact.png)

SignUp Page:
![Sign Up Page](assets/images/final-product/desktop/desktop-signup.png)

Staff Portal Page 
![Staff Portal Page](assets/images/final-product/desktop/desktop-staff-portal-dashboard.png)

Staff Portal Edit Artwork Page 
![Staff Portal Edit Page](assets/images/final-product/desktop/desktop-staff-edit-artwork.png)

Staff Portal Edit Artist Page 
![Staff Portal Edit Page](assets/images/final-product/desktop/desktop-staff-edit-artist.png)

Staff Add an Artist Page
![Staff Add an Artist Page](assets/images/final-product/desktop/desktop-staff-add-artist.png)

Staff Add Artwork Page
![Staff Add Artwork Page](assets/images/final-product/desktop/desktop-staff-add-artwork.png)

Staff delete page
![Staff delete page](assets/images/final-product/desktop/desktop-staff-delete-artwork.png)

Footer view
![Footer](assets/images/final-product/desktop/desktop-footer.png)


## Mobile Screen Views:

Home page View: 
![Homepage](assets/images/final-product/mobile/mobile-index.png)

About Us View: 
![About Us](assets/images/final-product/mobile/mobile-aboutus.png)

Gallery: 
![Gallery](assets/images/final-product/mobile/mobile-gallery.png)

Medium
![Medium](assets/images/final-product/mobile/mobile-medium.png)

Log In View:
![Log In](assets/images/final-product/mobile/mobile-login.png)

Header View:
![Header](assets/images/final-product/mobile/mobile-header.png)

Footer View:
![Footer](assets/images/final-product/mobile/mobile-footer.png)

Order: 
![order](assets/images/final-product/mobile/mobile-order.png)

Payment Confirmation:
![Payment Confirmation](assets/images/final-product/mobile/mobile-order-confirmation.png)

Contact Us Page:
![Contact Us Page](assets/images/final-product/mobile/mobile-contact.png)

SignUp Page:
![Sign Up Page](assets/images/final-product/mobile/mobile-signup.png)

Staff Portal Page 
![Staff Portal Page](assets/images/final-product/mobile/mobile-staff-portal-dashboard.png)

Staff Portal Edit Artwork Page 
![Staff Portal Edit Page](assets/images/final-product/mobile/mobile-staff-edit-artwork.png)

Staff Portal Edit Artist Page 
![Staff Portal Edit Page](assets/images/final-product/mobile/mobile-staff-edit-artist.png)

Staff Add an Artist Page
![Staff Add an Artist Page](assets/images/final-product/mobile/mobile-staff-add-artist.png)

Staff Add Artwork Page
![Staff Add Artwork Page](assets/images/final-product/mobile/mobile-staff-add-artwork.png)

Staff delete page
![Staff delete page](assets/images/final-product/mobile/mobile-staff-delete-artwork.png)


--------------------------------------------------------------------------------

## Deployment


### Database
The database is hosted on AWS

#### To create the database:
- Login to AWS as a root user or IAM with enough privileges to Use Auroa / RDS and Security Groups
- In the search bar find RDS
- Click Create with full configuration
- Choose PostgressSQL
- Set the database server size (small in this case)
- Give the database a name that identifies it clearly.
- Set the Master Username and a Self Managed password 
- Enter a strong password (eg. 32 Charaters)
- Set Public access to yes as it will be accessible by Heroku
- Use a Default security group as its the first resource were creating
- Minimise Monitoring and backups to save on cost as this is a demo project
- Choose Create Database

#### Setup the security group
- As the database is creating at the bottom of the screen choose the default inbound security group 
- Choose the Security Group ID
- Click edit inbound rules
- Add a rule with
    Type: PostgresSQL
    Source: Custom and 0.0.0.0/0 as we dont know Heroku's puiblic IP

#### Go Back to RDS (From the Search Box)
- Choose Databases from the left menu 
- click into the new database that was created
- Under Code Sinippets change the Programming language to Python and copy the details to the env.py file to form the URI for Django.

### Setting up AWS S3
To allow for uploading images AWS S3 is setup to handle all static content setting up S3:
- Login to AWS using a root user or an IAM account with S3 permissons
- Create a new bucket and allow public read access. 
- To allow Django to upload & manage files create a policy that allows edit access to that bucket. 
- Create a user attach the policy to edit files in the bucket
- get the AWS region, Bucket name, AWS Secret key and AWS Key ID and add them to Heroku

### Application
Make sure gunicorn is in the project requirements and the code is upto date in github.

Login to Heroku
Create the application
- In Deploy link to the github repo for the project: brushed-up-things
- Click Setup and in config vars add:
    - Database credentials = (the full URL from AWS incluing username & password)
    - A Unique secret key for the project
    - EMAIL_HOST_PASSWORD = (Email service password)
    - EMAIL_HOST_USER = (Email service username)
    - AWS secret keys
    - Stripe secret keys & webhook
- Go back to deploy and click the deploy button to deploy the application.
- Confirm gunicorn is running in the resources tab.

----------------------------------------------------------

## Bug Fixes:

1. Connection Refused Error ( Error No 61)
![Connection Refused error](assets/images/bugs/bug1.png)

- The Issue: When attempting to register a new user account through the django-allauth signup flow, the application crashed, displaying a yellow ConnectionRefusedError [Errno 61] traceback page.

- The Root Cause: By default, django-allauth attempts to send a real email verification link immediately upon registration. Because a local development environment does not have a live SMTP email server configured, the connection request timed out and failed.

- The Fix: To safely simulate emails in development without a live server, the following setting was added to settings.py:
  EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
  This solution allowed Django to intercept all outgoing registration emails and print them directly to the terminal console instead of sending them to real email.

2. App Registry Not Ready error
![App Registry Not Ready Error](assets/images/bugs/bug2.png)

- The Issue: While attempting to implement Django signals for user profiles, the server instantly crashed upon startup, displaying django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet. in the terminal.

- The Root Cause: This occurred because the standard Django User model was being imported at the absolute top-level of profiles/apps.py. When Django initializes, it loads app      configurations before loading database models. Importing the User model here forced Django to look for a model that hadn't been loaded yet, breaking the startup sequence.

- The Fix: The top-level import was removed. Instead, the import was placed defensively inside the ready() method of the configuration class

![App Registry Not Ready Error](assets/images/bugs/bug2a.png)

3. Django-Allauth Profile Redirect 404 error
![Django-Allauth Profile Redirect 404 error](assets/images/bugs/bug3.png)
- The Issue: Upon successful user authentication (login or signup), the browser instantly crashed into a Page not found (404) error, explicitly attempting to target the URL path /accounts/profile/.

- The Root Cause: This occurred because Django-Allauth automatically routes users to a default internal fallback path (/accounts/profile/) after authentication if no other instruction is given. Because the custom profile dashboard in this project is explicitly mapped to /profile/ instead, Django's URL configuration could not find a matching route for the default path.

- The Fix: The brushed_up_things/settings.py file was updated to include an explicit redirect override. The LOGIN_REDIRECT_URL variable was added to the Allauth configuration block and set to target the named 'profile' route:
LOGIN_REDIRECT_URL = '/'

-----------------------------------------------------
## Future Developments:

### Dynamic Artist Directory & Portfolios
In future development phases, the platform can be upgraded to feature interactive artist profile pages, allowing shoppers to click on an artist's profile to view their biography, portrait, and a dedicated gallery showcasing only their specific artwork. This will be achieved by introducing an **Artist Model** linked to the existing **Artwork Model** using a "One-to-Many" database relationship (`ForeignKey`), which ensures store administrators or staff can dynamically manage and add new artists through the admin dashboard or the staff portal at any time. Behind the scenes, a single Django database query will fetch the clicked artist's profile, and an automated Python loop inside the template will dynamically render their entire inventory collection in a clean grid without requiring any hardcoded changes.

-----------------------------------------------------

## References: 
1. Unsplash Royalty Free Images - Mayur Deshpande
2. Unsplash Royalty Free Images - Europeana
3. Unsplash Royalty Free Images - Vineet Pathak
4. Unsplash Royalty Free Images - Europeana
5. Unsplash Royalty Free Images - Faith Washere
6. Unsplash Royalty Free Images - Boston Public Library
7. Stripe Payments Integration

   **Stripe Developer Documentation** – Utilized for the foundational JavaScript SDK architecture, including base Element initialization, secure UI iframe generation, and asynchronous payment lifecycle confirmation.  
   * *Source:* [Stripe Docs: Accept a Payment](https://stripe.com/docs/payments/accept-a-payment)
   * **Custom Django & jQuery Implementation** – Developed custom front-end logic to bridge the Django backend with the Stripe API. This includes using jQuery for dynamic DOM element selection, handling secure data-extraction and string sanitization via `.slice()`, and implementing defensive UI controls (disabling buttons and inputs) to prevent duplicate form submissions.

8. Models & Database Layer
 - Django Models Baseline: Understanding fields, relationships, and options used to model the gallery artwork assets.
   [Django Documentation - Models](https://docs.djangoproject.com/en/5.3/topics/db/models/)

 - Model Fields Reference: Specific guide on fields utilized for creating transactional tracking tables, such as `CharField`, `DecimalField`, and automatic `DateTimeField`.
   [Django Documentation - Model Field Types](https://docs.djangoproject.com/en/5.3/ref/models/fields/)

 - Database Relationships: Guide on utilizing `ForeignKey` constraints with cascade rules (`on_delete=models.CASCADE` and `models.PROTECT`) to connect line items securely to parent transaction records.
  [Django Documentation - Many-to-one relationships](https://docs.djangoproject.com/en/5.3/topics/db/examples/many_to_one/)

9. Views & Business Logic
 - Django View Layer Foundations: Structural design pattern for organizing HTTP request/response handling logic for processing checkouts and displaying details.
   [Django Documentation - Writing Views](https://docs.djangoproject.com/en/5.3/topics/http/views/)

 - URL Routing Configuration: Reference for constructing clean, consistent, cross-platform path structures linking named routes directly to views.
   [Django Documentation - URL dispatcher](https://docs.djangoproject.com/en/5.3/topics/http/urls/)

10. Forms & Data Validation

 - Django Forms Framework: Baseline architecture used to initialize, validate, and process frontend user inputs safely before committing data to storage.
   [Django Documentation - Working with Forms](https://docs.djangoproject.com/en/5.3/topics/forms/)

 - ModelForms Customization:** Step-by-step guidance on constructing secure forms bound directly to database definitions to manage inventory adjustments.
   [Django Documentation - Creating forms from models](https://docs.djangoproject.com/en/5.3/topics/forms/modelforms/)

 11. HTML Templates & Frontend Logic

 - The Django Template Language: Official documentation covering layout inheritances via `{% extends %}` and dynamic section injections via `{% block %}` structures.
   [Django Documentation - The Django Template Language](https://docs.djangoproject.com/en/5.3/topics/templates/)

 - Built-in Template Tags and Filters: Usage reference for loop operations (`{% for %}`), control blocks (`{% if %}`), and static asset loading mechanics (`{% load static %}`).
   [Django Documentation - Built-in Template Tags Reference](https://docs.djangoproject.com/en/5.3/ref/templates/builtins/)

 12. User Feedback & Session Messages

 - The Django Messages Framework: Reference for storing system feedback and executing template looping logic to render temporary success notifications or validation errors cleanly on the front end.
   [Django Documentation - The Messages Framework](https://docs.djangoproject.com/en/5.3/ref/contrib/messages/)
### Database Querying & Filtering References

#### 1. Handling HTTP GET Request Parameters
* **The HttpRequest Object (`request.GET`):** Reference for using dictionary-like query dicts to fetch user parameters (the text value assigned to `'q'`) directly from the browser's incoming URL address bar.
  * [Django Documentation - HttpRequest.GET QueryDicts](https://docs.djangoproject.com/en/5.3/ref/request-response/#django.http.HttpRequest.GET)

#### 2. Advanced Multi-Field Database Filtering
* **Complex Lookups with `Q` Objects:** Guidance on using `Q` objects to escape single-field limits. This architecture allows developers to combine database queries using logical OR operators (`|`) so a single search string can audit titles, descriptions, and mediums simultaneously.
  * [Django Documentation - Complex Lookups with Q Objects](https://docs.djangoproject.com/en/5.3/topics/db/queries/#complex-lookups-with-q-objects)

#### 3. Database Text Matching Constraints
* **Case-Insensitive Containment Lookups (`__icontains`):** Reference detailing field lookup modifiers used to evaluate whether a text string exists anywhere within a database record field while ignoring uppercase/lowercase differences.
  * [Django Documentation - Field Lookups: icontains](https://docs.djangoproject.com/en/5.3/ref/models/querysets/#icontains)