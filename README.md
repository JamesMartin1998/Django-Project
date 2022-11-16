# Cinema Planet - Movie Booking Website

Cinema Planet is the name of the make-believe company in my project. The company is a cinema chain that currently has three cinemas located in the UK. Like other cinemas, it functions by showing the latest, most popular movies. The Cinema Planet website aims to act as a venue for users to view the current movies available at cinema by naviagating through a movie menu. Users can also see information about the particular movies and are able to find the closest cinema to them via the implemented Google Maps API. Users are able to check upcoming showings for each movie and can even make a booking. After making a booking, the user has access to full CRUD functionality, being able to see their active bookings, edit them and delete them. Consequently, the Cinema Planet website gives the user full control over their bookings and acts as an alternative method to the traditional methods of booking cinema tickets, such as by physically visiting the cinema or calling the cinema by telephone. With the almost instant nature of booking online, as well as the easy control over bookings, the website provides the user with a superior user experience and thus represents an advantage for companies in a competitive market. 

The target audience for this project would include, but is not limited to, movie and cinema lovers. These people act as a prime customer for Cinema Planet as they would love the service provided by the cinema and its website. By making an optimal user experience on the website, and coupling it with adequate quality cinemas, it is likely that this demographic would be regular, recurrent customers. In addition, people that don't usually go to the cinema but perhaps occasionally want to visit would be more likely to visit the cinema if the booking system is simple. Thus, the Cinema Planet website appeals to a large audience.

![Image showing website responsiveness](./static/images/amiresponsive.png)

## UX Design and Planning

During the planning stage of this product, I thought about the functionality I want my website to provide to users and thus which pages would be needed to be created to implement the functionality.

### Home Page

![Image showing wireframe of homepage](./static/images/homepage-wireframe-logged-in.png)

For the home page, I aimed to provide users with a simple layout, which would immediately represent itself as a cinema website. Consequently, I included a clear brand logo and movie carousel. Navbar links are also intuitive.

![Image showing wireframe of homepage logged in](./static/images/homepage-wireframe-logged-in.png)

I wanted users to also be able to access their booking details from the homepage for a better user experience. Thus I aimed to include a section below the carousel to display booking details to logged in users.

### Movies Page

![Image showing wireframe of movies page](./static/images/movies-wireframe.png)

For the 'Movies' page, the aim for to simply display all of the movies on at the cinema, in an organised layout. Users are able to click the image or text links to find out more about the particular movie. I later decided to add a review section to the 'Movies' page.

### Booking Page

![Image showing wireframe of booking page](./static/images/booking-page-wireframe.png)

When planning the project, I was wondering about the best way to implement the functionality for users to make bookings for a movie. The plan for this page, to allow users to select a date, cinema, time and seat was quite ambitious due to its dynamic nature. I later separated the booking functionality into two pages. Firstly, one where users could select a defined showing (for a particular movie, at a date and specific time, at a specific cinema.) Secondly, a page where users could select the number of seats for their booking. This method proved to be a more realistic, yet still user friendly approach to providing the functionality. I also made separate pages for editing and deleting bookings.

### Find a Cinema Page

![Image showing wireframe of find a cinema page](./static/images/find-a-cinema-wireframe.png)

For the 'Find a Cinema' page, the aim was to show users the different locations of 'Cinema Planet' cinemas in an appealing way, using the Google Maps API.

### Sign Up Page

![Image showing wireframe of sign up page](./static/images/sign-up-page-wireframe.png)

For the 'Sign Up' page, the aim was to provide a simple, attractive form for users to register for an account.

### Sign In Page

![Image showing wireframe of sign in page](./static/images/log-in-wireframe.png)

Like the 'Sign Up' page, the aim of the 'Login' page was to provide a simple, attractive form for users to log into their accounts. Users don't need a 'Sign Out' page, as they can sign out by clicking the button on the navbar.

### User Story Planning

During the planning stage of the project, I produced a list of user stories. Further into the project, I realised that there was a need for more functionailty and thus I added some more user stories during the development of the project. I also decided that although some user stories were valuable, they were not necessary to include, particularly when considering the scope of the project. For example, the account email confirmation wasn't necessary as messages were displayed to the user to inform them that their account was created, instead. An Agile tool, in the form of GitHub, was used to manage the planning and implementation of all significant functionality. Issues were created for each user story and these were mapped to the project. During development, these user stories were accessed on a Kanban board, where I could organise my workload by moving the user stories between the 'Todo', 'In Progress' and 'Done' columns.

![Image showing user stoires](./static/images/user-stories.png)

## Features

### Navigation

- Displays the title of the website / name of the website to the user.
- A clear 'Open Sans' font is used to make the title and links easily visible for the user.
- The dark grey background and white font color create contrast to also aid visibility.
- Allows users to navigate between the different pages on the site.
- Hovering over the navbar links will cause a lightening effect to show that the elements are clickable.
- On smaller devices, a hamburger button appears and when clicked opens a drop-down of the navbar links in a vertical list. This prevents the navbar from taking up unnecessary space when not in use, on smaller devices.
- When users are logged out, they will see links to 'Sign Up' and 'Login'. Logged in users will instead see a 'Logout link'. This dynamic navbar provides users with access to the appropriate functionality for their circumstances, as well as indicates to them their login state.
- Created using bootstrap for a simple, responsive design.

![Image showing navbar](./static/images/navbar.png)
(Large device navbar - logged out)

![Image showing navbar](./static/images/navbar.png)
(Large device navbar - logged in)

![Image showing navbar](./static/images/navbar-mobile.png) <br />
(Small device navbar - Closed)

![Image showing navbar open](./static/images/navbar%20open.png) <br />
(Small device navbar - Open)

- Navbar code from https://getbootstrap.com/docs/5.2/components/navbar/

### Home Page Carousel

- This carousel section allows users to cycle thorugh images of the movies currently being shown at the cinema.
- Constributes to forming a modern, attractive landing page.
- Occupies the majority of the page to allow users to clearly see the type of website instantly upon loading the website.
- Regular customers can instantly know if the latest movies are being shown at the cinema by cycling through the carousel.
- Buttons used to allow the user to click and cycle left and right continuously through the loop of movies.

![Image showing movie carousel](./static/images/movie-carousel.png)
- JavaScript was used to provide the carousel functionality
- Carousel code from https://www.youtube.com/watch?v=9HcxHDS2w1s
- Buttons from FontAwesome

### Home Page Active Bookings

- This section only appears for users that are logged in, that have already made a booking. If a user isn't logged in, or has no active bookings, the section will not be displayed.
- By being located on the home page, users can easily find their booking information, and thus receive a convenient user experience.
- The title clearly shows users what the section is showing.
- When a user makes a new booking, the details of the booking appear as a new row in the table under the heading.
- The table headings are bold and the columns have margin so that the information for each column is clear to the user. Users are able to see their booking: 'Movie', 'Tickets', 'Date' and 'Time'.
- Users are able to have multiple bookings, new bookings append as new rows at the bottom of the table; allowing for users to easily see all of their bookings in a list format.
- Each booking has its own 'Edit' button. Clicking will redirect the user to a new page where they can edit the details of their booking.
- Each booking has its own 'Cancel' button. Clicking will redirect the user to a new page where they can confirm their cancellation.
- 'Edit' and 'Cancel' buttons appear red to stand out easily to the user. A white hover effect makes it obvious to the user that the buttons are clickable.
- Due to the nature of the table being difficult to display on smaller devices, some less important booking details will become hidden to the user to allow the page to be responsive. Bookings can still be identified as sufficient information is kept visible for the uesr and if the user wishes to find all of the details of their booking, they can do so by clicking the 'Edit' button and viewing the details on the 'Edit Booking' page.

![Image showing active bookings](./static/images/active-bookings.png)
(Large device - Active Bookings)

![Image showing active bookings on mobile device](./static/images/active-bookings-mobile.png) <br />
(Mobile - Active Bookings)

### Footer

- This section aims to promote users to find out more about the cinema through social media, as well as provide the user with information about the cinema opening times and contact email.
- This section follows the same design theme as the navigation bar for consistency.
- Social links are included as icons from FontAwesome.
- When clicked, the links open in a new tab for a good user experience.
- On larger devices, the three sections are horizontal, but the navbar is also responsive and adopts a vertical layout on smaller devices.
- Code for this section was used from Code Institute's Love Running Project.

![Image showing footer](./static/images/footer.png)
(Large device - Footer)

![Image showing footer on medium-sized device](./static/images/footer-medium-device.png) <br />
(Medium device - Footer)

![Image showing footer on mobile device](./static/images/footer-mobile.png) <br />
(Large device - Footer)

### Movies

- Acts as a catelogue for users to browse through the current movies being shown at the cinema.
- The title at the top of the page, 'What's On?', makes it clear to the user that this page is showing the movies available to see at the cinema at the moment.
- Each movie has an image link and title link which will direct the user to a new page showing the details of the particular movie.
- Title links have a bold hover effect to inform the user that they are clickable links.
- On large devices, the movies are arranged as a grid, three columns wide. This grid reduces to two wide on medium devices and to a singular column on mobile devices. This responsive design enables movie images to be seen clearly on all devices; improving the user experience.

![Image showing movies page](./static/images/movies-page.png)
(Large device - Movies Page)

![Image showing movies page on medium device](./static/images/movies-page-medium-device.png) <br />
(Medium device - Movies Page)

![Image showing movies page on medium device](./static/images/movies-page-mobile.png) <br />
(Mobile device - Movies Page)

### Movie Detail

- Acts to provide the user with more information about a particular movie previously selected.
- Title and movie image clearly show the movie that this page is representing.
- A movie description is shown to explain the basic plot of the film do users can learn a little more about the movie before booking a ticket.
- Run time also shown for the user.
- A clear, red button, consistent with other buttons on the website, is labeled 'Book'. When clicked, users are redirected to a page showing the available showings for this movie. The white hover effect reinforces that the button is clickable.

![Image showing movie detail](./static/images/movie-detail.png)

### Reviews

- Allows users to read and make reviews about the selected movie.
- The review section is separated from the rest of the page with a horizontal rule. This clearly defines the sections to the user whilst keeping the reviews on the same page is its core information.
- The 'Make a Review' title and form are only displayed and made available for logged in users. This is due to the reviews requiring a username.
- The form body acts as an area for users to write their reviews.
- A clear, red button, consistent with other buttons on the website, is labeled 'Submit'. When clicked, the user's review will be posted.
- The ability of being able to make a review makes the website more appealing to users that want to share their opinions.
- All users, including logged out users, are able to read the reviews made by other users. This enables users to learn more about the movie before deciding to book a ticket. This additional feature may act as an advantage over rival cinemas that don't include this feature.
- The reviews stack vertically in a column. Information about the review, such as the author, date and time are displayed in bold, with the review underneath. Collectively a clear, pleasant layout for the reviews is created.
- Having reviews creates a greater community on the website, perhaps encouraging more user interaction and returning customers.

![Image showing reviews](./static/images/reviews.png)

- Reviews section adapts on the Comment code from Code Institute's Django Blog project.

### Showings

- Allows users to see the available showings for the selected movie.
- Title and movie image clearly show the movie that this page is representing.
- 'Next Availble Showings' title clearly informs the user that subsequent information is about the movie's showings.
- Small paragraph explains to users that they can book their tickets online, however will pay when the collect the tickets in person at the cinema. This helps the user avoid confusion over the ticket purchasing process.
- Each available showing is displayed in its own row in a table.
- The table headings are bold and the columns have margin so that the information for each column is clear to the user. Users are able to see their booking: 'Movie', 'Location', 'Date', 'Time', 'Seats remaining' and 'Ticket Price'.
- The information shown about each showing allows users to make a choice based on their circumstances and preferences. For example, users can search for a showing at their closest cinema, at their favoured date and time. Users are also able to see if there are enough seats remaining for their attending party and whether the price is satisfactory before clicking on a showing to book. This therefore provides a beneficial user experience.
- Due to the table being difficult to show on smaller devices. The page acts responsively to maximise its use of space by hiding the 'Movie' column as it is clear that the showings are for the selected movie with the title and image above. In addition, the ticket price is consistent for all showings of a particular movie so this column is hidden and the information is provided above the table. The seats remaining information is also becomes hidden but is made available by being displayed on the next page.
- Each movie showing row has its own 'Book' button. By clicking this button, if the user is logged in, they can select a showing and will be redirected to page where they can select their number of tickets are confirm their booking. If the user is logged out, clicking the link will redirect the user to the 'Sign In' page; as only authenticated users are able to make bookings. This is consistent with other buttons on the website, reinforcing the theme. The white hover effect, again, shows that the button is clickable.

![Image showing movie showings](./static/images/showings.png)
(Large device - Showings Page)

![Image showing movie showings on mobile device](./static/images/showings-mobile.png) <br />
(Mobile device - Showings Page)

### Order

- The order page allows users to finalise their booking by selecting the number of tickets to add to their booking and confirming all of the booking details.
- Page can only be accessed by by logged in users.
- The title clearly shows the important details about the movie, location, date and time. This allows the user to check their booking before ordering.
- The image shows the movie selected and continues the theme of the pages in the booking process.
- The remaining booking information uses bold titles to make the details eye-catching to the user.
- The seats remaining information allows users on mobile devices to check if there are enough seats for their party before booking. This is important as mobile users were not able to see this information on the previous page.
- Users are able to select the number of tickets they want to include in their order. Tickets are capped at 8 per booking to prevent people for booking the whole cinema.
- Users are also prevented from inputting 0 tickets, strings, a negative number of tickets, floats and more tickets than available seats remaining.
- If users attempt to submit an invalid form, they will receive an error message, explaining the problem and the page will reload.
- The 'Order' button is consistent with other buttons on the website. When clicked, the user will receive a success message, confirming their order and is redirected to the home page. Users will see their booking in the 'Active Bookings' section.

![Image showing order page](./static/images/order.png)

### Edit Booking
 - Enables users to change the details of their bookings.
 - Accessed by clicking the 'Edit' button, for a particular booking in the 'Active Bookings' section.
 - The movie title and image is used to continue the consistent theme as throughout and clearly show the user the movie selected in their booking.
 - Using the 'Showing' dropdown box, users are able to change their showing for the selected movie. This enables them to change to a more suitable location, date, time.
 - Users are also able to input a new 'Number of Tickets'. This enables users to have flexibility over situations where additional people want to join there party, as well as if members need to cancel their ticket without canceling the whole group.
 - The 'Number of Tickets' input, has the same valiadtion applied as the for the 'Order' form. Consequently users are unable to book tickets that are a higher amount than the remaining number of seats remaining for the showing, a negative number of tickets, more than eight tickets, 0 tickets, string values or float values. Attempting to submit the form with one of these invalid formats will result in an error message to explain the problem, and the page reloading.
 - If the user decides to change the number of tickets for a booking, the number of seats remaining for the affected showing or showings will update correctly.
 - Upon submission of a valid form by clicking the 'Submit' button, the user will receive a success message to inform them that their booking has updated successfully and they will be redirected to the home page. The user is then able to see their new booking details in the 'Active Bookings' section.

![Image showing edit booking page](./static/images/edit.png)

 - JavaScript was used to filter out showings for other movies than that in the original booking. This enables showings that only include the same movie as the original booking to be shown in the dropdown box.
 - Code was recommended to me by my Korean developer friend, from this website: https://goodsgoods.tistory.com/249

 ### Cancel Booking

 - Enables users to easily cancel a booking.
 - Accessed by clicking the 'Cancel' button, for a particular booking in the 'Active Bookings' section.
 - The movie title and image is used to continue the consistent theme as throughout and clearly show the user the movie selected in their booking.
 - Users are asked one last time to confirm their cancellation.
 - The 'Delete Booking' button has a red background and white hover effect, consistent with the theme throughout the project.
 - When the 'Delete Booking' button is clicked, the booking will be deleted and the user will receive a success message to explain that their booking has been deleted. They will then be redirected to the home page and their booking will be absent from the 'Active Bookings' section.
 - Upon deletion, the 'Showing' from the 'Booking' will have its number of seats remaining updated correctly.
 - This feature provides a good user experience as users can quickly cancel their booking without spending time emailing or calling with staff.

![Image showing delete booking page](./static/images/delete.png)

### Find a Cinema

- Allows users to easily locate cinemas close to them visually.
- Title inform the user that they can use the Google Map to locate cinemas.
- The map fills the majority of the screen making it easily visible to users.
- The map loads automatically with focus on the UK, as all cinemas are located here.
- Upon loading, users can see one marker for Manchester and a cluster for Brighton and London, as they are close together. By clicking the cluster, the user can then see Brighton and London as individual markers.

![Image showing find a cinema page](./static/images/find-a-cinema.png)

- Implemented using the Google Maps API and JavaScript.
- Code was used from Code Institute's Bootstrap Resume project.

 ### Sign Up

- Allows users to register for an account.
- Clear title informs users that this page will allow them to sign up for an account.
- The form is clearly laid out in the center of the page.
- Paragraph provides a link to the 'Sign In' page in case user already have an account.
- Users are required to input a username, password and password confirmation, whilst having the option to provide an email address. Form validation prevents users from submitting the form without filling these required fields.
- The 'Sign Up' button is conistent with other buttons and is clearly visible and clickable.
- By clicking the 'Sign Up' button, users will receive a success message to inform them that they have successfully logged in, and they are redirected to the home page.

![Image showing sign up page](./static/images/sign-up.png)

### Login

- Allows users to sign into an account.
- Clear title informs users that this page will allow them to sign into an account.
- The form is clearly laid out in the center of the page.
- Paragraph provides a link to the 'Sign Up' page in case user don't already have an account.
- Users are required to input a username and password. Form validation prevents users from submitting the form without filling these required fields.
- Users can check the 'Remember Me' box to make their signing in process more convenient in the future.
- The 'Sign In' button is conistent with other buttons and is clearly visible and clickable.
- By clicking the 'Sign In' button, users will receive a success message to inform them that they have successfully logged in, and they are redirected to the home page.

![Image showing sign in page](./static/images/sign-in.png)

### Logout

- Allows users to sign out of an account instantly by clicking the 'Logout' button in the navbar.
- Users receive a success message and are redirected to the home page.

### Messages

- Alert the user after success and error events.
- Messages confirm to the user that an event has occurred successfully, and explain why an error has occurred.
- Examples of success events include: a user logged into an account, completing a booking, deleting a booking, etc.
- Error events arise when invalid data is submitted in forms and thus events can't be performed, e.g. trying to order more tickets than seats available.
- Messages appear in the center of the sceen, under the Navbar so they can easily be located. 
- A green background is used for success messages, whereas red is used for errors. This allows used to differentiate between them easily.
- Messages disappear automatically after 2.5 seconds, or they can be closed by clicking the 'X' button in the top right corner, before.
- Overall the feedback provided by messages enhances the user experience greatly.

![Image showing success message](./static/images/success-message.png)
(Success Message Example)

![Image showing error message](./static/images/error-message.png)
(Error Message Example)

- Bootstrap alerts were used with JavaScript to create the messages.
- Code was used from Code Institute's Django Blog project.

### Admin Roles

- Admins are able to create, read, update and delete movies, showings, bookings and reviews on the website via the Django admin site.
- Admins are responsible for listing new movies when they are being shown at the cinema, as well as deleting them when they are no longer being shown.
- Admins are responsible for listing the showings for each movie to keep the website up-to-date.
- As the cinema website needs to evolve constantly to keep up-to-date with new movies and showings. The admin has a critically role in enabling this website's functionality.

## Manual Testing

For this Django project, extensive manual testing was performed.

### High Level Test Cases

![Image showing test cases part 1](./static/images/test-cases-1.png)
![Image showing test cases part 2](./static/images/test-cases-2.png)
![Image showing test cases part 3](./static/images/test-cases-3.png)

Mapped to user stories:

![Image showing user stories mapped to test cases](./static/images/user-stories-mapped.png)

### High Level Test Case Results

![Image showing test cases results](./static/images/test-case-results.png)

Full Results can be found [here](django-project-testing.xlsx)

## Validator Testing

### W3C HTML Validator

Tests performed at https://validator.w3.org/nu/

- Home Page - No errors

![Image showing home page HTML validation](./static/images/homepage-w3c.png)

- Movies Menu Page - No errors

![Image showing Movies Menu page HTML validation](./static/images/movies-w3c.png)

- Movie Details Page - No errors

![Image showing Movie Details page HTML validation](./static/images/movie-detail-w3c.png)

- Movie Showings Page - No errors

![Image showing movie showings page HTML validation](./static/images/movie-showings-w3c.png)

- Booking Order Page - No errors

![Image showing find a cinema page HTML validation](./static/images/find-a-cinema-w3c.png)

- Edit Booking Page - returns error on the form due to the jinja template being used to import the form

![Image showing edit booking page HTML validation](./static/images)

- Cancel Booking Page - No errors

![Image showing cancel booking page HTML validation](./static/images/delete-w3c.png)

- Sign Up Page - No errors

![Image showing sign up page HTML validation](./static/images/sign-up-w3c.png)

- Login Page - No errors

![Image showing sign in page HTML validation](./static/images/login-w3c.png)

### W3C CSS Validator

- style.css - No errors

![Image showing style.css validation](./static/images/style.css-w3c.png)

### JSHint

- Messages JavaScript Code - No errors

![Image showing messages jshint validation](./static/images/messages-jshint.png)

- maps.js - No errors

![Image showing maps.js jshint validation](./static/images/maps.js-jshint.png)

- script.js - No errors

![Image showing maps.js jshint validation](./static/images/script.js-jshint.png)

- Edit Booking Script

![Image showing Edit Booking jshint validation](./static/images/edit-booking-script-jshint.png)








