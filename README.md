#search_by_words
This script makes a search in a text by words and return the phrases found with those words.

## How does it work?
Follow an example:

```python
  from search_by_words import search_by_words

  text = """
  Text messaging, or texting, is the act of composing and sending brief, electronic messages between two or more mobile phones, or fixed or portable devices over a phone network. The term originally referred to messages sent using the Short Message Service (SMS).
  It may simply be referred to as a text in North America, the United Kingdom, Australia, New Zealand and the Philippines, an SMS in most of mainland Europe, and an MMS or SMS in the Middle East, Africa, and Asia.
  Text messages can be used to interact with automated systems to, for example, to order products or services, or to participate in contests. Advertisers and service providers use direct text marketing to message mobile phone users about promotions, payment due dates, et cetera instead of using mail, e-mail or voicemail.
  SMS messaging was used for the first time on 3 December 1992, when Neil Papworth, a 22-year-old test engineer for Sema Group in the UK[6] (now Airwide Solutions),[7] used a personal computer to send the text message "Merry Christmas" via the Vodafone network to the phone of Richard Jarvis[8][9] who was at a party in Newbury, Berkshire which had been organised to celebrate the event.
  """

  search_by_words(text, 'SMS', 'MMS')
  # ['The term originally referred to messages sent using the Short Message Service (SMS)', 'It may simply be referred to as a text in North America, the United Kingdom, Australia, New Zealand and the Philippines, an SMS in most of mainland Europe, and an MMS or SMS in the Middle East, Africa, and Asia', ' SMS messaging was used for the first time on 3 December 1992, when Neil Papworth, a 22-year-old test engineer for Sema Group in the UK[6] (now Airwide Solutions),[7] used a personal computer to send the text message "Merry Christmas" via the Vodafone network to the phone of Richard Jarvis[8][9] who was at a party in Newbury, Berkshire which had been organised to celebrate the event']
```

## Contributing
### Running tests
```shell
  python test.py
```
