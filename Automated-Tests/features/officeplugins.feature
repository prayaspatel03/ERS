Feature: OfficePlugins

  Background:
    Given Set OfficePlugin id-"/api/v1/OfficePlugins"

  Scenario: Access the list of available office plugin versions.
    When Show all OfficePlugin versions
    And Show the OfficePlugin versions which are greater-than "1.0.0.0"
    And Post the new OfficePlugin sion "1.0.8.0"
    And Delete the OfficePlugin version "1.0.8.0"