Feature: Projects

  Background:
    Given Set Projects id-"/api/v1/Projects"

  Scenario: List all (summaries about) each Project object.
    When Show all stored Projects
    And Show all Projects via If-None-Match
    And Show all Projects via If-None-Match and X-Long-Polling

  Scenario: Information about a single Project
    Given Set Projects id-"/api/v1/Project"
    When POST project using "sample_files\SimpleProject1.json"
    And Show new project using ID
    And Show new project via If-None-Match
    And Delete new project using ID
