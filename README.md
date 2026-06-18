# Brushed Up Things! - An independent Art Gallery Catalog. 

## Table of Contents:

1. [About](#about)
2. [Business Goals](#business-goals)
3. [User Stories & Acceptance Criteria ](#user-stories-and-acceptance-criteria)
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
13. [CSS Validation Checks and Explanation of Results](#css-validation-checks)
14. [Python Validation Checks and Explanation of Results](#python-validation-check)
15. [Fixed](#fixed)
16. [Manual Testing of the website](#manual-testing)
17. [Responsiveness](#responsive-testing)
18. [Final Product](#final-product)
19. [Mobile Screen Views](#mobile-screen-views)
20. [Business Goals and User Stories met](#business-goals-and-user-stories-met)
21. [Deployment](#deployment)
22. [Bug Fixes](#bug-fixes)
23. [Project Constraints or Limitations](#project-constraints-or-limitations)
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

## User Stories & Acceptance Criteria:

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

    ![Logical Data Model](assets/images/erd-diagrams/logical-brushed-up-erd.png)

2. Physical Data Model (ERD):

    ![Physical Data Model](assets/images/erd-diagrams/physical-brushed-up-erd.png)

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