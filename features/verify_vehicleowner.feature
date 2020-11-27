Feature:Verify Vehicle owner


  Scenario: Login into the RentVehivle Page
    Given start chrome browser
    When open RentVehicle login page
    Then verify the logo present on the page
    And Enter emailid "admin@gmail.com" and password "admin@123"
    And Click on login button
    Then User must login to the home page


  Scenario: Navigate into driver section
    When Click on driver dropdown
    Then Select Drivers list
    And Click on Action view
    And Verify driver details pagge title
    Then Verify driver name
    Then Verify driver email
    Then Verify NIC number
    And Click on Go back button
    And close browser
