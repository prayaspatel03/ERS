Feature: Logs

  Background:
    Given Set Log id-"/api/v1/Logs"

  Scenario: User activity log, tracking the creation, updating, and deletion of charts and related objects.
    When Show all log entries, with all attributes
    And Show only log entries before "2018-01-03"
    And Show only log entries which apply to object "6DF36B83E25C38CE787E133BAF6208809D4A02D668C536CC763AF075FA35E9F1"
	And Show all of "shweta" changes since "2019-01-01"
	And Show only user and when attributes
	And Create a new event
    #Then I should be able to get true result from TestMode
