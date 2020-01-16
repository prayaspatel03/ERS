Feature: HelpDesks

  Background:
    Given Set HelpDesks id-"/api/v1/HelpDesks"

  Scenario: Access the list of available powerpoint presentation help deck versions.
    When Show all help deck versions
    And Show the help deck versions which are greater-than "1.0.0.0"
    #And Post the new help deck sion "1.0.8.0"
    #And Delete the help deck version "1.0.8.0"