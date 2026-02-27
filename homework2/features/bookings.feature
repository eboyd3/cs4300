Feature: Movie Theater Booking System

  Scenario: List all movies
    Given the database has movies
    When I request the list of movies
    Then I should receive a 200 status code
    And the response should contain a list of movies

  Scenario: Check available seats
    Given the database has seats
    When I request available seats
    Then I should receive a 200 status code
    And the response should only contain unbooked seats

  Scenario: Authenticated user can create a booking
    Given I am logged in as a user
    And the database has movies
    And the database has seats
    When I create a booking
    Then I should receive a 201 status code
    And the seat should be marked as booked

  Scenario: Unauthenticated user cannot create a booking
    Given I am not logged in
    And the database has movies
    And the database has seats
    When I create a booking
    Then I should receive a 403 status code

  Scenario: User can only see their own bookings
    Given I am logged in as a user
    And another user has a booking
    When I request my booking history
    Then I should only see my own bookings