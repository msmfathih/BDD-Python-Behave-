Feature:Rent Vehicle Login


  Background: Common Steps
    Given start chrome browser
    When open RentVehicle login page
    Then verify the logo present on the page
    And Enter emailid "admin@gmail.com" and password "admin@123"
    And Click on login button

  Scenario: Login into the RentVehivle Page
    Then User must login to the home page


  Scenario: Fill Driver Registration Form
    When Click om Drive dropdown
    Then Click on Driver Registration Page
    And Enter Drivername "aadil"
    And Enter PhoneNumber "97152854262"
    And Enter Emailid "aadil@gmail.com"
    Then Upload Licence copy file
    Then Click Owner of this vehicle
    Then Select Dropdown Vehicle
    And Click submit button
    And close browser


























