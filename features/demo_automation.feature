Feature:Demo Automation Login

  Scenario: Login into the Demo Automation Page
    Given start chrome browser
    When open demo automation login page
    Then verify the logo present on the page
    And Enter emailid "admin@gmail.com"
    And Click on login button
    Then User must login to the home page
    And close browser





