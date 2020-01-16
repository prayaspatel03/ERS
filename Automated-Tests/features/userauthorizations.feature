Feature: UserAuthorizations

  Background:
    Given Set UserAuthorizations id-"/api/v1/UserAuthorizations"

  Scenario: List all (summaries about) each UserAuthorization object.
    When Show all stored UserAuthorizations
    And Show current authentication information, including username and privileges
    And Post the new user "JIM"
    And Delete the user "JIM"