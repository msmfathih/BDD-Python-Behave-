Feature:Rent Vehicle Login

  Scenario: Login into the RentVehivle Page
    Given start chrome browser
    When open RentVehicle login page
    Then verify the logo present on the page
    And Enter emailid "admin@gmail.com" and password "admin@123"
    And Click on login button
    Then User must login to the home page
    And close browser












