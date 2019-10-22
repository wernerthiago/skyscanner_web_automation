Feature: Home page
  As a user,
  I want to see the Something prompt

    Scenario: Website displays the Home components
        Given the website displays the "Home" page
        Then the website should display the "Origem" field
            And the website should display the "Destino" field
            And the website should display the "Ida" button
            And the website should display the "Volta" button
            And the website should display the "Buscar" button
  
    Scenario Outline: Website opens a Date Picker
        Given the website displays the "Home" page
        When the user clicks on the "<button_name>" button
        Then the website should display the "<prompt_name>" prompt
        Examples:
            |  button_name  |  prompt_name      |
            | Ida           | Ida Date Picker   |
            | Volta         | Volta Date Picker |

    Scenario Outline: Selecting a date on the Date Picker
        Given the website displays the "<prompt_name>" prompt
        When the user selects "<month>" month
            And the user selects "<day>" day
        Then the website should dismiss the "<prompt_name>" prompt
            And the website should display the "Home" page
        Examples:
            |  month            |  day  |  prompt_name      |
            | julho de 2020     | 1     | Ida Date Picker   |
            | setembro de 2020  | 1     | Volta Date Picker |

    Scenario: The website ables the user to be authenticated
        Given the website displays the "Home" page
        When the user types "Florianópolis" on the "Origem" field
            And the user types "Lisboa" on the "Destino" field
            And the user selects "julho de 2020" month at the "Ida Date Picker" prompt
            And the user selects "1" day at the "Ida Date Picker" prompt
            And the user selects "setembro de 2020" month at the "Volta Date Picker" prompt
            And the user selects "1" day at the "Volta Date Picker" prompt
            And the user clicks on the "Buscar" button
        Then the website should display the "Result" page