Feature: Configuration

  Background:
    Given I GET Configuration "/api/v1/Configuration/"

  Scenario: POST Configuration
    When I POST fVersion
    #And I GET TestMode in Configuration
    #And I POST TestMode in Configuration
    #Then I should be able to get true result from TestMode
