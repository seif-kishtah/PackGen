Feature: Send and Clear Packets

  Scenario: Send two packets and clear the send table
    Given I have started the PackGen application
    When I enter the first packet with the following details:
      | Name    | ASCII       | HEX             | Address     | Port | Type |
      | Packet1 | HelloWorld  | 48656C6C6F      | 192.168.1.1 | 8080 | TCP  |
    And I enter the second packet with the following details:
      | Name    | ASCII       | HEX             | Address     | Port | Type |
      | Packet2 | TestPacket  | 546573745061636B6574 | 192.168.1.2 | 8081 | UDP  |
    And I send both packets
    Then the send table should contain 2 packets
    When I click the Clear Log button
    Then the send table should be empty