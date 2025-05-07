# Created by jacki at 4/23/2025
Feature: Test Scenarios for User Guide functionality

  Scenario: User can open User guide page
    Given Open Reelly main page
    When Enter email: jackiemettler@yahoo.com
    And Enter password: si5xFhT&$74dG#DN
    And Click continue
    And Click on the settings option
    And Click on the User Guide Option
    Then Verify User Guide page opens
    And Switch to iFrame
    And Verify the lesson video title is: Full overview of Reelly platform

  @mobile
  Scenario: Mobile User can open User guide page
    Given Open Reelly main page
    When Enter email: jackiemettler@yahoo.com
    And Enter password: si5xFhT&$74dG#DN
    And Click continue
    And Click on the settings icon
    And Click on the Mobile User Guide Option
    Then Verify User Guide page opens
    And Switch to iFrame
    And Verify the lesson video title is: Full overview of Reelly platform