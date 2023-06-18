# Manual Testing

[View the live project here.](https://pp5-all-tours.herokuapp.com/)

### Responsiveness:

![Responsiveness](/media/readme-images/responsiveness.jpg)

Images - 
Ipad Air
![Ipad](/media/readme-images/ipad_air_response.jpg)

Iphone XR
![Iphone](/media/readme-images/iphone_xr.jpg)

Desktop
![Desktop](/media/readme-images/desktop_response.jpg)

### Browser Compatibility:

![browser compatibility](/media/readme-images/browser_compatibility.jpg)

### Bugs:

During development two issues were experienced -

**1.** Server Error 500 on checkout after first deployment:
When I first ran through purchasing something after deploying my website I was getting a 500 server error.
**Resolution:-** I changed debug to true in order to see the error and it confirmed that I had input the wrong public key and secret key for stripe.  I corrected this and then checkout worked.

**2.** Forgot password function isn't working properly.
**Resolution:-** Unfortunately I have run out of time to resolve this.  An email
does get sent to the user to confirm a new password but the screens do not show this.
So the function works but just not cleanly.

### Lighthouse:

#### Desktop Device:

![Desktop Device](/media/readme-images/lighthouse_desktop.jpg)

#### Mobile Device:

![Mobile Device](/media/readme-images/lighthouse_mobile.jpg)

### Code Validation:

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [View Results](/media/readme-images/css_validator.png)

-   Python Validation - [View Results](/media/readme_images/python_validation.jpg)
		**Resolution:-**
		All lines of code showing as being too long was amended

### Testing User Stories from User Experience (UX) Section:

## User Stories Met:
As you will have seen from the main README document agile was used to meet the user story requirements.  This is clearly outlined in the different sprints.  

During testing, all tester were asked to action out the different user stories.  No issues were discovered.

### Further Testing:

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.