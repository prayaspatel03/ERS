Feature: slides

    Background:

        Given I POST project using
            |file                            | endpoint      |
            |sample_files\SimpleProject1.json|/api/v1/Project|

    Scenario: POST slide
        When I POST sample slide with same project ID that created using
            |file                           |endpoint       |
            |sample_files\SimpleSlide1.json |/api/v1/Slide |
        And I GET newly added slide using end point GET "/api/v1/Slide/" and Slide ID

