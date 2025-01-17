Feature: Search Packets in Saved Table

  Scenario: Search for packets in the saved table
    Given I have started the PackGen application
    And I have saved the following packets:
      | Name      | ASCII       | HEX             | Address     | Port | Type |
      | Packet1   | HelloWorld  | 48656C6C6F      | 192.168.1.1 | 8080 | TCP  |
      | Packet2   | TestPacket  | 546573745061636B6574 | 192.168.1.2 | 8081 | UDP  |
      | Packet3   | DataPacket  | 446174615061636B6574 | 192.168.1.3 | 8082 | SSL  |
    When I type "Packet" in the search field
    Then the saved table should show 3 packets
    When I type "Packet1" in the search field
    Then the saved table should show 1 packet
    When I type "Hello" in the search field
    Then the saved table should show 1 packet
    When I clear the search field
    Then the saved table should show 3 packets