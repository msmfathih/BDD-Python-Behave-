Feature:Demo Automation Logo

  Scenario: Logo present on the Demo Automation Page
    Given start chrome browser
    When open demo automation login page
    Then verify the logo present on the page
    And close browser





