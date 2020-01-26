Feature: Flipkart order placement

  @chrome
  @debug
  Scenario: verify user is able to place an order through net banking
    Given the user opens Flipkart
     When  the user navigates to "Electronics/Mobile" options
      And  selects "OPPO"
     Then product list page is opened
     When  the user selects "OPPO A3s (Purple, 16 GB)"
      And  clicks on add to cart
      And the user navigates to Flipkart main page by clicking Home icon
      And the user navigates to cart page
     Then the item is present in cart
     When the user clicks on place the order
      And the user enters "9007935049" and "kolkata@1992"
      And  clicks on Submit
     Then user navigates to payment options page
     When  the user clicks on net banking
      And  selects bank as "Corporation Bank"
     Then user takes a screen shot of the page


