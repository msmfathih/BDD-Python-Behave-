Feature:Demo Automation Login

  Scenario: Login Demo Automation with valid Parameter
    Given start chrome browser
    When open demo automation login page
    And Enter emailid "admin@gmail.com"
    And Click on login button
    Then User must login to the home page
    And close browser








