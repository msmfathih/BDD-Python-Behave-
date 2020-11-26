Feature:Rent Vehicle Login


  Scenario: Login into the RentVehivle Page
    Given start chrome browser
    When open RentVehicle login page
    Then verify the logo present on the page
    And Enter emailid "admin@gmail.com" and password "admin@123"
    And Click on login button
    Then User must login to the home page
    And close browser


  Scenario Outline: Login into the RentVehivle Page with multiple parameter
    Given start chrome browser
    When open RentVehicle login page
    Then verify the logo present on the page
    And Enter emailid "<email>" and password "<password>"
    And Click on login button
    Then User must login to the home page
    And close browser


    Examples:
      | email                  |  password   |
      | admin@gmail.com        |  admin@123  |
      | ashikamrf71@gmail.com  |  ashika@91  |
      | ashikamrf51@gmail.com  |  ashika@91  |
















