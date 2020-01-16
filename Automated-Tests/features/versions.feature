Feature: Versions

  Background:
    Given Set Versions id-"/api/v1/Versions"

  Scenario: Version info on installed/running components.
    When Show all Versions